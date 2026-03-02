from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def login_and_go_inventory(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")


def test_add_single_product_to_cart(driver):
    login_and_go_inventory(driver)

    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    inventory.add_first_product()
    assert inventory.get_cart_count() == "1"

    cart.open_cart()
    assert cart.get_cart_items_count() == 1


def test_add_multiple_products_to_cart(driver):
    login_and_go_inventory(driver)

    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    inventory.add_first_product()
    inventory.add_first_product()  # Add another product

    cart.open_cart()
    assert cart.get_cart_items_count() >= 1


def test_remove_product_from_cart(driver):
    login_and_go_inventory(driver)

    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    inventory.add_first_product()
    cart.open_cart()

    cart.remove_first_item()
    assert cart.get_cart_items_count() == 0
