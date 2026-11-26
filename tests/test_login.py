from config import BASE_URL
from config import INVALID_USERNAME, INVALID_PASSWORD
from config import BASE_URL, STANDARD_USER, PASSWORD, LOCKED_OUT_USER
from pages.inventory_page import InventoryPage
from selenium.webdriver.support.ui import WebDriverWait


# TC_AUTO_001: Verify that the SauceDemo website opens successfully
def test_open_saucedemo(driver):
    driver.get(BASE_URL)

    assert driver.current_url == BASE_URL

    print("SauceDemo website opened successfully!")


from config import BASE_URL, STANDARD_USER, PASSWORD
from pages.login_page import LoginPage

# TC_AUTO_002: Verify login with valid credentials
def test_open_saucedemo(driver):
    driver.get(BASE_URL)

    assert driver.current_url == BASE_URL

    print("SauceDemo website opened successfully!")

def test_valid_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    assert "inventory.html" in driver.current_url

    print("Login successful!")


# TC_AUTO_003: Verify login with invalid credentials
def test_invalid_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)

    actual_error = login_page.get_error_message()

    expected_error = "Epic sadface: Username and password do not match any user in this service"

    assert actual_error == expected_error

    print("Invalid login error message verified successfully!")

# TC_AUTO_004: Verify login with empty username and password
def test_empty_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.click_login()

    actual_error = login_page.get_error_message()

    expected_error = "Epic sadface: Username is required"

    assert actual_error == expected_error

    print("Empty login validation verified successfully!")

# TC_AUTO_005: Verify login with empty username and valid password
def test_empty_username(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_password(PASSWORD)

    login_page.click_login()

    actual_error = login_page.get_error_message()

    expected_error = "Epic sadface: Username is required"

    assert actual_error == expected_error

    print("Empty username validation verified successfully!")

# TC_AUTO_006: Verify login with valid username and empty password
def test_empty_password(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.enter_username(STANDARD_USER)

    login_page.click_login()

    actual_error = login_page.get_error_message()

    expected_error = "Epic sadface: Password is required"

    assert actual_error == expected_error

    print("Empty password validation verified successfully!")

# TC_AUTO_007: Verify login with locked-out user
def test_locked_out_user_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(LOCKED_OUT_USER, PASSWORD)

    actual_error = login_page.get_error_message()

    expected_error = "Epic sadface: Sorry, this user has been locked out."

    assert actual_error == expected_error

    print("Locked-out user validation verified successfully!")

# TC_AUTO_008: Verify successful logout
def test_successful_logout(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)

    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)

    inventory_page.click_menu()

    inventory_page.click_logout()

    WebDriverWait(driver, 10).until(
        lambda driver: driver.current_url == BASE_URL
    )

    assert driver.current_url == BASE_URL

    print("Logout successful!")