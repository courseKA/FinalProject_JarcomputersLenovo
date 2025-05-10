from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QApplication
)
import mysql.connector
from config import db_config


class CustomerViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Laptop Viewer")
        self.resize(800, 600)
        layout = QVBoxLayout()

        # Filter area
        filter_layout = QHBoxLayout()
        self.price_input = QLineEdit()
        self.screen_input = QLineEdit()
        self.filter_btn = QPushButton("Filter")
        self.filter_btn.clicked.connect(self.load_data)

        filter_layout.addWidget(QLabel("Max Price:"))
        filter_layout.addWidget(self.price_input)
        filter_layout.addWidget(QLabel("Min Screen Size:"))
        filter_layout.addWidget(self.screen_input)
        filter_layout.addWidget(self.filter_btn)

        layout.addLayout(filter_layout)

        # Table area
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Product Name", "Price", "Screen Size"])
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.load_data()

    def load_data(self):
        max_price = self.price_input.text()
        min_screen = self.screen_input.text()

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = "SELECT product_name, price, screen_size FROM customers WHERE 1=1"
        params = []

        if max_price:
            query += " AND price <= %s"
            params.append(float(max_price))
        if min_screen:
            query += " AND screen_size >= %s"
            params.append(float(min_screen))

        cursor.execute(query, params)
        rows = cursor.fetchall()

        self.table.setRowCount(len(rows))
        for row_idx, row in enumerate(rows):
            for col_idx, value in enumerate(row):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        cursor.close()
        conn.close()
