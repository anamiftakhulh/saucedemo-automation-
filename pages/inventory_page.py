from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ADD_TO_CART_BTNS = (By.XPATH, "//button[text()='Add to cart']")
    REMOVE_BTNS = (By.XPATH, "//button[text()='Remove']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    MENU_BTN = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")

    # ---------- SORTING ----------

    def sort_by_visible_text(self, text):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(text)

    def get_product_names(self):
        elements = self.driver.find_elements(*self.PRODUCT_NAMES)
        return [el.text for el in elements]

    def get_product_prices(self):
        elements = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(el.text.replace("$", "")) for el in elements]

    # ---------- CART ACTIONS ----------

    def add_first_product(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        if buttons:
            buttons[0].click()

    def add_all_products(self):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)
        for button in buttons:
            button.click()

    def remove_all_products(self):
        buttons = self.driver.find_elements(*self.REMOVE_BTNS)
        for button in buttons:
            button.click()

    def get_cart_count(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        if badges:
            return badges[0].text
        return "0"

    def open_cart(self):
        self.click(*self.CART_ICON)

    # ---------- LOGOUT ----------

    def logout(self):
        self.click(*self.MENU_BTN)
        self.click(*self.LOGOUT_LINK)
