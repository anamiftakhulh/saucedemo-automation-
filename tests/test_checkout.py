from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def login_add_product_and_go_checkout(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.click_checkout()


def test_checkout_success(driver):
    login_add_product_and_go_checkout(driver)

    checkout = CheckoutPage(driver)

    checkout.enter_checkout_information("John", "Doe", "12345")
    checkout.click_continue()
    checkout.click_finish()

    assert "Thank you for your order!" in checkout.get_success_message()


def test_checkout_empty_first_name(driver):
    login_add_product_and_go_checkout(driver)

    checkout = CheckoutPage(driver)

    checkout.enter_checkout_information("", "Doe", "12345")
    checkout.click_continue()

    assert "Error" in checkout.get_error_message()


def test_checkout_empty_postal_code(driver):
    login_add_product_and_go_checkout(driver)

    checkout = CheckoutPage(driver)

    checkout.enter_checkout_information("John", "Doe", "")
    checkout.click_continue()

    assert "Error" in checkout.get_error_message()
