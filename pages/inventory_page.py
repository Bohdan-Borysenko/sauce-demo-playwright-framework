from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.inventory_list = page.locator(".inventory_list")
        self.cart_icon = page.locator(".shopping_cart_link")
        self.add_to_cart_buttons = page.locator("button[id^='add-to-cart']")

    def add_first_item_to_cart(self):
        self.add_to_cart_buttons.first.click()

    def go_to_cart(self):
        self.click(self.cart_icon)