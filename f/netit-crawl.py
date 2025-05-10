import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from concurrent.futures import ThreadPoolExecutor

class WebCrawler:
    def __init__(self, start_url, depth=1, max_threads=5):
        self.start_url = start_url
        self.depth = depth
        self.max_threads = max_threads
        self.visited = set()

    def get_html(self, url):
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f'Request exception: {e}')

        return None

    def fetch_links(self, url):
        """Fetch all links from a given URL."""
        links = []
        html = self.get_html(url)

        if html:
            # Create a BeautifulSoup object to parse the HTML content
            soup = BeautifulSoup(html, 'html.parser')

            # Find all 'a' (anchor) tags in the HTML that have an href attribute
            for link in soup.find_all('a', href=True):
                # Construct the full URL by combining the base URL with the relative link, extracted from a tag
                full_url = urljoin(url, link['href'])
                if full_url not in self.visited:
                    links.append(full_url)

        return links


    def crawl(self):
        """Crawl URLs up to the specified depth using threading."""
        urls_to_visit = [self.start_url]
        for _ in range(self.depth):
            new_urls = set()

            # Create a ThreadPoolExecutor to manage concurrent requests
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                # Use `executor.map` to apply `fetch_links` concurrently to each URL in `urls_to_visit`
                # This returns an iterable (`results`) containing the links found for each URL
                results = executor.map(self.fetch_links, urls_to_visit)

                for links in results:
                    for link in links:
                        if link not in self.visited:
                            self.visited.add(link)
                            new_urls.add(link)
            urls_to_visit = list(new_urls)


if __name__ == '__main__':
    # Instantiate and run the crawler
    crawler = WebCrawler("https://books.toscrape.com/", depth=1, max_threads=10)
    crawler.crawl()
    print("\nFound URLs:")
    print("\n".join(crawler.visited))