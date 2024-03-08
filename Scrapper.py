import sys
import requests
from urllib import *
from urllib.parse import urljoin

from bs4 import BeautifulSoup


visited_url = set()

def spider_urls(url, keyword):
    try:
        response = requests.get(url)
    except:
        print(f"Request Failed {url}. ")
        return
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        a_tag = soup.find_all('a') # Find all <a>
        urls = []
        for tag in a_tag:
            href = tag.get("href")

            if href is not None and href != "":
                urls.append(href)
            #print(urls)
        for new_urls in urls: #Recursive scrapping -> scrape the collected urls 
            if new_urls not in visited_url:
                visited_url.add(url)
                url_join = urljoin(url, new_urls)
                if keyword in url_join:
                    print(url_join)
                    spider_urls(url_join, keyword)
            else:
                pass





url = input(f"input url you want to scrap:  ")
keyword = input(f"input the keyword you want to search for in a url:  ")

spider_urls(url, keyword)
