from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_user_logout_invalidates_session(driver):
    """
    Verify that:
    1. User can logout successfully
    2. User is redirected to login page
    3. Direct URL access to inventory is blocked after logout
    """

    # ---------- Step 1: Login ----------
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)

    # ---------- Step 2: Logout ----------
    inventory.logout()

    # ---------- Step 3: Verify redirected to Login Page ----------
    assert login.is_login_page_displayed(), "User is not redirected to login page after logout"

    # ---------- Step 4: Try direct access to protected page ----------
    driver.get("https://www.saucedemo.com/inventory.html")

    # ---------- Step 5: Verify session is invalidated ----------
    assert login.is_login_page_displayed(), \
        "User was able to access inventory page after logout (Session not invalidated)"
