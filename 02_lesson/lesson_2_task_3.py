import math

# Функция для вычисления площади квадрата
def square(side):
    # Вычисляем площадь
    area = side * side
    # Если сторона не целая, округляем результат вверх
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

side1 = 5
side2 = 3.2

print(f"Площадь квадрата со стороной {side1}: {square(side1)}")
print(f"Площадь квадрата со стороной {side2}: {square(side2)}")