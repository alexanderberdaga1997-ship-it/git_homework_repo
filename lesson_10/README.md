# Домашнее задание № 10 — Allure

В проекте реализованы автоматизированные тесты с использованием Python, pytest, Selenium и Allure.

Для работы со страницами используется паттерн PageObject. Методы классов содержат описания, аннотации типов параметров и возвращаемых значений.

## Проверяемая функциональность

- Калькулятор — проверка сложения чисел 7 и 8 с задержкой вычисления.
- Интернет-магазин SauceDemo — проверка авторизации, добавления трёх товаров в корзину и итоговой суммы заказа.

## Установка зависимостей

Для запуска тестов необходимы Python, Google Chrome и Mozilla Firefox.

Установите Python-библиотеки:

```powershell
python -m pip install pytest selenium allure-pytest
```

Для просмотра отчётов необходимо отдельно установить Allure CLI и Java.

## Запуск тестов

Из корневой папки репозитория выполните:

```powershell
python -m pytest lesson_10 -v --alluredir=lesson_10/allure-results
```

Результаты тестирования будут сохранены в папке `lesson_10/allure-results`.

## Просмотр Allure-отчёта

Если Allure CLI добавлен в PATH, выполните из корня репозитория:

```powershell
allure serve lesson_10/allure-results
```

Для Windows можно запустить Allure напрямую из распакованной папки:

```powershell
& "$env:USERPROFILE\Downloads\allure-2.46.1\allure-2.46.1\bin\allure.bat" serve lesson_10/allure-results
```

После выполнения команды отчёт откроется в браузере. В нём можно посмотреть результаты тестирования, шаги и проверки.

## Проверка стиля кода

Из корня репозитория выполните:

```powershell
python -m flake8 lesson_10
```

Папки `allure-results`, `allure-report` и временные файлы Python не должны добавляться в Git.