
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """Сохраняет экземпляр браузера для работы со страницей."""
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации SauceDemo."""
        self.driver.get("https://www.saucedemo.com/")

    def enter_username(self, username: str) -> None:
        """Вводит имя пользователя в поле авторизации."""
        self.driver.find_element(
            By.ID,
            "user-name"
        ).send_keys(username)

    def enter_password(self, password: str) -> None:
        """Вводит пароль в соответствующее поле."""
        self.driver.find_element(
            By.ID,
            "password"
        ).send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку входа на сайт."""
        self.driver.find_element(
            By.ID,
            "login-button"
        ).click()

    def login(self, username: str, password: str) -> None:
        """Вводит данные пользователя и выполняет вход."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
