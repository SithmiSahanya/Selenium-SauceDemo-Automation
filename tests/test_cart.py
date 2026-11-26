from config import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from selenium.webdriver.common.by import By

# TC_AUTO_018: Verify shopping cart page opens successfully
def test_shopping_cart_page_opens(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    assert "cart.html" in driver.current_url

    print("Shopping cart page opened successfully!")

# TC_AUTO_019: Verify product details in the shopping cart
def test_cart_product_details(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)

    product_names = cart_page.get_cart_product_names()
    product_prices = cart_page.get_cart_product_prices()

    assert "Sauce Labs Backpack" in product_names
    assert "$29.99" in product_prices

    print("Cart product names:", product_names)
    print("Cart product prices:", product_prices)

# TC_AUTO_020: Verify product can be removed from the cart
def test_remove_product_from_cart(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.remove_product()

    product_names = cart_page.get_cart_product_names()

    assert len(product_names) == 0

    print("Product successfully removed from cart!")


# TC_AUTO_021: Verify checkout button navigates to checkout information page
def test_checkout_button_navigation(driver):
    driver.get(BASE_URL)

    # Login to SauceDemo
    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    # Add a product to the cart
    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    # Click checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Verify navigation to checkout information page
    assert "checkout-step-one.html" in driver.current_url

    print("Successfully navigated to checkout information page!")


# TC_AUTO_022: Verify checkout with empty customer information
def test_checkout_with_empty_information(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Click Continue without entering customer information
    driver.find_element(By.ID, "continue").click()

    # Verify the validation error message
    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "First Name is required" in error_message

    print("Checkout validation message:", error_message)


# TC_AUTO_023: Verify checkout with missing Last Name
def test_checkout_with_missing_last_name(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter First Name only
    driver.find_element(By.ID, "first-name").send_keys("Sithmi")

    # Click Continue
    driver.find_element(By.ID, "continue").click()

    # Get validation error
    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "Last Name is required" in error_message

    print("Checkout validation message:", error_message)


# TC_AUTO_024: Verify checkout with missing Postal Code
def test_checkout_with_missing_postal_code(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter First Name and Last Name
    driver.find_element(By.ID, "first-name").send_keys("Sithmi")
    driver.find_element(By.ID, "last-name").send_keys("Sahanya")

    # Leave Postal Code empty and click Continue
    driver.find_element(By.ID, "continue").click()

    # Verify validation error
    error_message = driver.find_element(
        By.CSS_SELECTOR, "[data-test='error']"
    ).text

    assert "Postal Code is required" in error_message

    print("Checkout validation message:", error_message)


# TC_AUTO_025: Verify successful checkout
def test_successful_checkout(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter valid customer information
    driver.find_element(By.ID, "first-name").send_keys("Sithmi")
    driver.find_element(By.ID, "last-name").send_keys("Sahanya")
    driver.find_element(By.ID, "postal-code").send_keys("10350")

    # Continue to checkout overview
    driver.find_element(By.ID, "continue").click()

    # Verify checkout overview page
    assert "checkout-step-two.html" in driver.current_url

    print("Successfully navigated to checkout overview page!")


# TC_AUTO_026: Verify successful order placement
def test_successful_order_placement(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter customer information
    driver.find_element(By.ID, "first-name").send_keys("Sithmi")
    driver.find_element(By.ID, "last-name").send_keys("Sahanya")
    driver.find_element(By.ID, "postal-code").send_keys("10350")

    # Continue to checkout overview
    driver.find_element(By.ID, "continue").click()

    # Click Finish to place the order
    driver.find_element(By.ID, "finish").click()

    # Verify successful order confirmation
    confirmation_message = driver.find_element(
        By.CLASS_NAME, "complete-header"
    ).text

    assert confirmation_message == "Thank you for your order!"

    print("Order confirmation:", confirmation_message)


# TC_AUTO_027: Verify cart is empty after successful order placement
def test_cart_is_empty_after_order_placement(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # Enter customer information
    driver.find_element(By.ID, "first-name").send_keys("Sithmi")
    driver.find_element(By.ID, "last-name").send_keys("Sahanya")
    driver.find_element(By.ID, "postal-code").send_keys("10350")

    # Continue and finish checkout
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()

    # Return to inventory page
    driver.find_element(By.ID, "back-to-products").click()

    # Verify cart badge is not displayed
    cart_badges = driver.find_elements(
        By.CLASS_NAME, "shopping_cart_badge"
    )

    assert len(cart_badges) == 0

    print("Shopping cart is empty after successful order!")
