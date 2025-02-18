from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

element = driver.find_element(By.NAME, "q") #нашли элемент - строку поиска
element.clear()
element.send_keys("test skypro") #отправляем текст
sleep(3)
element.clear()


sleep(5)

driver.quit()