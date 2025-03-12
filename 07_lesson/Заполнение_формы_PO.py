from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Класс FormPage
class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)

    def fill_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)

    def fill_phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)

    def fill_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)

    def fill_country(self, country):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)

    def fill_job_position(self, job_position):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)

    def fill_company(self, company):
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    def submit(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


# Класс ResultPage
class ResultPage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_zip_code_highlight(self):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
        )

    def is_zip_code_highlighted_red(self):
        zip_code_field = self.driver.find_element(By.ID, "zip-code")
        return "alert-danger" in zip_code_field.get_attribute("class")

    def is_field_highlighted_green(self, field_id):
        element = self.driver.find_element(By.ID, field_id)
        return "alert-success" in element.get_attribute("class")


# Тест
def test_form_submission():
    driver = webdriver.Chrome()
    try:
        form_page = FormPage(driver)
        form_page.open()
        form_page.fill_first_name("Иван")
        form_page.fill_last_name("Петров")
        form_page.fill_address("Ленина, 55-3")
        form_page.fill_email("test@skypro.com")
        form_page.fill_phone("+7985899998787")
        form_page.fill_city("Москва")
        form_page.fill_country("Россия")
        form_page.fill_job_position("QA")
        form_page.fill_company("SkyPro")
        form_page.submit()

        result_page = ResultPage(driver)
        result_page.wait_for_zip_code_highlight()

        assert result_page.is_zip_code_highlighted_red(), "Поле Zip code не подсвечено красным"

        fields_to_check = [
            "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
        ]
        for field in fields_to_check:
            assert result_page.is_field_highlighted_green(field), f"Поле {field} не подсвечено зеленым"

        print("Все проверки прошли успешно!")

    finally:
        driver.quit()

if __name__ == "__main__":
    test_form_submission()