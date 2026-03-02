from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BTN = (By.XPATH, "//button[text()='Add to cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    def sort_by(self, value):
        self.driver.find_element(*self.SORT_DROPDOWN).send_keys(value)

    def add_first_product(self):
        self.driver.find_elements(*self.ADD_TO_CART_BTN)[0].click()

    def get_cart_count(self):
        return self.get_text(*self.CART_BADGE)

    def logout(self):
        self.click(*self.MENU_BTN)
        self.click(*self.LOGOUT_LINK)
