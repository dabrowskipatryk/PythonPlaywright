from fixtures.browser_context import browser_context
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_item_count(browser_context):
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(browser_context)
    inventory_page.assert_url_for_page()
    inventory_page.assert_inventory_items_count(6)

def test_inventory_sorting(browser_context):
    # Login
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Check if Inventory Page is displayed
    inventory_page = InventoryPage(browser_context)
    inventory_page.assert_url_for_page()

    # Sort Inventory Page Z --> A
    inventory_page.sort_by("za")
    inventory_page.assert_lis_sorted(True)


    inventory_page.sort_by("az")
    inventory_page.assert_lis_sorted(False)



    # Check if inventory sorted


    # Sort Inventory Page A --> Z


    # Check if inventory sorted