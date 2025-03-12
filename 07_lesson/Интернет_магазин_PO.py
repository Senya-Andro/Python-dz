from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Класс для страницы авторизации
class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()


# Класс для страницы каталога товаров
class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        item_xpath = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        self.driver.find_element(By.XPATH, item_xpath).click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


# Класс для страницы корзины
class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()


# Класс для страницы оформления заказа
class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)

    def continue_to_overview(self):
        self.driver.find_element(By.ID, "continue").click()

    def get_total_amount(self):
        return self.driver.find_element(By.CLASS_NAME, "summary_total_label").text.split("$")[1]


# Тест
def test_saucedemo():
    driver = webdriver.Chrome()
    try:
        # Открытие страницы авторизации и вход в систему
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        # Добавление товаров в корзину
        inventory_page = InventoryPage(driver)
        items_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie"
        ]
        for item in items_to_add:
            inventory_page.add_item_to_cart(item)

        # Переход в корзину и оформление заказа
        inventory_page.go_to_cart()
        cart_page = CartPage(driver)
        cart_page.checkout()

        # Заполнение формы оформления заказа
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_shipping_info("Иван", "Иванов", "123456")
        checkout_page.continue_to_overview()

        # Проверка итоговой суммы
        total_amount = checkout_page.get_total_amount()
        assert total_amount == "58.29", f"Итоговая сумма не совпадает. Ожидалось: $58.29, Фактически: ${total_amount}"

        print("Тест пройден успешно. Итоговая сумма равна $58.29")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_saucedemo()