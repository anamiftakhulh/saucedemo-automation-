from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)

    def is_login_page_displayed(self):
        return self.is_visible(*self.USERNAME)

    def is_visible(self, by, locator):
        return self.driver.find_element(by, locator).is_displayed()
