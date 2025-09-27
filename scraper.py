import requests
from bs4 import BeautifulSoup
import re
import mysql.connector
from config import db_config
import time


class LaptopScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.pattern = r'\b\d+(?:\.\d+)?\s*cm\b'  # намира размер на екрана в cm

    def scrape_data(self, pages=4):
        """Скрапва модел, цена и размер на екрана от зададения сайт"""
        data = []

        for p in range(1, pages + 1):
            url = f"{self.base_url}?page={p}"
            print(f"Fetching: {url}")

            try:
                response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
                if response.status_code != 200:
                    print(f"Error: {response.status_code}. Skipping page {p}.")
                    continue

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
                    screen_size = (
                        float(size_match[0].replace("cm", "").strip()) if size_match else 0.0
                    )

                    data.append({
                        'model': name,
                        'price': price,
                        'screen_size': screen_size
                    })

                time.sleep(2)  # малка пауза, за да не блокира сайтът

            except Exception as e:
                print(f"Error processing page {p}: {str(e)}")

        print(f"Scraped total: {len(data)} items")
        return data

    def _parse_price(self, price_text):
        """Парсва цената и връща float"""
        matches = re.findall(r'\d+\.\d+', price_text)
        if matches:
            return float(matches[0])
        digits = re.findall(r'\d+', price_text)
        return float(digits[0]) if digits else 0.0

    def save_to_db(self, data):
        """Записва изчистените данни в MySQL"""
        conn = None
        cursor = None
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()

            # Създава таблицата, ако я няма
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS laptops (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    model VARCHAR(255) NOT NULL,
                    price DECIMAL(10,2) NOT NULL,
                    screen_size FLOAT
                )
            """)

            # Изчистваме таблицата преди нови данни
            cursor.execute("TRUNCATE TABLE laptops")

            # Вкарваме данните
            for item in data:
                cursor.execute("""
                    INSERT INTO laptops (model, price, screen_size)
                    VALUES (%s, %s, %s)
                """, (item['model'], item['price'], item['screen_size']))

            conn.commit()
            print(f"Inserted {len(data)} items into database.")

        except Exception as e:
            print(f"Database error: {str(e)}")

        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
            print("Database connection closed.")
