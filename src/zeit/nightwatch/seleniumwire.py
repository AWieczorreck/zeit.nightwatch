import seleniumwire.webdriver
import selenium.webdriver


class WebDriverChrome(
        seleniumwire.webdriver.Chrome,
        selenium.webdriver.WebDriverChrome):
    opts = seleniumwire.webdriver.ChromeOptions()
