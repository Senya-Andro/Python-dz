from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на сайт
driver.get("http://uitestingplayground.com/textinput")

# Ввод текста
input_field = driver.find_element(By.ID, "newButtonName")
input_field.clear()
input_field.send_keys("SkyPro")

# Нажатие на синюю кнопку
button = driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Ожидание обновления текста кнопки
wait = WebDriverWait(driver, 10)
updated_button = wait.until(
  EC.presence_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
)

# Получение текста кнопки
updated_button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button_text1 = updated_button.text

# Вывод в консоль

print(f"Текст кнопки после нажатия: {button_text1}")
button_text = updated_button.text
print(button_text)

driver.quit()