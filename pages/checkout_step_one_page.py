from playwright.sync_api import Page, expect


class CheckoutStepOnePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = ("https://www.saucedemo.com/v1/checkout-step-one.html")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.cart_button = page.locator(".cart_button")


    def assert_url_for_page(self):
        expect(self.page).to_have_url(self.url)

    def fill_your_information(self, first_name: str, last_name: str, postal_code: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)

    def click_continue_button(self):
        self.cart_button.click()
