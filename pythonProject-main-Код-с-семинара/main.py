# This is a sample Python script.
from Tasks import Tasks
import random

from list_average import ListAverage


def main():
    la = ListAverage.ListAverage(random.sample(range(100), 10), random.sample(range(100), 10))
    average0 = la.average_first_list
    average1 = la.average_second_list

    print(f"Первый список: {la.first_list}")
    print(f"Второй список: {la.second_list}")
    print()

    if average0 > average1:
        print(f"Первый список имеет большее среднее значение ({average0}) чем второй список ({average1})")
    elif average1 > average0:
        print(f"Второй список имеет большее среднее значение ({average1}) чем первый список ({average0})")
    else:
        print(f"Средние значения первого и второго списка равны {average0}")


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # Примеры использования функций:
    # 1
    avg = Tasks.find_average([1, 2, 3, 4, 5])
    print(avg)

    # 2
    print_hi('andre')
    # 3
    person = Tasks.Person(1000)
    bank = Tasks.Bank()
    person.transfer_money(100, bank)
    print(bank.balance)

    # 5
    result = Tasks.divide(10, 2)
    print(result)

    # 6
    product = Tasks.multiply(4, 5)
    print(product)

    # 8
    sq = Tasks.square(4)
    print(sq)

    # 9
    prime = Tasks.is_prime(7)
    print(prime)
