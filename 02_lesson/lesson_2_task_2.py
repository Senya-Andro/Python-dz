# Функция для проверки, является ли год високосным
def is_year_leap(year):
    # Если год делится на 4 без остатка, он високосный
    if year % 4 == 0:
        return True
    else:
        return False


# Вызов функции и передача года
year = 2025
result = is_year_leap(year)


print(f"год {year}: {result}")