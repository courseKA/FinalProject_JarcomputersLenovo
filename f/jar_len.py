
import requests
from bs4 import BeautifulSoup as bs
import re
#from urllib.parse import urljoin
#from concurrent.futures import ThreadPoolExecutor
import pandas as pd

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
        print(m)
        # if m:
        #     screen_size = m.groups(1)
       


url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'
r = requests.get(url)
r.text
soup = bs(r.text, 'lxml')
z = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
x = soup.find('span', class_='long_title description').find('a', class_='plttl').text
# y = soup.find('a', class_='plttl')

ret = soup.find('div', class_='s1')
print(ret)

# get name
name = soup.find('a', class_='plttl').text
#print(name)

# get url
awer = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
lenovo_link = soup.find_all(href=re.compile('lenovo'))
# print(lenovo_link)

# get price
price = soup.find('div', class_='price').text
#print(price)

#  Print all laptop names
laptop_names = soup.find_all( href = re.compile('lenovo'))
#for laptop_name in laptop_names:
    #print(laptop_name.text.strip())

# Print all laptop prices
#laptop_prices = soup.select('.price')
#for laptop_price in laptop_prices:
    #print(laptop_price.text.strip())

data.append([laptop_names, laptop_prices])
heather = ['laptop_names', 'laptop_prices']
df = pd.DataFrame(data, columns=heather)
df.to_csv(r"C:\Users\ksa\our_spider\jarcom1\jarcom1\jar.csv", sep=':', encoding='utf-8')


if __name__ == 'main':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'