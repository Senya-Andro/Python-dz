from email.policy import strict

import pytest

from calculator import Calculator

calculator = Calculator()

#@pytest.mark.skip(reason="починить тест позже") #функция, если нужно пропустить эту проверку
#@pytest.mark.xfail(strict=True) #функция, если ожидается, что тест упадет. В скобках говорится о том, что нужно указать, что он действительно упал
#@pytest.mark.positive_test
@pytest.mark.parametrize( 'num1, num2, result', [ (4,5,9), (-6, -10, -16), (-6, 6, 0), (5.61, 4.29, 9.9), (10,0, 10)] )
def test_sum_positive_nums(num1, num2, result):
    calculator = Calculator()
    res = calculator.sum(num1, num2)
    assert res == result



def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-6, 6)
    assert res == 0

def test_sum_float_nums():
    calculator = Calculator()
    res = calculator.sum(5.6, 4.3)
    res = round(res, 1)
    assert res == 9.9

def test_sum_zero_nums():
    calculator = Calculator()
    res = calculator.sum(10, 0) #вот эта строка вызывает ошибку
    assert res == 10

@pytest.mark.positive_test
def test_div_positive():
    calculator = Calculator()
    res = calculator.div(10, 2)
    assert res == 5

def test_div_by_zero():
    calculator = Calculator()
    with pytest.raises(ArithmeticError):
        calculator.div(10, 0)

@pytest.mark.parametrize( 'nums, result', [ ([], 0)] )
def test_avg_empty_list(nums, result):
    calculator = Calculator()
    numbers = []
    res = calculator.avg(nums)
    assert res == result

@pytest.mark.positive_test
def test_avg_positive_list():
    calculator = Calculator()
    numbers = [1,2,3,4,5,6,7,8,9,5]
    res = calculator.avg(numbers)
    assert res == 5


# print("start")
# res = calculator.sum(4,5)
# assert res == 9
#
# res = calculator.sum(-6, -10)
# assert res == -16
#
# res = calculator.sum(-6, 6)
# assert res == 0
#
# # round result ?
# res = calculator.sum(5.6, 4.3) #Python посчитает сумму
# res = round(res, 1) #округлит ее до одного знака после запятой
# #print(res) #напечатает сумму
# assert res == 9.9 #сравнит с предполагаемым значением
#
# res = calculator.sum(10, 0)
# assert res == 10
#
# res = calculator.div(10, 2)
# assert res == 5
#
# #res = calculator.div(10, 0)
# #assert res == None
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
# res = calculator.avg(numbers)
# print(res)
# assert res == 5
#
# print("finish")