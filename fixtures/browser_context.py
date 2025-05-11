import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        yield page

        #Teardown
        context.close()
        browser.close()

