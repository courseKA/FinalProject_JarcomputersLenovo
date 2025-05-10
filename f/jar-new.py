import requests
from bs4 import BeautifulSoup as bs
import re
import csv
import pandas as pd

data=[]

url = 'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html?page=1'
r = requests.get(url)
r.text
soup = bs(r.text, 'lxml')

x = soup.find('span', class_='long_title description').find('a', class_='plttl').get('href')
#print(x)

laptop_name = soup.find('a', class_='plttl').text

#print(len(laptop_name))
    #print(laptop_name.text.strip())
laptop_price = soup.find('div', class_='price').text
#print(laptop_price)
ret = soup.find('div', class_='s1').text

#price = soup.find('div', class_='s1').text
#print(price)
#price = soup.find('div', class_='price').text

pattern = r'\b\d+(?:\.\d+)?\s*cm\b'
matches = re.findall(pattern, laptop_name)

data.append([laptop_name, laptop_price, matches])

df = pd.DataFrame(data )
df.to_csv('jar.csv', index=False, encoding='utf-8-sig')
