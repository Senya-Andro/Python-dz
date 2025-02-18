from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # открыть страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # ввести значение "tomsmith" в поле username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # ввести значение "SuperSecretPassword!" в поле password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # нажать кнопку "Login"
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    sleep(5)

finally:
    driver.quit()