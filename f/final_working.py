import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

data = []

headers = {
    'User-Agent': 'Mozilla/5.0'
}

pattern = r'\b\d+(?:\.\d+)?\s*cm\b'  # matches screen size in cm like "39.6 cm"

for p in range(1, 5):
    url = f'https://www.jarcomputers.com/lenovo/laptopi-cat-2.html?page={p}'
    response = requests.get(url, headers=headers)
    time.sleep(2)
    soup = BeautifulSoup(response.text, 'lxml')

    products = soup.find_all('li', class_='sProduct')

    for product in products:
        # Product name from image alt
        img_tag = product.find('img', class_='photo')
        img_alt = img_tag.get('alt', 'N/A') if img_tag else 'N/A'

        # Price
        price_tag = product.find('div', class_='price')
        price = price_tag.get_text(strip=True) if price_tag else 'N/A'

        # Extract screen size in cm from price or nearby text
        text_block = product.get_text(" ", strip=True)
        size_match = re.findall(pattern, text_block)
        screen_size_cm = size_match[0] if size_match else 'N/A'

        data.append({
            'Product Name': img_alt,
            'Price': price,
            'Screen Size': screen_size_cm
        })

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('jar_lenovo_laptops.csv', index=False, encoding='utf-8-sig')

print("✅ Done! Data saved with screen size in cm.")