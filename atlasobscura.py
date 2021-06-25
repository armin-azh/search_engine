import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json

def atlasobscura_crawler( ):
    atlasobscura = []
    docid = 1
    for i in tqdm(range (1 , 10)):
        data = {}

        page = requests.get(f"https://www.atlasobscura.com/places?page={i}&sort=likes_count")
        soup = BeautifulSoup(page.text, 'html.parser')

        posts = soup.select("#page-content > div > div > div > div > div")

        for i in posts:
            title = i.find('h3').text
            header_img = i.find('img')['data-src']
            link = 'https://www.atlasobscura.com/' + i.find('a')["href"]

            page = requests.get(link)
            soup = BeautifulSoup(page.text, 'html.parser')

            images_path = soup.select("#page-content > article > header > div > div.DDPage__item-gallery-container.item-gallery-container.hidden-print > div > figure > a")
            images = []
            for k in images_path:
                images.append(k["data-lightbox-src"])

            txt =''
            text_path = soup.select("#place-body")
            for tag in text_path:
                txt += tag.text

            data[str(docid)] = {
            'title' : title,
            'header_img' : header_img,
            'text' : txt,
            "images" : images,
            'link' : link
            }
            docid += 1
            atlasobscura.append(data)
        
    return atlasobscura
