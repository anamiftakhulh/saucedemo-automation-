from pages.login_page import LoginPage


def test_login_valid(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url


def test_login_invalid(driver):
    login = LoginPage(driver)
    login.load()
    login.login("invalid_user", "secret_sauce")

    assert "Epic sadface" in login.get_error()
