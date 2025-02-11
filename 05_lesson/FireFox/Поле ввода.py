from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # найти поле ввода и ввести текст "1000"
    input_field = driver.find_element(By.TAG_NAME, "input")
    input_field.send_keys("1000")

    # очистить поле
    input_field.clear()

    # ввести текст "999"
    input_field.send_keys("999")

    sleep(5)

finally:
    driver.quit()