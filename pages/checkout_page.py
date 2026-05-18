from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.postal_code = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.success_message = page.locator(".complete-header")

    def fill_customer_info(self, first_name: str, last_name: str, postal_code: str):
        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.postal_code, postal_code)
        self.click(self.continue_button)

    def finish_order(self):
        self.click(self.finish_button)

    def get_success_message(self) -> str:
        return self.success_message.inner_text()