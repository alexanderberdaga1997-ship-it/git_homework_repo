from selenium import webdriver


def test_session_storage_auth():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://gitflic.ru")

    driver.add_cookie({
        "name": "SESSION",
        "value": "ВСТАВЬ_СЮДА_ЗНАЧЕНИЕ_COOKIE"
    })

    driver.refresh()

    driver.quit()