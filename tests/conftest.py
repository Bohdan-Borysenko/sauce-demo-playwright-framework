import pytest
from utils.helpers import take_screenshot

@pytest.fixture(autouse=True)
def open_base_url(page):
    if "saucedemo.com" not in page.url:
        page.goto("https://www.saucedemo.com/")
    yield

# Автоскриншот при падении теста
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                take_screenshot(page, item.name)
        except:
            pass