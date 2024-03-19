# Acme Product Management System
 This project implements a Python-based product management system for Acme Corporation. It includes classes for modeling various products, generating random products, and generating inventory reports. The project emphasizes object-oriented programming, code style adherence, and unit testing.

## Introduction:
Welcome to the Acme Product Management System! This project is designed to help organize and manage the vast inventory of products sold by Acme Corporation. With this system, you can model different types of products, generate random products for inventory, and generate reports summarizing the inventory.

## Requirements:
To run this project, you need Python installed on your system. Additionally, ensure that you have the following modules available:

pytest
random (from the Python standard library)
Installation:
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/acme-product-management.git
Navigate to the project directory:
bash
Copy code
cd acme-product-management
Usage:
acme.py: This file contains the Product and BoxingGlove classes for modeling products sold by Acme Corporation. It also includes methods for calculating stealability, explosion risk, and specific functionality for boxing gloves.

acme_report.py: Use this module to generate random products and generate inventory reports based on the generated products. It includes functions generate_products(num_products) and inventory_report(product_list).

acme_test.py: This file contains unit tests for the Product class. Ensure that the Product class functions correctly by running the tests provided in this file.

Running Tests:
To run the unit tests for the Product class, execute the following command:

Copy code
pytest acme_test.py
Contributing:
If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.
