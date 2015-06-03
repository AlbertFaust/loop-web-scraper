#! /usr/bin/bash python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
url='http://github.com/AlbertFaust?tab=repositories'
page=urlopen(url)
soup=BeautifulSoup(page.read())
for links in soup.find_all('a'):
    if (links.get('href')).startswith('http') and (links.get('href')) != '#':
        print(links.get('href'))                                                                                                                                
        page=urlopen(links.get('href'))
        soup=BeautifulSoup(page.read())
        for links in soup.find_all('a'):
            print(links.get('href'))
    else:
        print('http://github.com'+links.get('href'))
