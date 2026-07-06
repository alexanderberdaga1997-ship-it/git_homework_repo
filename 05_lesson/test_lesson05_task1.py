from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/")

    driver.find_element(By.LINK_TEXT, "HTML Forms").click()

    assert "/forms/post" in driver.current_url

    driver.back()

    assert "httpbin.org" in driver.current_url

    driver.quit()
    