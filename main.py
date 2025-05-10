from scraper import LaptopScraper
from gui import CustomerViewer
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    url = "https://www.jarcomputers.com/lenovo/laptopi-cat-2.html"
    scraper = LaptopScraper(url)
    data = scraper.scrape_data()
    scraper.save_to_db(data)

    app = QApplication(sys.argv)
    viewer = CustomerViewer()
    viewer.show()
    sys.exit(app.exec_())
