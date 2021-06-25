import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def theplanetd_crawler():
    site = requests.get(r"https://theplanetd.com/travel-blog/")
    soup = BeautifulSoup(site.text, 'html.parser')
    links = soup.select('#wpsp-2863 > article.wp-show-posts-single > div > div > a')
    pages = int(soup.select("div.wpsp-load-more> a")[-2].text)
    theplanetd = []
    data = {}
    docid = 1

    for index , i in enumerate(links):
        blog = requests.get(i['href'])
        soup = BeautifulSoup(blog.text, "html.parser")

        contenttags = soup.select("div.inside-article > div.entry-content > div:not(.gb-container.gb-container-77275a9a,.ez-toc-v2_0_17.ez-toc-wrap-left.counter-hierarchy, .gb-container.gb-container-b3e80905)")

        txt = ''
        images = []
        for tag in contenttags:
            txt += tag.text
            if tag.find("img"):        
                images.append(tag.find("img")['data-pin-media'])
        try:
            header_img = i.img['nitro-lazy-src']
        except:
            header_img = 'null'

        data[str(docid)] = {
            'title' : i['title'],
            'header_img' : header_img,
            'text' : txt,
            "images" : images,
            'link' : i['href']
        }
        docid += 1
        theplanetd.append(data)



    for i in tqdm(range (2 , 20)):
        page = requests.get(f"https://theplanetd.com/travel-blog/page/{i}/")
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.select('#wpsp-2863 > article.wp-show-posts-single > div > div > a')


        for index , i in enumerate(links):
            blog = requests.get(i['href'])
            soup = BeautifulSoup(blog.text, "html.parser")

            contenttags = soup.select("div.inside-article > div.entry-content > div:not(.gb-container.gb-container-77275a9a,.ez-toc-v2_0_17.ez-toc-wrap-left.counter-hierarchy, .gb-container.gb-container-b3e80905)")

            txt = ''
            images = []
            for tag in contenttags:
                txt += tag.text
                if tag.find("img"):        
                    images.append(tag.find("img")['data-pin-media'])

            try:
                header_img = i.img['nitro-lazy-src']
            except:
                header_img = 'null'

            data[str(docid)] = {
                'title' : i['title'],
                'header_img' : header_img,
                'text' : txt,
                "images" : images,
                'link' : i['href']
            }
            docid += 1
            theplanetd.append(data)

    return theplanetd