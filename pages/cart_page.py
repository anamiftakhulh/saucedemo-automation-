from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):

    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    REMOVE_BTN = (By.XPATH, "//button[text()='Remove']")
    CHECKOUT_BTN = (By.ID, "checkout")

    def open_cart(self):
        self.click(*self.CART_ICON)

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_first_item(self):
        self.driver.find_elements(*self.REMOVE_BTN)[0].click()

    def click_checkout(self):
        self.click(*self.CHECKOUT_BTN)
