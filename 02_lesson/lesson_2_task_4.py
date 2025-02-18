# Функция FizzBuzz
def fizz_buzz(n):
    for i in range(1, n + 1):  # Цикл от 1 до n включительно
        if i % 3 == 0 and i % 5 == 0:  # Если делится на 3 и на 5
            print("FizzBuzz")
        elif i % 3 == 0:  # Если делится на 3
            print("Fizz")
        elif i % 5 == 0:  # Если делится на 5
            print("Buzz")
        else:
            print(i)

fizz_buzz(17)