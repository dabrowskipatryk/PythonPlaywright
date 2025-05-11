from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = ("https://www.saucedemo.com/v1/cart.html")
        self.cart_items = page.locator(".cart_item")
        self.checkout_button = page.locator(".checkout_button")

    def assert_url_for_page(self):
        expect(self.page).to_have_url(self.url)

    def assert_cart_items_count(self, expected_count: int):
        expect(self.cart_items).to_have_count(expected_count)

    def click_checkout_button(self):
        self.checkout_button.click()