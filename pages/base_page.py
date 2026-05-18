from playwright.sync_api import Page, Locator
from abc import ABC

class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page
        self.timeout = 15000

    def goto(self, url: str):
        self.page.goto(url)

    def is_visible(self, locator: Locator, timeout: int = None):
        return locator.is_visible(timeout=timeout or self.timeout)

    def click(self, locator: Locator):
        locator.click()

    def fill(self, locator: Locator, value: str):
        locator.fill(value)