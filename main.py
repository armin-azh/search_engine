from atlasobscura import atlasobscura_crawler
from theplanetd import theplanetd_crawler

import json

def merge_crawlers():
    
    crawler_atlasobscura = atlasobscura_crawler()
    crawler_theplanetd = theplanetd_crawler()
    
    data = { "theplanetd": crawler_theplanetd , "atlasobscura": crawler_atlasobscura}
    
    return data


if __name__ == '__main__':
    
    crawler_data = merge_crawlers()

    with open(r'E:\crawl_data.json', 'w') as data:
        json.dump(crawler_data , data)