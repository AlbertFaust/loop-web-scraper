#!/usr/bin/env python3                                                                                                                                        
from bs4 import BeautifulSoup
from urllib.request import urlopen
url="http://github.com/AlbertFaust?tab=repositories"

def recursiveURL(url,depth):
    print(url)
    if depth == 5 or url is None:
        return url
    else:
        page=urlopen(url)
        soup=BeautifulSoup(page.read())
        new = soup.find('a')
        if len(new) == 0:
            return url
        else:
            return url, recursiveURL(new, depth+1)
def links(url):
    page=urlopen(url)
    soup=BeautifulSoup(page.read())
    link=soup.find_all('a')
    for i in link:
        link.append(recursiveURL(i,0))
        return link

recursiveURL(url,1)
print(links(url))
