from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(
            By.ID,
            "first-name"
        ).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(
            By.ID,
            "last-name"
        ).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(
            By.ID,
            "postal-code"
        ).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(
            By.ID,
            "continue"
        ).click()

    def fill_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()

    def get_total(self):
        return self.driver.find_element(
            By.CLASS_NAME,
            "summary_total_label"
        ).text
