
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет экземпляр браузера для работы со страницей."""
        self.driver = driver

    def enter_first_name(self, first_name: str) -> None:
        """Вводит имя покупателя."""
        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """Вводит фамилию покупателя."""
        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """Вводит почтовый индекс покупателя."""
        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

    def click_continue(self) -> None:
        """Нажимает кнопку продолжения оформления заказа."""
        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def fill_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> None:
        """Заполняет данные покупателя и продолжает оформление."""
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total(self) -> str:
        """Возвращает итоговую сумму заказа в виде строки."""
        return self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label"
        ).text
