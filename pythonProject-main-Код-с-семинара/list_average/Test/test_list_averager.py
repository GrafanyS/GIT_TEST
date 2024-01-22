from list_average import ListAverage
import pytest

first_list = [2, 5, 25, 8, 3, 13, 9, 23, 4, 1]  # среднее значение 9.3
second_list = [78, 3, 8, 22, 6, 9, 15, 88, 1, 10]  # среднее значение 24


class TestListAverage(object):
    def test_init(self):
        """Проверка корректной инициализации класса."""
        nums_list = ListAverage.ListAverage(first_list, second_list)
        assert nums_list.first_list == first_list
        assert nums_list.second_list == second_list

    def test_first_list(self):
        la = ListAverage.ListAverage(first_list, second_list)
        assert sorted(first_list) == sorted(la.first_list)

    def test_second_list(self):
        la = ListAverage.ListAverage(first_list, second_list)
        assert sorted(second_list) == sorted(la.second_list)

    def test_average_first_list(self):
        la = ListAverage.ListAverage(first_list, second_list)
        assert format(la.average_first_list, '1f') == format(9.3, '1f')

    def test_average_second_list(self):
        la = ListAverage.ListAverage(first_list, second_list)
        assert la.average_second_list == 24

    def test_get_lists_averages(self):
        """Проверка средних значений списков размером больше 1."""
        nums_list = ListAverage.ListAverage(first_list, second_list)
        assert nums_list.get_lists_averages == (9.3, 24)

    def test_first_average_more(self, capfd):
        """Проверка сообщения когда среднее значение первого списка больше второго."""
        nums_list = ListAverage.ListAverage(second_list, first_list)
        nums_list.compare_averages()
        captured = capfd.readouterr()
        assert captured.out.strip() == 'Первый список имеет большее среднее значение.'

    def test_second_average_more(self, capfd):
        """Проверка сообщения когда среднее значение второго списка больше первого."""
        nums_list = ListAverage.ListAverage(first_list, second_list)
        nums_list.compare_averages()
        captured = capfd.readouterr()
        assert captured.out.strip() == 'Второй список имеет большее среднее значение.'

    def test_equal_averages(self, capfd):
        """Проверка сообщения когда средние значения списков равны."""
        nums_list = ListAverage.ListAverage(first_list, first_list)
        nums_list.compare_averages()
        captured = capfd.readouterr()
        assert captured.out.strip() == 'Средние значения равны.'

    @pytest.mark.parametrize("first_list1, second_list2, result", [([1, 2, 3], [], (2, 0)),
                                                                   ([], [1, 2, 3], (0, 2)), ([], [], (0, 0))])
    def test_get_empty_lists_averages(self, first_list1, second_list2, result):
        """Проверка средних значений, если один или оба списка пустые."""
        nums_list = ListAverage.ListAverage(first_list1, second_list2)
        assert nums_list.get_lists_averages == result

    @pytest.mark.parametrize("first_list1, second_list2, result", [([1, 2, 3], [5], (2, 5)),
                                                                   ([5], [1, 2, 3], (5, 2)), ([5], [5], (5, 5))])
    def test_get_one_element_lists_averages(self, first_list1, second_list2, result):
        """Проверка средних значений, если один или оба списка имеют только один элемент."""
        nums_list = ListAverage.ListAverage(first_list1, second_list2)
        assert nums_list.get_lists_averages == result
