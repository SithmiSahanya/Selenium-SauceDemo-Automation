from config import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


# TC_AUTO_009: Verify products are displayed
def test_products_are_displayed(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    product_count = inventory_page.get_product_count()

    assert product_count == 6

    print(f"Total products displayed: {product_count}")

# TC_AUTO_010: Verify product names are displayed
def test_product_names_are_displayed(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    product_names = inventory_page.get_product_names()

    assert len(product_names) == 6

    assert all(name.strip() for name in product_names)

    print("Product names:", product_names)

# TC_AUTO_011: Verify product prices are displayed
def test_product_prices_are_displayed(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    product_prices = inventory_page.get_product_prices()

    assert len(product_prices) == 6

    for price in product_prices:
        assert price.startswith("$")
        assert float(price.replace("$", "")) > 0

    print("Product prices:", product_prices)

# TC_AUTO_012: Verify product descriptions are displayed
def test_product_descriptions_are_displayed(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    product_descriptions = inventory_page.get_product_descriptions()

    assert len(product_descriptions) == 6

    assert all(description.strip() for description in product_descriptions)

    print("Product descriptions:", product_descriptions)

# TC_AUTO_013: Verify products are sorted by Name (A to Z)
def test_sort_products_by_name_az(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.select_sort_option("az")

    product_names = inventory_page.get_product_names()

    assert product_names == sorted(product_names)

    print("Products sorted A to Z:", product_names)

# TC_AUTO_014: Verify products are sorted by Price (Low to High)
def test_sort_products_by_price_low_to_high(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.select_sort_option("lohi")

    product_prices = inventory_page.get_product_prices()

    numeric_prices = [
        float(price.replace("$", ""))
        for price in product_prices
    ]

    assert numeric_prices == sorted(numeric_prices)

    print("Products sorted by price (Low to High):", product_prices)

# TC_AUTO_015: Verify products are sorted by Price (High to Low)
def test_sort_products_by_price_high_to_low(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.select_sort_option("hilo")

    product_prices = inventory_page.get_product_prices()

    numeric_prices = [
        float(price.replace("$", ""))
        for price in product_prices
    ]

    assert numeric_prices == sorted(numeric_prices, reverse=True)

    print("Products sorted by price (High to Low):", product_prices)

# TC_AUTO_016: Verify that a product can be added to the cart
def test_add_product_to_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()

    cart_badge = driver.find_element(
        By.CLASS_NAME, "shopping_cart_badge"
    ).text

    assert cart_badge == "1"

    print("Product successfully added to cart!")

# TC_AUTO_017: Verify that a product can be removed from the cart
def test_remove_product_from_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    # Add product to cart
    inventory_page.add_product_to_cart()

    # Remove product from cart
    inventory_page.remove_product_from_cart()

    # Verify cart badge is no longer displayed
    cart_badges = driver.find_elements(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert len(cart_badges) == 0

    print("Product successfully removed from cart!")

