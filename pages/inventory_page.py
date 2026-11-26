from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait, Select


class InventoryPage:

    # Locators
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    PRODUCT_ITEMS = (By.CLASS_NAME, "inventory_item")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_DESCRIPTIONS = (By.CLASS_NAME, "inventory_item_desc")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def click_menu(self):
        self.driver.find_element(*self.MENU_BUTTON).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOGOUT_BUTTON)
        )

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        ).click()

    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))

    def get_product_names(self):
        products = self.driver.find_elements(*self.PRODUCT_NAMES)

        return [product.text for product in products]

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)

        return [price.text for price in prices]

    def get_product_descriptions(self):
        descriptions = self.driver.find_elements(
            *self.PRODUCT_DESCRIPTIONS
    )

        return [description.text for description in descriptions]

    def select_sort_option(self, option_value):
        dropdown = self.driver.find_element(*self.SORT_DROPDOWN)
        Select(dropdown).select_by_value(option_value)

    def get_product_count(self):
        products = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located(self.PRODUCT_ITEMS)
    )
        return len(products)

    def add_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def remove_product_from_cart(self):
        self.driver.find_element(*self.REMOVE_BUTTON).click()

    def click_cart(self):
        self.driver.find_element(*self.CART_ICON).click()