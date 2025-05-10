import requests
from bs4 import BeautifulSoup
import csv
import re
import pandas as pd
import time

data = []

for p in range(1, 5):
    url = f'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html?page={p}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('div', class_='product-info')

    for product in products:
        # Get product title and image alt
        img_tag = product.find('img')
        img_alt = img_tag['alt'].strip() if img_tag and 'alt' in img_tag.attrs else 'No alt text'

        # Get price
        price_tag = product.find('span', class_='price')
        price = price_tag.text.strip() if price_tag else 'No price'

        # Try to extract screen size from alt or title using regex (e.g., "15.6")
        screen_match = re.search(r'(\d{2}\.\d)"?', img_alt)
        screen_size = screen_match.group(1) if screen_match else 'Unknown'

        data.append({
            'Image Alt': img_alt,
            'Price': price,
            'Screen Size (inches)': screen_size
        })

    time.sleep(3)  # respectful scraping

# Save to CSV using pandas
df = pd.DataFrame(data)
df.to_csv('lenovo.csv', index=False)
print("Saved data to lenovo_laptops.csv")