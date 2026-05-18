import pytest
from pages.login_page import LoginPage
from data.users import users

@pytest.mark.parametrize("user", users)
def test_login_with_different_users(page, user):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(user["username"], user["password"])

    if user["expected"] == "success":
        assert page.locator(".inventory_list").is_visible(), f"Unable to log in {user['username']}"
        print(f"Successful login {user['username']}")
    else:
        error_msg = login_page.get_error_message()
        assert "Sorry" in error_msg or "locked" in error_msg, "An error was expected"
        print(f"The error is displayed for {user['username']}")