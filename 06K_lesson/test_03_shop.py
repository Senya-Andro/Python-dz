from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

try:
    # Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Авторизация как пользователь standard_user
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Добавление товаров в корзину
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]

    for item_name in items_to_add:
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_to_cart_button = driver.find_element(By.XPATH, item_xpath)
        add_to_cart_button.click()

    # Переход в корзину
    cart_button = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_button.click()

    # Нажатие на кнопку Checkout
    checkout_button = driver.find_element(By.ID, "checkout")
    checkout_button.click()

    # Заполнение формы своими данными
    first_name_field = driver.find_element(By.ID, "first-name")
    last_name_field = driver.find_element(By.ID, "last-name")
    postal_code_field = driver.find_element(By.ID, "postal-code")

    first_name_field.send_keys("Иван")
    last_name_field.send_keys("Иванов")
    postal_code_field.send_keys("123456")

    # Нажатие на кнопку Continue
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()

    # Чтение итоговой стоимости
    total_amount = driver.find_element(By.CLASS_NAME, "summary_total_label").text
    total_amount_value = total_amount.split("$")[1]

    # Проверка, что итоговая сумма равна $58.29
    assert total_amount_value == "58.29", f"Итоговая сумма не совпадает. Ожидалось: $58.29, Фактически: ${total_amount_value}"

    print("Тест пройден успешно. Итоговая сумма равна $58.29")

finally:
    driver.quit()