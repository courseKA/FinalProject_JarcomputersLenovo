import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
)

import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='uUkol87g65tr@W3*h21y',
        database='laptop_data'
    )

class LaptopApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("💻 Lenovo Laptops - Filter")
        self.setGeometry(100, 100, 700, 500)

        self.layout = QVBoxLayout()

        # Price filter
        self.price_layout = QHBoxLayout()
        self.price_label = QLabel("Max Price:")
        self.price_input = QLineEdit()
        self.price_button = QPushButton("Filter by Price")
        self.price_button.clicked.connect(self.filter_by_price)
        self.price_layout.addWidget(self.price_label)
        self.price_layout.addWidget(self.price_input)
        self.price_layout.addWidget(self.price_button)

        # Screen size filter
        self.screen_layout = QHBoxLayout()
        self.screen_label = QLabel("Screen Size (cm):")
        self.screen_input = QLineEdit()
        self.screen_button = QPushButton("Filter by Screen Size")
        self.screen_button.clicked.connect(self.filter_by_screen)
        self.screen_layout.addWidget(self.screen_label)
        self.screen_layout.addWidget(self.screen_input)
        self.screen_layout.addWidget(self.screen_button)

        # Results box
        self.result_box.setText(output)
        self.result_box.setReadOnly(True)

        # Add everything to main layout
        self.layout.addLayout(self.price_layout)
        self.layout.addLayout(self.screen_layout)
        self.layout.addWidget(self.result_box)
        self.setLayout(self.layout)

    def filter_by_price(self):
        max_price = self.price_input.text().strip()
        if not max_price.replace('.', '', 1).isdigit():
            self.result_box.setText("❌ Please enter a valid number for price.")
            return

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT * FROM lenovo_laptops
            WHERE REPLACE(REPLACE(price, 'лв.', ''), ',', '') REGEXP '^[0-9.]+$'
        """)
        rows = [r for r in cursor.fetchall()
                if float(r['price'].replace('лв.', '').replace(',', '').strip()) <= float(max_price)]

        self.show_results(rows)
        cursor.close()
        conn.close()

    def filter_by_screen(self):
        size = self.screen_input.text().strip()
        if not size.endswith("cm"):
            size += " cm"

        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM lenovo_laptops WHERE screen_size_cm = %s", (size,))
        rows = cursor.fetchall()

        self.show_results(rows)
        cursor.close()
        conn.close()

    def show_results(self, rows):
        if not rows:
            self.result_box.setText("❌ No matching laptops found.")
            return

        output = ""
        for row in rows:
            output += f"{row['product_name']} | {row['price']} | {row['screen_size_cm']}\n"
            self.result_box.setText(output)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    window = LaptopApp()
    window.show()
    sys.exit(app.exec_())