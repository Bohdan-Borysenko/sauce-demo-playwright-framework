import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.mark.e2e
def test_full_purchase_flow(page):
    # Login
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    # Inventory → Add to cart
    inventory_page = InventoryPage(page)
    inventory_page.add_first_item_to_cart()
    inventory_page.go_to_cart()

    # Cart
    cart_page = CartPage(page)
    assert cart_page.get_cart_items_count() > 0, "Your cart is empty"

    cart_page.go_to_checkout()

    # Checkout
    checkout_page = CheckoutPage(page)
    checkout_page.fill_customer_info("Богдан", "Test", "58000")
    checkout_page.finish_order()

    # Final check
    assert "Thank you for your order!" in checkout_page.get_success_message()
    print("The entire purchase process has been successfully completed!")