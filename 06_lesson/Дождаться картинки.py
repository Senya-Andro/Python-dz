from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Переход на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Ожидание загрузки всех картинок
WebDriverWait(driver, 20).until(
  EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img"))
)

# Получение атрибута src у 3-й картинки
images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")  # Находим все изображения

if len(images) >= 3:  # Проверяем, что есть хотя бы 3 картинки
    src_attribute = images[2].get_attribute("src")
    print(f"Атрибут src у 3-й картинки: {src_attribute}")
else:
    print(f"Найдено изображений: {len(images)}")

driver.quit()
