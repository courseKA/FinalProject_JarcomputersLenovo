import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
import mysql.connector

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('PyQt MySQL Example')
        self.setGeometry(100, 100, 300, 100)

        self.button = QPushButton('Connect to MySQL', self)
        self.button.clicked.connect(self.connect_to_mysql)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.setLayout(layout)

    def connect_to_mysql(self):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='uUkol87g65tr@W3*h21y',
                database='laptop_data'
            )

            cursor = conn.cursor()
            cursor.execute("SELECT * FROM your_table_name LIMIT 1")
            result = cursor.fetchone()

            QMessageBox.information(self, 'Success', f'Connected! First row: {result}')
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            QMessageBox.critical(self, 'Error', f'Error: {err}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())