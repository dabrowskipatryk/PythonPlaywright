import pytest

from fixtures.browser_context import browser_context
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


# def test_successfull_login(browser_context):
#     login_page = LoginPage(browser_context)
#     login_page.load()
#     login_page.login("standard_user", "secret_sauce")
#     #Openning inventory page
#     inventory_page = InventoryPage(browser_context)
#     inventory_page.assert_url_for_page()

@pytest.mark.parametrize(("username", "password", "message"), [
    ("", "", "Username is required"),
    ("standard_user", "",  "Password is required"),
    ("standard_user", "wrong_password", "Username and password do not match any user in this service"),
])
def test_invalid_login(browser_context, username, password, message):
    # Initialize page with page from line "yield page"
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login(username, password)
    login_page.assert_error_message(f"Epic sadface: {message}")
    login_page.assert_url_for_page()

