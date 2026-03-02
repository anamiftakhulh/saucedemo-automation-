from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def click(self, by, locator):
        self.driver.find_element(by, locator).click()

    def type(self, by, locator, text):
        self.driver.find_element(by, locator).clear()
        self.driver.find_element(by, locator).send_keys(text)

    def get_text(self, by, locator):
        return self.driver.find_element(by, locator).text

    def is_visible(self, by, locator):
        return self.driver.find_element(by, locator).is_displayed()
