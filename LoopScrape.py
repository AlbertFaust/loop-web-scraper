import mechanize                                                                                                                                                
import cookielib
from bs4 import BeautifulSoup
import urllib2

br = mechanize.Browser()
br.set_handle_robots(False)
cj = cookielib.CookieJar()
br.set_cookiejar(cj)
sign_in=br.open("http://loop.dcu.ie/login/index.php")
br.select_form(nr=0)
br.form["username"] = "USERNAME"
br.form["password"] = "PASSWORD"
br.submit()
url=br.open("https://loop.dcu.ie/my/").read()
page=urllib2.urlopen(url)
soup=BeautifulSoup(page.read())
for links in soup.find_all('a'):
    if (links.get('href')).startswith('http') and (links.get('href')) != '#':
        print(links.get('href'))
        page=urllib2.urlopen(links.get('href'))
        soup=BeautifulSoup(page.read())
        for links in soup.find_all('a'):
            print(links.get('href'))
    else:
        print('http://loop.dcu.ie'+links.get('href'))
