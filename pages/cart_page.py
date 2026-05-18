from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_button = page.locator("#checkout")
        self.cart_item = page.locator(".cart_item")
        self.continue_shopping_button = page.locator("#continue-shopping")

    def go_to_checkout(self):
        self.click(self.checkout_button)

    def get_cart_items_count(self) -> int:
        return self.cart_item.count()