from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://google.com")

element = driver.find_element(By.NAME, "q")
usd = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Мне повезёт!"]')

tag = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Мне повезёт!"]')
txt = usd.get_attribute('value') #в переменную с методом text соберется информация об элементе
id = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Мне повезёт!"]').id
ff = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Мне повезёт!"]').value_of_css_property("font-family")
color = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Мне повезёт!"]').value_of_css_property("color")


print(txt) #запрос выведет информацию из переменной в терминал
print(tag)
print(id)
print(ff)
print(color)


driver.quit() #закрываем драйвер