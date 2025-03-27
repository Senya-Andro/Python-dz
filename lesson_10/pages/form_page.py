from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    """Класс для работы со страницей формы"""
    def __init__(self, driver):
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу с формой"""
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def fill_first_name(self, first_name: str) -> None:
        """Заполняет поле First Name
        Args:
            first_name: имя для заполнения
        """
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)

    # Аналогично документируем остальные методы fill_*
    # Пример для одного метода:
    def fill_last_name(self, last_name: str) -> None:
        """Заполняет поле Last Name
        Args:
            last_name: фамилия для заполнения
        """
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)

    def submit(self) -> None:
        """Отправляет форму"""
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

class ResultPage:
    """Класс для проверки результатов заполнения формы"""
    def __init__(self, driver):
        self.driver = driver

    def wait_for_zip_code_highlight(self) -> None:
        """Ожидает появления подсветки поля ZIP code"""
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger"))
        )

    def is_zip_code_highlighted_red(self) -> bool:
        """Проверяет, подсвечено ли поле ZIP code красным
        Returns:
            bool: True если поле красное, False если нет
        """
        zip_code_field = self.driver.find_element(By.ID, "zip-code")
        return "alert-danger" in zip_code_field.get_attribute("class")

    def is_field_highlighted_green(self, field_id: str) -> bool:
        """Проверяет, подсвечено ли поле зеленым
        Args:
            field_id: ID проверяемого поля
        Returns:
            bool: True если поле зеленое, False если нет
        """
        element = self.driver.find_element(By.ID, field_id)
        return "alert-success" in element.get_attribute("class")