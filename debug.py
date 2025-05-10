import requests
from bs4 import BeautifulSoup

def scrape_data(self, pages=4):
    data = []

    for p in range(1, pages + 1):
        url = f"{self.base_url}?page={p}"
        print(f"Fetching: {url}")
        response = requests.get(url, headers=self.headers)
        print(f"Status code: {response.status_code}")
        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, 'lxml')
        products = soup.find_all('li', class_='sProduct')
        print(f"Page {p}: Found {len(products)} products")

        for product in products:
            img_tag = product.find('img', class_='photo')
            img_alt = img_tag.get('alt', 'N/A') if img_tag else 'N/A'

            price_tag = product.find('div', class_='price')
            price = price_tag.get_text(strip=True) if price_tag else 'N/A'

            text_block = product.get_text(" ", strip=True)
            size_match = re.findall(self.pattern, text_block)
            screen_size_cm = size_match[0] if size_match else 'N/A'

            price_val = self._parse_price(price)
            size_val = self._parse_screen_size(screen_size_cm)

            data.append({
                'product_name': img_alt,
                'price': price_val,
                'screen_size': size_val
            })

    print(f"Total scraped: {len(data)} items")
    return data