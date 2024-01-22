from unittest.mock import Mock

import pytest

from Tasks import Tasks


def test_find_average():
    assert format(Tasks.find_average([1, 4, 7, 2]), '1f') == format(3.5, '1f')


"""
Модифицируйте функцию find_average так, чтобы она вызывала исключение TypeError, если
ей передается не список.
Напишите тест, который проверяет вызов этого исключения
"""


def test_find_average_rise():
    with pytest.raises(TypeError):
        Tasks.find_average("1, 2, 3")


"""
test balanced
"""


def test_balanced():
    person = Tasks.Person(1000)
    bank = Tasks.Bank()
    person.transfer_money(10, bank)

    assert person.balance == 990
    assert bank.balance == 10


"""
negative test balanced
"""


def test_negative_balanced():
    with pytest.raises(ValueError):
        person = Tasks.Person(1000)
        bank = Tasks.Bank()
        person.transfer_money(10000, bank)


""""
В предыдущем задании используйте unittest.mock для создания мок-объекта Bank.
Напишите тест, в котором вы проверите, вызывается ли метод receive_money с правильным
аргументом.
"""


def test_mock():
    person = Tasks.Person(1000)
    bank = Mock()
    person.transfer_money(100, bank)

    bank.receive_money.assert_called_with(100)


"""
q
"""


def test_divide_ab():
    with pytest.raises(ZeroDivisionError):
        Tasks.divide(1, 0)


def test_normal_division():
    assert Tasks.divide(132, 11) == 12


"""
w

"""


@pytest.mark.parametrize("a, b, expected",
                         [(10, 0, 0),
                          (5, 5, 25),
                          (-1, 5, -5),
                          (-123, -10, 1230),
                          (12, -10, -120)])
def test_multiply(a, b, expected):
    assert Tasks.multiply(a, b) == expected


"""
Создайте функцию square(n), которая возвращает квадрат числа n. 
Напишите doctest, который проверяет работу этой функции.
"""


@pytest.mark.parametrize("a,b",
                         [(2, True),
                          (4, False),
                          (6, False),
                          (3, True),
                          (7, True)])
def test_prime(a, b):
    assert Tasks.is_prime(a) == b


"""
линтер SonarLint

система оценивания:
SonarQube
"""

"""
pip install coverage
coverage run test_new_file.py
coverage report -m
"""