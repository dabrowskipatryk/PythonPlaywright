from playwright.sync_api import Page, expect


class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://www.saucedemo.com/v1/checkout-complete.html"
        self.complete_header = page.locator(".complete-header")
        self.checkout_button = page.locator(".checkout_button")

    def assert_url_for_page(self):
        expect(self.page).to_have_url(self.url)

    def assert_complete_header_text(self, expected_text: str):
        expect(self.complete_header).to_have_text(expected_text)

