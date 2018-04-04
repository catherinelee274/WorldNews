#scraper for China
from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

url = 'http://www.chinadaily.com.cn/china/governmentandpolicy.html'
html = urlopen(url)

soup = BeautifulSoup(html, "html5lib")
table = soup.find('div', attrs = {'class': 'main_art'}) #all breaking stories are under <div>

print(table)
row_info = []
for row in table.findAll('div'):
    print(row.text)



 

