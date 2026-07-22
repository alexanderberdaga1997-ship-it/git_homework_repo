from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage


def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page.add_backpack()
        inventory_page.add_bolt_t_shirt()
        inventory_page.add_onesie()
        inventory_page.open_cart()

        cart_page.checkout()

        checkout_page.fill_form(
            "Alexander",
            "Berdaga",
            "MD-2000"
        )

        total = checkout_page.get_total()

        assert total == "Total: $58.29"

    finally:
        driver.quit()
