
import allure
from selenium import webdriver

from calculator_page import CalculatorPage


@allure.title("Проверка работы калькулятора")
@allure.description(
    "Проверка сложения чисел 7 и 8 с задержкой вычисления."
)
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator():
    driver = webdriver.Chrome()

    try:
        page = CalculatorPage(driver)

        with allure.step("Открыть страницу калькулятора"):
            page.open()

        with allure.step("Установить задержку 45 секунд"):
            page.set_delay(45)

        with allure.step("Выполнить сложение 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")

        with allure.step("Дождаться результата вычисления"):
            page.wait_for_result("15")

        with allure.step("Проверить, что результат равен 15"):
            assert page.get_result() == "15"

    finally:
        driver.quit()
