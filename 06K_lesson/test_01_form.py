from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполнение формы
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # Нажатие кнопки Submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Ожидание появления подсветки для поля Zip code
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
    )

    # Проверка, что поле Zip code подсвечено красным
    zip_code_field = driver.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class"), "Поле Zip code не подсвечено красным"

    # Проверка, что остальные поля подсвечены зеленым
    fields_to_check = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
    ]
    for field in fields_to_check:
        element = driver.find_element(By.ID, field)
        assert "alert-success" in element.get_attribute("class"), f"Поле {field} не подсвечено зеленым"

    print("Все проверки прошли успешно!")

finally:
    driver.quit()