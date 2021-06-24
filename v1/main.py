from files import FileManager
from indexer import Indexer
from search import Search

if __name__ == '__main__':
    dirs = [
        '../data'
    ]
    index_file = '../data/temp/index.txt'
    posting_list_file = '../data/temp/postinglist.txt'
    scan_list_file = '../data/temp/scan.txt'

    file_manager = FileManager(path_folders=dirs, scan_file_dir=scan_list_file, strip_ch='!?,.\n')
    indexer = Indexer(file_manager=file_manager,index_file_dir=index_file,posting_file_dir=posting_list_file)
    inverted_index=indexer.update_tokens()
    search_ob = Search()
    query = "NOT passion"
    print(search_ob.process_query(query=query,inverted_index=inverted_index))
    print(inverted_index)
