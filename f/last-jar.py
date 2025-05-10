import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import re

# Data containers
all_names = []
all_prices = []
all_sizes = []

# Loop through 5 pages
for page in range(1, 6):
    url = f'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html?page={page}'
    r = requests.get(url)
    soup = bs(r.text, 'lxml')

    # Get all products
    products = soup.find('ol', id = 'product_list', class_='p1').text
    print(products)

    for product in products:
        # Laptop name
        #name = soup.find_all( href = re.compile('lenovo'))
        name = soup.find('a', class_='plttl').text
        
        # Price
        price = soup.find('div', class_='price').text

        # Screen size (like 15.6, 14, etc.)
        pattern = r'\b\d+(?:\.\d+)?\s*cm\b'
        size = re.findall(pattern, name)

        # Save data
        all_names.append(name)
        all_prices.append(price)
        all_sizes.append(size)

# Save to CSV
df = pd.DataFrame({
    'Laptop Name': all_names,
    'Price': all_prices,
    'Display Size': all_sizes
})

df.to_csv('lenovo.csv',index=False, encoding='utf-8-sig')
print("Scraping complete! Data saved to 'lenovo_laptops_all_pages.csv'.")