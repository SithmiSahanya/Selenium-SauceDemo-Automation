import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#TC_AUTO_000
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    # Selenium Manager automatically manages ChromeDriver
    browser = webdriver.Chrome(options=options)

    yield browser

    # Close the browser after the test finishes
    browser.quit()