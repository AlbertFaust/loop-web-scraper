#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
url="http://github.com/AlbertFaust?tab=repositories"
page=urlopen(url)
soup = BeautifulSoup(page.read())
for link in soup.find_all('a'):
	print(link.get('href'))
