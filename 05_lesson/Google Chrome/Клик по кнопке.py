from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # открыть страницу
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

    # пять раз кликнуть на кнопку "Add Element"
    add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    for _ in range(5):
        add_button.click()

    # собрать со страницы список кнопок "Delete"
    delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

    # вывести на экран размер списка
    print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

finally:
    # Закрытие браузера
    driver.quit()