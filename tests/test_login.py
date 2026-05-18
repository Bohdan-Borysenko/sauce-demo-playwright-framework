import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    
    assert page.locator(".inventory_list").is_visible(), "Unable to log in"
    print("Login successful")