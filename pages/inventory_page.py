from playwright.sync_api import Page, expect


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = ("https://www.saucedemo.com/v1/inventory.html")
        self.inventory_items = page.locator(".inventory_item")
        self.inventory_item_names = page.locator(".inventory_item_name")
        self.shopping_cart = page.locator("#shopping_cart_container")
        self.sort_dropdown = page.locator("select.product_sort_container")

    def assert_url_for_page(self):
        expect(self.page).to_have_url(self.url)

    def assert_inventory_items_count(self, expected_count: int):
        expect(self.inventory_items).to_have_count(expected_count)

    def add_product_by_name(self, product_name: str):
        self.page.locator(f".inventory_item:has-text('{product_name}') button").click()

    def open_shopping_cart(self):
        self.shopping_cart.click()

    def sort_by(self, option: str):
        self.sort_dropdown.select_option(option)

    # Sorting - metoda pomocnicza
    # Definijemy że zwróci listę z webowego elementu

    def get_product_names(self) -> list:
        return [el.inner_text() for el in self.inventory_item_names.all()]

    # def assert_sorted_z_to_a(self):
    #     names = self.get_product_names()
    #     assert names == sorted(names, reverse=True), f"Expected Z -> A, got {names}"
    #
    # def assert_sorted_a_to_z(self):
    #     names = self.get_product_names()
    #     assert names == sorted(names), f"Expected A -> Z, got {names}"

    # Dwie powyższe metody w jednej
    def assert_lis_sorted(self, non_alphabetical_order: bool):
        names = self.get_product_names()
        assert names == sorted(names, reverse=non_alphabetical_order)
