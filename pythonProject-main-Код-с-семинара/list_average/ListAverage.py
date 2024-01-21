from statistics import mean
from typing import List


class ListAverage:
    """Класс для сравнения средних значений двух списков."""

    def __init__(self, first_list: list[int | float], second_list: list[int | float]) -> None:
        """
        Инициализирует экземпляр класса двумя списками.

        Параметры:
            first_list (list[int | float]): Первый список.
            second_list (list[int | float]): Второй список.
        """
        self.__first_list: List = first_list
        self.__second_list: List = second_list
        self.__average_first_list = None
        self.__average_second_list = None

    @property
    def first_list(self) -> List:
        return self.__first_list

    @property
    def second_list(self) -> List:
        return self.__second_list

    @property
    def average_first_list(self) -> float | int:
        if self.__average_first_list is None:
            self.__average_first_list = mean(self.__first_list)
        return self.__average_first_list

    @property
    def average_second_list(self) -> float | int:
        if self.__average_second_list is None:
            self.__average_second_list = mean(self.__second_list)
        return self.__average_second_list

    """Класс для сравнения средних значений двух списков."""

    @property
    def get_lists_averages(self) -> tuple[float | int, float | int]:
        """
        Вычисляет и возвращает средние значения двух списков.

        Возвращает:
            tuple[float, float]: Кортеж, содержащий среднее значение `lst1` и `lst2`.
        """
        avg1 = 0
        if self.__first_list:
            avg1 = sum(self.__first_list) / len(self.__first_list)

        avg2 = 0
        if self.__second_list:
            avg2 = sum(self.__second_list) / len(self.__second_list)

        return avg1, avg2

    def compare_averages(self) -> None:
        """
        Сравнивает средние значения двух списков и выводит результат.

        Этот метод вычисляет средние значения двух списков с помощью метода `get_lists_averages`
        и сравнивает их. Если среднее значение первого списка больше среднего значения второго
        списка, он выводит 'Первый список имеет большее среднее значение'. Если среднее значение
        первого списка меньше среднего значения второго списка, он выводит 'Второй список имеет
        большее среднее значение'. Если средние значения равны, он выводит 'Средние значения равны'.

        Параметры:
            self (ClassName): Экземпляр класса.

        Возвращает:
            None: Этот метод ничего не возвращает.
        """
        avg1, avg2 = self.get_lists_averages
        if avg1 > avg2:
            print('Первый список имеет большее среднее значение.')
        elif avg1 < avg2:
            print('Второй список имеет большее среднее значение.')
        else:
            print('Средние значения равны.')
