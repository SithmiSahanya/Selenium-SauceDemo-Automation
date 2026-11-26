
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from conftest import driver


class CartPage:

    # Locators
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            10,
            ignored_exceptions=(StaleElementReferenceException,)
    )

    def get_cart_product_names(self):

        def get_names(driver):
            products = driver.find_elements(*self.CART_ITEM_NAMES)
            return ([product.text for product in products],)

        return self.wait.until(get_names)[0]


    def get_cart_product_prices(self):
        self.wait.until(
            EC.presence_of_element_located(self.CART_ITEM_PRICES)
        )

        prices = self.driver.find_elements(*self.CART_ITEM_PRICES)
        return [price.text for price in prices]

    def remove_product(self):

        def click_remove_button(driver):
            try:
                driver.find_element(*self.REMOVE_BUTTON).click()
                return True
            except StaleElementReferenceException:
                return False

        self.wait.until(click_remove_button)

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
