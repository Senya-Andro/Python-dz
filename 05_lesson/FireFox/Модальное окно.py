from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
    # открыть страницу
    driver.get("http://the-internet.herokuapp.com/entry_ad")

    # дождаться появления модального окна и нажать на кнопку "Close"
    # ждем, пока модальное окно станет видимым
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC

    # Ожидание появления модального окна
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "modal"))
    )

    # находим кнопку "Close" внутри модального окна и кликаем по ней
    close_button = modal.find_element(By.XPATH, ".//p[text()='Close']")
    close_button.click()

    sleep(5)

finally:
    driver.quit()