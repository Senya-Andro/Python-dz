import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Ввод значения 45 в поле ввода по локатору #delay
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажатие на кнопки 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    # Ожидание результата в течении 45 секунд
    result = WebDriverWait(driver, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    # Проверка результата
    result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result_text == "15", f"Ожидаемый результат 15, но получили {result_text}"

    print("Тест пройден успешно!")

finally:
    driver.quit()