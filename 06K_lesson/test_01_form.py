from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form():
    driver = webdriver.Edge()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    driver.find_element(By.NAME, "first-name").send_keys("ĐĐ˛Đ°Đ˝")
    driver.find_element(By.NAME, "last-name").send_keys("ĐźĐµŃ‚Ń€ĐľĐ˛")
    driver.find_element(By.NAME, "address").send_keys("Đ›ĐµĐ˝Đ¸Đ˝Đ°, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("ĐśĐľŃĐşĐ˛Đ°")
    driver.find_element(By.NAME, "country").send_keys("Đ ĐľŃŃĐ¸ŃŹ")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    submit_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    )
    driver.execute_script("arguments[0].click();", submit_button)

    zip_code = driver.find_element(By.ID, "zip-code")
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
        element = driver.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute("class")

    driver.quit()
