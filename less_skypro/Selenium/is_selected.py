from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox1 = driver.find_element(By.CSS_SELECTOR, "input[type=checkbox]")
checkbox1.click()

is_selected = checkbox1.is_selected()
print(is_selected)

sleep(3)

is_selected = checkbox1.is_selected()
print(is_selected)

sleep(3)

driver.quit()