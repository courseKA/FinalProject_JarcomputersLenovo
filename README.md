FinalProject_JarcomputersLenovo
This project is a Python-based application designed to scrape and display laptop specifications from the Lenovo website. It features a graphical user interface (GUI) built with PyQt5 
and utilizes MySQL for data storage.

Table of Contents

Project Overview

Features

Installation

Usage

Project Structure

Technologies Used

License

Project Overview

The application allows users to browse and filter Lenovo laptop specifications. It scrapes data from Lenovo's official website and stores it in a MySQL database.
The GUI provides an intuitive interface for users to interact with the data.

Features

Web Scraping: Extracts laptop specifications from Lenovo's official website.

GUI Interface: Built with PyQt5 for a user-friendly experience.

MySQL Database: Stores laptop data for efficient querying and management.

Data Filtering: Allows users to filter laptops based on various specifications.

Installation

To set up the project locally, follow these steps:

Clone the repository:
git clone https://github.com/courseKA/FinalProject_JarcomputersLenovo.git
cd FinalProject_JarcomputersLenovo

Set up the MySQL database:
Create a database called laptop_data:

CREATE DATABASE laptop_data;
(Optional) Create required tables manually or run provided SQL schema if included.

Configure database connection:
Update your MySQL credentials in config.py:

db_config = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'laptop_data'
}
Install required Python packages:

pip install PyQt5 mysql-connector-python beautifulsoup4 requests

Usage

To run the application:
python main.py
This will launch the GUI, allowing you to interact with the application.

Project Structure

FinalProject_JarcomputersLenovo/
├── main.py            # Entry point of the application
├── gui.py             # Contains the GUI layout and logic
├── scraper.py         # Web scraping logic
├── config.py          # Configuration settings
├── laptop_data.sql    # MySQL database schema
└── requirements.txt   # List of required Python packages

Technologies Used

Python: Programming language used for the application.

PyQt5: Framework for building the GUI.

MySQL: Relational database management system for data storage.

Requests: HTTP library for making requests to web pages.

BeautifulSoup: Library for parsing HTML and XML documents.

License
This project is licensed under the MIT License - see the LICENSE file for details.
