
CREATE DATABASE IF NOT EXISTS laptop_data;

USE laptop_data;

CREATE TABLE IF NOT EXISTS lenovo_laptops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255),
    price VARCHAR(50),
    screen_size VARCHAR(20)
);