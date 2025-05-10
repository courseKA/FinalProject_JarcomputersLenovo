import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
import re

#data = []
# URL of the page to scrape
url = 'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html?page=1'

# Send a request to the page
r = requests.get(url)
soup = bs(r.text, 'lxml')

# Find all product name elements
products = soup.find_all('li', class_='sProduct')
print(type(products))
print(len(products))

# Extract the text (product name) from each product

names = [product.text.strip() for product in products]
# Print all names



prices = [product.text.strip() for product in products]
# Print all prices


for product in products:
    pattern = r'\b\d+(?:\.\d+)?\s*cm\b'
    sizes = re.findall(pattern, names)


#data.append([names,prices,sizes])
# Save to CSV (optional)
df = pd.DataFrame([names,prices,sizes])
df.to_csv('lenovo_laptops.csv',index=False, encoding='utf-8-sig' )

# data.append([name, price, matches])
# print(data)
# df = pd.DataFrame(name)
# df.to_csv('jar.csv')