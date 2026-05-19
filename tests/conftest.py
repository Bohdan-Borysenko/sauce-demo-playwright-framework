import pytest
from config.config import Config
from utils.logger import logger
from utils.helpers import take_screenshot

config = Config()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(config.timeout)
    logger.info(f"The page is open: {page.url}")
    yield page
    context.close()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        try:
            page = item.funcargs.get("page")
            if page:
                take_screenshot(page, item.name)
                logger.error(f"The test failed: {item.name}")
        except:
            pass