from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Явное ожидание
driver.implicitly_wait(20)

# Переход на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажатие на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получение текста из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Вывод в консоль
print(txt)

driver.quit()