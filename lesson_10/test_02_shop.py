
import allure
from selenium import webdriver

from cart_page import CartPage
from checkout_page import CheckoutPage
from inventory_page import InventoryPage
from login_page import LoginPage


@allure.title("Проверка оформления заказа в интернет-магазине")
@allure.description(
    "Проверка авторизации, добавления трёх товаров "
    "в корзину и итоговой стоимости заказа."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Firefox()

    try:
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Открыть сайт SauceDemo"):
            login_page.open()

        with allure.step("Авторизоваться в интернет-магазине"):
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавить рюкзак в корзину"):
            inventory_page.add_backpack()

        with allure.step("Добавить футболку в корзину"):
            inventory_page.add_bolt_t_shirt()

        with allure.step("Добавить боди в корзину"):
            inventory_page.add_onesie()

        with allure.step("Открыть корзину"):
            inventory_page.open_cart()

        with allure.step("Перейти к оформлению заказа"):
            cart_page.checkout()

        with allure.step("Заполнить данные покупателя"):
            checkout_page.fill_form(
                "Alexander",
                "Berdaga",
                "MD-2000"
            )

        with allure.step("Получить итоговую сумму заказа"):
            total = checkout_page.get_total()

        with allure.step("Проверить итоговую сумму заказа"):
            assert total == "Total: $58.29"

    finally:
        driver.quit()
