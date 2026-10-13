
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет экземпляр браузера для работы со страницей."""
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    def set_delay(self, delay: int) -> None:
        """Устанавливает задержку вычисления в секундах."""
        delay_input = self.driver.find_element(
            By.CSS_SELECTOR,
            "#delay"
        )
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, value: str) -> None:
        """Нажимает кнопку калькулятора с указанным значением."""
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{value}']"
        ).click()

    def wait_for_result(self, result: str) -> None:
        """Ожидает появления нужного результата на экране."""
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"),
                result
            )
        )

    def get_result(self) -> str:
        """Возвращает результат, отображаемый калькулятором."""
        return self.driver.find_element(
            By.CLASS_NAME,
            "screen"
        ).text
