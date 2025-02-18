from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.maximize_window() #развернуть окно под размер экрана
# driver.minimize_window() #свернуть окно
# driver.fullscreen_window() #развернуть окно на весь экран (аналог клавиши F11)

driver.get("https://ya.ru")
driver.set_window_size(1000, 600)

sleep(5)