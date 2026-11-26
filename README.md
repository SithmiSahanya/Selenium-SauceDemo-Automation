# SauceDemo Selenium Automation Testing

## Project Overview

This project focuses on automating the functional testing of the SauceDemo e-commerce website using Python, Selenium WebDriver, and Pytest.

The project follows the **Page Object Model (POM)** design pattern to improve code organization, readability, and maintainability.

## Website Under Test

https://www.saucedemo.com/

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Google Chrome
- Git and GitHub


## Project Structure

```text
Selenium-SauceDemo-Automation/
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_inventory.py
│   └── test_cart.py
│
├── config.py
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Test Coverage

A total of **27 automated test cases** have been implemented.

| Test Module | Number of Test Cases |
|---|---:|
| Login Testing | 8 |
| Inventory Testing | 9 |
| Shopping Cart and Checkout Testing | 10 |
| **Total** | **27** |

### Main Testing Scenarios

- Verify successful login and logout
- Verify invalid login credentials
- Verify locked-out user login
- Verify product details
- Verify product sorting
- Verify adding and removing products from cart
- Verify shopping cart functionality
- Verify checkout form validation
- Verify successful order placement

## Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate to the project folder:

```bash
cd Selenium-SauceDemo-Automation
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment (Windows):

```bash
venv\Scripts\activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Execute Automated Tests

Run all test cases:

```bash
python -m pytest -v
```

## Generate HTML Test Report

```bash
python -m pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to view the test execution results.

## Test Execution Results

**Latest execution:** 27 Passed

## Author

QA Automation Testing Portfolio Project
