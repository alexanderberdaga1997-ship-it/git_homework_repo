
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет экземпляр браузера для работы с корзиной."""
        self.driver = driver

    def checkout(self) -> None:
        """Нажимает кнопку перехода к оформлению заказа."""
        self.driver.find_element(
            By.ID,
            "checkout"
        ).click()
