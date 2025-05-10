import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from config import db_config
import time


class LaptopScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.pattern = r'\b\d+(?:\.\d+)?\s*cm\b'

    def scrape_data(self, pages=4):
        data = []

        for p in range(1, pages + 1):
            url = f"{self.base_url}?page={p}"
            print(f"Fetching: {url}")

            # Use requests to get the page content
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            if response.status_code != 200:
                print(f"Error: {response.status_code}. Skipping page {p}.")
                continue  # Skip the page if it can't be fetched

            soup = BeautifulSoup(response.text, 'lxml')
            products = soup.find_all('li', class_='sProduct')

            print(f"Page {p}: Found {len(products)} products")

            for product in products:
                name_tag = product.find('img', class_='photo')
                name = name_tag.get('alt', 'N/A') if name_tag else 'N/A'

                price_tag = product.find('div', class_='price')
                price = self._parse_price(price_tag.get_text()) if price_tag else 0.0

                text_block = product.get_text(" ", strip=True)
                size_match = re.findall(self.pattern, text_block)
                screen_size = float(size_match[0].replace("cm", "").strip()) if size_match else 0.0

                data.append({
                    'product_name': name,
                    'price': price,
                    'screen_size': screen_size
                })

            time.sleep(2)  # Add delay to avoid hitting the server too hard

        print(f"Scraped total: {len(data)} items")
        return data

    def _parse_price(self, price_str):
        # Extract the price value
        digits = re.sub(r"[^\d.]", "", price_str)
        return float(digits) if digits else 0.0

    def save_to_db(self, data):
        # Save scraped data to MySQL
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_name VARCHAR(255),
                price FLOAT,
                screen_size FLOAT
            )
        """)
        cursor.execute("TRUNCATE TABLE customers")

        for item in data:
            cursor.execute("""
                INSERT INTO customers (product_name, price, screen_size)
                VALUES (%s, %s, %s)
            """, (item['product_name'], item['price'], item['screen_size']))

        conn.commit()
        cursor.close()
        conn.close()
        print(f"Inserted {len(data)} items into database.")