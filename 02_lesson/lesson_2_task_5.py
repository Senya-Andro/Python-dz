# Функция для определения сезона по номеру месяца
def month_to_season(month):
    if month in [12, 1, 2]:  # Зима
        return "Зима"
    elif month in [3, 4, 5]:  # Весна
        return "Весна"
    elif month in [6, 7, 8]:  # Лето
        return "Лето"
    elif month in [9, 10, 11]:  # Осень
        return "Осень"
    else:
        return "Неверный номер месяца"  # Обработка некорректного ввода


print(month_to_season(7))
