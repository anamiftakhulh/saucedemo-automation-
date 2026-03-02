from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def login_and_open_inventory(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")


# -------- INVENTORY DISPLAY TEST --------

def test_inventory_page_loaded(driver):
    login_and_open_inventory(driver)

    assert "inventory" in driver.current_url


def test_inventory_products_displayed(driver):
    login_and_open_inventory(driver)

    inventory = InventoryPage(driver)

    names = inventory.get_product_names()
    prices = inventory.get_product_prices()

    assert len(names) > 0
    assert len(prices) > 0
    assert len(names) == len(prices)


# -------- SORTING TESTS --------

def test_sort_name_a_to_z(driver):
    login_and_open_inventory(driver)

    inventory = InventoryPage(driver)

    inventory.sort_by_visible_text("Name (A to Z)")
    names = inventory.get_product_names()

    assert names == sorted(names)


def test_sort_name_z_to_a(driver):
    login_and_open_inventory(driver)

    inventory = InventoryPage(driver)

    inventory.sort_by_visible_text("Name (Z to A)")
    names = inventory.get_product_names()

    assert names == sorted(names, reverse=True)


def test_sort_price_low_to_high(driver):
    login_and_open_inventory(driver)

    inventory = InventoryPage(driver)

    inventory.sort_by_visible_text("Price (low to high)")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices)


def test_sort_price_high_to_low(driver):
    login_and_open_inventory(driver)

    inventory = InventoryPage(driver)

    inventory.sort_by_visible_text("Price (high to low)")
    prices = inventory.get_product_prices()

    assert prices == sorted(prices, reverse=True)
