lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

result = []
for x in lst:
    if x < 30 and x % 3 == 0:
        result.append(x)

print("Элементы, которые меньше 30 и делятся на 3 без остатка:", result)