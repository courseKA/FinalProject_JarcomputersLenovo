import sys
import mysql.connector
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QTableWidget,
    QTableWidgetItem, QLineEdit, QPushButton, QLabel, QHBoxLayout
)
from config import db_config


class LaptopViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lenovo Laptop Viewer")
        self.setGeometry(100, 100, 900, 600)

        layout = QVBoxLayout()

        # Филтри
        filter_layout = QHBoxLayout()

        self.price_filter = QLineEdit()
        self.price_filter.setPlaceholderText("Филтър по максимална цена")
        filter_layout.addWidget(QLabel("Цена ≤"))
        filter_layout.addWidget(self.price_filter)

        self.screen_filter = QLineEdit()
        self.screen_filter.setPlaceholderText("Филтър по минимален екран (см)")
        filter_layout.addWidget(QLabel("Екран ≥"))
        filter_layout.addWidget(self.screen_filter)

        self.filter_btn = QPushButton("Приложи филтър")
        self.filter_btn.clicked.connect(self.load_data)
        filter_layout.addWidget(self.filter_btn)

        layout.addLayout(filter_layout)

        # Бутони за сортиране
        sort_layout = QHBoxLayout()
        self.sort_price_btn = QPushButton("Сортирай по цена")
        self.sort_price_btn.clicked.connect(lambda: self.table.sortItems(1))  # колона 1 = цена
        sort_layout.addWidget(self.sort_price_btn)

        self.sort_screen_btn = QPushButton("Сортирай по екран")
        self.sort_screen_btn.clicked.connect(lambda: self.table.sortItems(2))  # колона 2 = екран
        sort_layout.addWidget(self.sort_screen_btn)

        layout.addLayout(sort_layout)

        # Таблица
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Модел", "Цена", "Екран (см)"])
        self.table.setSortingEnabled(True)
        self.table.setColumnWidth(0, 450)   # по-широка колона за модел
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_data()

    def load_data(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # >>> променено от customers на laptops
        query = "SELECT model, price, screen_size FROM laptops WHERE 1=1"
        values = []

        # Филтър по цена
        if self.price_filter.text():
            query += " AND price <= %s"
            values.append(float(self.price_filter.text()))

        # Филтър по екран (каст към число)
        if self.screen_filter.text():
            query += " AND CAST(screen_size AS DECIMAL(10,2)) >= %s"
            values.append(float(self.screen_filter.text()))

        cursor.execute(query, values)
        rows = cursor.fetchall()

        self.table.setRowCount(len(rows))
        for row_idx, row_data in enumerate(rows):
            for col_idx, value in enumerate(row_data):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        cursor.close()
        conn.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = LaptopViewer()
    viewer.show()
    sys.exit(app.exec_())

