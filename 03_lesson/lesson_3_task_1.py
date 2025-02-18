from user import User

# Создаем экземпляр класса User
my_user = User("Екатерина", "Иванова")

# Вызываем методы и выводим результаты
print(my_user.get_first_name())  # Ожидаемый результат: "Екатерина"
print(my_user.get_last_name())   # Ожидаемый результат: "Иванова"
print(my_user.get_full_name())   # Ожидаемый результат: "Екатерина Иванова"