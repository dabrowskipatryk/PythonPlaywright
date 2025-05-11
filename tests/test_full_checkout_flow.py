from fixtures.browser_context import browser_context
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_e2e_checkout_flow(browser_context):
    # Login page - login
    login_page = LoginPage(browser_context)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    # Inventory page - add elements to the cart and open cart
    inventory_page = InventoryPage(browser_context)
    inventory_page.assert_url_for_page()
    inventory_page.add_product_by_name("Sauce Labs Backpack")
    inventory_page.add_product_by_name("Sauce Labs Onesie")
    inventory_page.open_shopping_cart()

    # Cart page - check number of elements and go to checkout
    cart_page = CartPage(browser_context)
    cart_page.assert_url_for_page()
    cart_page.assert_cart_items_count(2)
    cart_page.checkout_button.click()

    # Checkout step one page - fill personal data
    checkout_step_one_page = CheckoutStepOnePage(browser_context)
    checkout_step_one_page.assert_url_for_page()
    checkout_step_one_page.fill_your_information(
        first_name="Patryk",
        last_name="Dabrowski",
        postal_code="60100"
    )
    checkout_step_one_page.click_continue_button()

    # Checkout step two page - check page loaded, check number of elements and finish checkout
    checkout_step_two_page = CheckoutStepTwoPage(browser_context)
    checkout_step_two_page.assert_url_for_page()
    checkout_step_two_page.assert_cart_items_count(2)
    checkout_step_two_page.click_finish_button()


    # Checkout complete page - check if page is displayed with title
    checkout_complete_page = CheckoutCompletePage(browser_context)
    checkout_complete_page.assert_url_for_page()
    checkout_complete_page.assert_complete_header_text("THANK YOU FOR YOUR ORDER")

