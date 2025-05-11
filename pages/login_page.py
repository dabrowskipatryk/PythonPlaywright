from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message_label = page.locator("[data-test='error']")
        self.url = ("https://www.saucedemo.com/v1/index.html")

    def load(self):
        self.page.goto(self.url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def assert_error_message(self, error_message: str):
        expect(self.error_message_label).to_have_text(error_message)

    def assert_url_for_page(self):
        expect(self.page).to_have_url(self.url)