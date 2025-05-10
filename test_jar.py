import requests
from bs4 import BeautifulSoup as bs
import re
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import csv

class LaptopsLenovo:
    # constract
    def __init__(self, brand, price, screen_size, depth=1):
        self.brand = brand
        self.price = price
        self.screen_size = screen_size
        self.depth = depth
        self.visited = set()

    def brand(self, text: str) -> str:
        regex = re.compile()
        pass

    def price(self):
        price = soup.find('div', class_='price').text
        pass

    def screen_size(self, text: str) -> float:
        regex = re.compile(r'^\s*([\d.].*+)')
        m = regex.match(text)
        if m:
            screen_size = m.groups(1)
            pass


url = 'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html'
r = requests.get(url)
r.text
soup = bs(r.text, 'lxml')
Link = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
long_title = soup.find('span', class_='long_title description').find('a', class_='plttl').text
#y = soup.find('a', class_='plttl')


# ret = soup.find('div', class_='s1')
# print('ret is', ret)

# get name
l_name = soup.find('a', class_='plttl').text
#print(l_name)

# get url
awer = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
lenovo_link = soup.find_all(href=re.compile('lenovo'))
# print(lenovo_link)

# get price
price = soup.find('div', class_='price').text
#print(price)

#  Print all laptop names
# laptop_names = soup.find_all( href = re.compile('lenovo'))
# for laptop_name in laptop_names:
#     print(laptop_name.text.strip())

# Print all laptop prices
# laptop_prices = soup.select('.price')
# for laptop_price in laptop_prices:
#     print(laptop_price.text.strip())




data=[]
for p in range(1, 5):
    url = f'https://www.jarcomputers.com/lenovo/laptopi-cat-[p].html'

    laptop_prices = soup.select('.price')
    prices = []
    for laptop_price in laptop_prices:
        pr = laptop_price.text.strip()
        prices.append(pr)
    
    #print(prices)
    #print(len(prices))

    laptop_names = soup.find_all( href = re.compile('lenovo'))
    names = []
    for laptop_name in laptop_names:
        if laptop_name not in names:
            names.append(laptop_name)
        
    #print(names)
    #print(len(names))
    #print(laptop_name.text.strip())
        
data.append([names, prices])

heather = ['laptop_names', 'laptop_prices']
df = pd.DataFrame(data, columns=heather)
df.to_csv(r"C:\Users\ksa\our_spider\jarcom1\jarcom1\jar.csv")

if __name__ == 'main':
    url = 'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html'