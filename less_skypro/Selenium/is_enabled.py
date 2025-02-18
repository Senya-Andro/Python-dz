from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# yes_radio = driver.find_element(By.CSS_SELECTOR, "yesRadio")
# is_enabled = yes_radio.is_enabled()
# print("Элемент yesRadio доступен:", is_enabled)
#
# no_radio = driver.find_element(By.CSS_SELECTOR, "noRadio")
# is_enabled = no_radio.is_enabled()
# print("Элемент noRadio доступен:", is_enabled)
#
# driver.quit()

driver.get("https://demoqa.com/radio-button")

is_enabled = driver.find_element(By.CSS_SELECTOR, "yesRadio").is_enabled()
print(is_enabled)

is_enabled = driver.find_element(By.CSS_SELECTOR, "noRadio").is_enabled()
print(is_enabled)

driver.quit()