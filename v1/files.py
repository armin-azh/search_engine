import os
import hashlib
import sys
from collections import defaultdict
from tokenizer import Tokenizer


class File(object):
    """
    this class is for keeping file states
    """

    def __init__(self, doc_id, path, sha1, status='new'):
        self._doc_id = doc_id
        self._path = path
        self._sha1 = sha1
        self._status = status

    @property
    def get_doc_id(self):
        return self._doc_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, x):
        self._status = x

    @property
    def sha1(self):
        """
        getter for sha1
        :return:
        """
        return self._sha1

    @sha1.setter
    def sha1(self, new_val):
        """
        setter for sha1
        :param new_val: new sha1 value
        """
        self._sha1 = new_val

    @staticmethod
    def read_file(f_path):
        """
        this method read whole file
        :return joined lines: (string)
        """
        with open(f_path, 'r') as f:
            lines = f.readlines()
        return "".join(lines)

    @property
    def path(self):
        """
        property for getting file full path
        :return file path:
        """
        return os.path.join(self._path, self._file_name)

    def parse_file_path(self):
        """
        :return filename,filepath:
        """
        return os.path.basename(self._path), os.path.dirname(self._path)


class PostingList(object):
    def __init__(self, path):
        self._posting_list_directory = path if os.path.isfile(path) else sys.exit("Posting list file does not exists")

    def read(self):
        with open(self._posting_list_directory, 'r') as f:
            lines = f.readlines()

        posting_list = list()

        for line in lines:
            line = line.strip('\n')
            line = line.split(' ')
            doc_ids = [int(idx) for idx in line[1:]]
            posting_list.append((line[0], doc_ids))

        return posting_list

    def write_lines(self, lines):
        f = open(self._posting_list_directory, 'w')

        for line in lines:
            f.write(line)

        f.close()

    @staticmethod
    def format_to_write(ps):
        """
        convert posting list to writable format
        :param ps: posting list
        :return: formatted line
        """
        lines = list()
        for term, doc_ids in ps:
            doc_ids = [str(idx) for idx in doc_ids]
            doc_ids = " ".join(doc_ids)
            line = "{} {}\n".format(term, doc_ids)
            lines.append(line)
        return lines


class IndexFile(object):
    def __init__(self, path):
        self._index_directory = path if os.path.isfile(path) else sys.exit("Index file does not exists.")

    def read(self):
        with open(self._index_directory, 'r') as f:
            lines = f.readlines()

        index_dic = defaultdict(int)

        for line in lines:
            line = line.strip('\n')
            line = line.split(' ')
            index_dic[line[0]] = int(line[1])

        return index_dic

    def write_lines(self, lines):
        f = open(self._index_directory, 'w')

        for line in lines:
            f.write(line)

        f.close()

    @staticmethod
    def format_to_write(dic):
        lines = list()
        for key, value in dic.items():
            line = "{} {}\n".format(key, str(value))
            lines.append(line)
        return lines


class ScanFile(object):
    def __init__(self, path):
        self._scan_file = path if os.path.isfile(path) else sys.exit("Scan file does not exists.")

    def read(self):
        with open(self._scan_file) as f:
            lines = f.readlines()

        watched_lines = list()
        for line in lines:
            line = line.strip('\n')
            line = line.split()
            watched_lines.append((line[0], line[1]))
        return watched_lines

    def write_lines(self, lines):
        f = open(self._scan_file, 'w')

        for line in lines:
            f.write(line)

        f.close()

    @staticmethod
    def format_to_write(scan_list):
        lines = list()
        for l in scan_list:
            line = "{} {}\n".format(l[0], l[1])
            lines.append(line)
        return lines

    @staticmethod
    def get_paths(scan_list):
        paths = list()
        for l in scan_list:
            paths.append(l[0])
        return paths


class FileManager(object):
    """
    This class do managing steps on all files
    """

    def __init__(self, path_folders, strip_ch,scan_file_dir):
        """
        :param path_folders: file directories
        :param strip_ch:
        """
        self._path_files = self.expand_folder_path(path_folders)
        self._tokenizer = Tokenizer(strip_ch=strip_ch)
        self._scan_file = ScanFile(path=scan_file_dir)

    @staticmethod
    def expand_folder_path(paths, ex='.txt'):
        """
        this method expand all txt file in a folder path
        :param ex:
        :return:
        """
        file_paths = list()
        for base in paths:
            if os.path.isdir(base):
                dirls = os.listdir(base)
                for name in dirls:
                    if os.path.splitext(name)[1] == ex:
                        file_paths.append(os.path.join(base, name))
            elif os.path.isdir(base) and os.path.splitext(base):
                file_paths.append(base)

        return file_paths

    def status(self):
        """
        check that scan path need any changes or not
        :return:
        """
        scan_paths_list = self._scan_file.read()
        scan_paths = self._scan_file.get_paths(scan_paths_list)
        if len(scan_paths) == len(self._path_files) and self.check_files(scan_paths) and self.check_files_changes(
                scan_paths_list):
            return True
        else:
            # update whole states
            return False

    def check_files(self, scan_path):
        signal = True
        for path in scan_path:
            if path not in self._path_files:
                signal = False
                break
        return signal

    def check_files_changes(self, scan_paths_list):
        signal = True
        for path, sha1 in scan_paths_list:
            idx = self._path_files.index(path)
            if sha1 != FileManager.generate_file_sha1(File.read_file(self._path_files[idx])):
                signal = False
                break
        return signal

    def update(self):
        """
        this method update paths if necessary
        :return:
        """
        if self.status():
            return 'not-updated-scan'
        else:
            new_scan_paths_list = list()
            for path in self._path_files:
                new_scan_paths_list.append((path,FileManager.generate_file_sha1(File.read_file(path))))
            self._scan_file.write_lines(ScanFile.format_to_write(new_scan_paths_list))
            return 'updated-scan'

    def get_tokens(self):

        update = self.update()

        if update == 'updated-scan':
            tokens = list()
            for idx, path in enumerate(self._scan_file.get_paths(self._scan_file.read())):
                temp = (idx, self._tokenizer.get_token(File.read_file(path)))
                tokens.append(temp)
            return tokens, update
        else:
            return None, update

    @staticmethod
    def generate_file_sha1(read_lines):
        """
        generate file sha1
        :param read_lines: encoded read_lines
        :return: sha1
        """
        return hashlib.sha1(read_lines.encode()).hexdigest()
