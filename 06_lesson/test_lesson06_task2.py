from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def test_cookie_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    cookie_user_1 = "ZTFkOWJkYWQtYTk2OC00MzA0LTg3M2EtNDkxZTY5ZmVkNjU5"
    cookie_user_2 = "ODJjNGRiNDEtNjMyOC00MDY0LWJkYWQtNmM1MjRlMjc0ZmEx"

    profile_user_1 = "https://gitflic.ru/user/alexandr985"
    profile_user_2 = "https://gitflic.ru/user/fvaheryig"

    try:
        # Пользователь 1
        driver.get("https://gitflic.ru/")
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": cookie_user_1,
            }
        )
        driver.refresh()

        driver.get(profile_user_1)
        wait.until(lambda browser: "alexandr985" in browser.current_url)
        url_user_1 = driver.current_url

        # Выход из первого аккаунта через очистку cookie
        driver.delete_all_cookies()

        # Пользователь 2
        driver.get("https://gitflic.ru/")
        driver.add_cookie(
            {
                "name": "SESSION",
                "value": cookie_user_2,
            }
        )
        driver.refresh()

        driver.get(profile_user_2)
        wait.until(lambda browser: "fvaheryig" in browser.current_url)
        url_user_2 = driver.current_url

        assert url_user_1 != url_user_2

    finally:
        driver.quit()