from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/forms/post")

    driver.find_element(By.NAME, "custname").send_keys("Alexander")

    driver.find_element(By.XPATH, "//button").click()

    assert "/post" in driver.current_url

    driver.quit()