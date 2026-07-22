from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://bonigarcia.dev/"
            "selenium-webdriver-java/data-types.html"
        )

        wait.until(
            EC.visibility_of_element_located(
                (By.NAME, "first-name")
            )
        ).send_keys("ÄÂÄË›ÄÂ°ÄËť")

        driver.find_element(
            By.NAME, "last-name"
        ).send_keys("ÄĹşÄÂµĹâ€šĹâ‚¬ÄÄľÄË›")

        driver.find_element(
            By.NAME, "address"
        ).send_keys("Äâ€şÄÂµÄËťÄÂ¸ÄËťÄÂ°, 55-3")

        driver.find_element(
            By.NAME, "e-mail"
        ).send_keys("test@skypro.com")

        driver.find_element(
            By.NAME, "phone"
        ).send_keys("+7985899998787")

        driver.find_element(
            By.NAME, "city"
        ).send_keys("ÄĹ›ÄÄľĹÂÄĹźÄË›ÄÂ°")

        driver.find_element(
            By.NAME, "country"
        ).send_keys("ÄÂ ÄÄľĹÂĹÂÄÂ¸ĹĹą")

        driver.find_element(
            By.NAME, "job-position"
        ).send_keys("QA")

        driver.find_element(
            By.NAME, "company"
        ).send_keys("SkyPro")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button[type='submit']")
            )
        )
        driver.execute_script(
            "arguments[0].click();",
            submit_button
        )

        zip_code = wait.until(
            EC.visibility_of_element_located(
                (By.ID, "zip-code")
            )
        )
        assert "alert-danger" in zip_code.get_attribute("class")

        fields = [
            "first-name",
            "last-name",
            "address",
            "e-mail",
            "phone",
            "city",
            "country",
            "job-position",
            "company",
        ]

        for field in fields:
            element = wait.until(
                EC.visibility_of_element_located(
                    (By.ID, field)
                )
            )
            assert "alert-success" in element.get_attribute("class")

    finally:
        driver.quit()
