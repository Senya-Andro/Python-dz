import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Класс для страницы калькулятора
class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys(delay)

    def click_button(self, button_text):
        self.driver.find_element(By.XPATH, f"//span[text()='{button_text}']").click()

    def click_buttons(self, *buttons):
        for button in buttons:
            self.click_button(button)


# Класс для проверки результата
class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_result(self, timeout):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text


# Тест
def test_calculator():
    driver = webdriver.Chrome()
    try:
        calculator_page = CalculatorPage(driver)
        calculator_page.open()
        calculator_page.set_delay("45")
        calculator_page.click_buttons("7", "+", "8", "=")

        result_page = ResultPage(driver)
        result_page.wait_for_result(45)

        result_text = result_page.get_result()
        assert result_text == "15", f"Ожидаемый результат 15, но получили {result_text}"

        print("Тест пройден успешно!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_calculator()