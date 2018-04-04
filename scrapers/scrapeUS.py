#US scraper

from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = 'http://hosted.ap.org/dynamic/fronts/POLITICS?SITE=KSNEW&SECTION=HOME'
html = urlopen(url)

soup = BeautifulSoup(html, "html5lib")
table = soup.find('tr', attrs = {'class': 'ap-topheadline-tr'}) 

#print(table)
row_info = []
for row in table.findAll('p'):
    print(row.text)



 

