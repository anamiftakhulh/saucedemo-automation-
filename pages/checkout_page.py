from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    # -------- STEP ONE (Information Page) --------
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    # -------- STEP TWO (Overview Page) --------
    FINISH_BTN = (By.ID, "finish")

    # -------- COMPLETE PAGE --------
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    # ---------- ACTIONS ----------

    def enter_checkout_information(self, first, last, postal):
        self.type(*self.FIRST_NAME, first)
        self.type(*self.LAST_NAME, last)
        self.type(*self.POSTAL_CODE, postal)

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)

    def click_finish(self):
        self.click(*self.FINISH_BTN)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MSG)

    def get_success_message(self):
        return self.get_text(*self.COMPLETE_HEADER)
