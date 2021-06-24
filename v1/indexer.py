from collections import deque, OrderedDict, Counter
from files import IndexFile, PostingList


class Indexer(object):
    def __init__(self, file_manager, index_file_dir, posting_file_dir):
        self._file_manager = file_manager
        self._index_file = IndexFile(path=index_file_dir)
        self._posting_file = PostingList(path=posting_file_dir)

    def update_tokens(self):
        """
        this method update the token by giving them from file manager
        :return:
        """
        tokens, update = self._file_manager.get_tokens()

        if update == 'updated-scan':
            all_in_one = list()
            for idx, token in tokens:
                all_in_one.extend(token)

            cnt = Counter(all_in_one)

            indexes = dict()
            for key, value in cnt.items():
                occ_list = list()
                for idx, token in tokens:
                    if key in token:
                        occ_list.append(idx)
                occ_list = sorted(occ_list)

                indexes[key] = (value, occ_list)

            inverted_index = indexes
            self.write_inverted_index(indexes)
            return inverted_index

        else:
            return self.read_files()

    def write_inverted_index(self,inverted_index):
        """
        write inverted index to files
        :param inverted_index:
        :return:
        """
        index_file = dict()
        posting_list = list()

        for key,value in inverted_index.items():
            index_file[key]=value[0]
            posting_list.append((key,value[1]))

        self._index_file.write_lines(IndexFile.format_to_write(index_file))
        self._posting_file.write_lines(PostingList.format_to_write(posting_list))

    def read_files(self):
        index_file = self._index_file.read()
        posting_file = self._posting_file.read()

        inverted_index = dict()
        for term, doc_idx in posting_file:
            inverted_index[term] = (index_file[term], doc_idx)

        return inverted_index