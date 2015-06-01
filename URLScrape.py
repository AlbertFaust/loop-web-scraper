#!/usr/bin/env python3
from bs4 import BeautifulSoup
import urllib2
url="http://github.com/AlbertFaust?tab=repositories"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())
for link in soup.find_all('a'):
	print(link.get('href'))
