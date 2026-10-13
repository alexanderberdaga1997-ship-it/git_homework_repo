
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class InventoryPage:
    """Класс для работы со страницей товаров."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет экземпляр браузера для работы со страницей."""
        self.driver = driver

    def add_backpack(self) -> None:
        """Добавляет рюкзак Sauce Labs в корзину."""
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-backpack"
        ).click()

    def add_bolt_t_shirt(self) -> None:
        """Добавляет футболку Sauce Labs Bolt в корзину."""
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

    def add_onesie(self) -> None:
        """Добавляет боди Sauce Labs Onesie в корзину."""
        self.driver.find_element(
            By.ID,
            "add-to-cart-sauce-labs-onesie"
        ).click()

    def open_cart(self) -> None:
        """Открывает корзину с добавленными товарами."""
        self.driver.find_element(
            By.CLASS_NAME,
            "shopping_cart_link"
        ).click()
