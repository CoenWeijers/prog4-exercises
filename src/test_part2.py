import pytest

from src.part1 import oppervlakte_kubus

from .part2 import *


def test_oppervlakte_kegel_1_2():
    result = oppervlakte_kegel(1, 2)
    expected = 10.17

    assert abs(result - expected) < 0.1


def test_oppervlakte_kegel_4_5():
    result = oppervlakte_kegel(4, 5)
    expected = 130.73

    assert abs(result - expected) < 0.1


def test_last_element():
    result = last_element([3])
    assert result == 3


def test_last_element_5():
    result = last_element([1, 2, 3, 4, 5])
    assert result == 5


def test_sum_of_list_empty():
    result = sum_of_list([])
    assert result == 0


def test_sum_of_list():
    result = sum_of_list([1, 2, 3])
    assert result == 6


def test_average_of_list_3():
    result = average_of_list([1, 2, 3])
    assert result == 2


def test_average_of_list_2():
    result = average_of_list([4, 40])
    assert result == 22


def test_min_max_of_list():
    result = min_max_of_list([1, 2, 3])
    assert result == (1, 3)


def test_min_max_of_list_eq():
    result = min_max_of_list([3, 3])
    assert result == (3, 3)


def test_squared_list_empty():
    result = squared_list([])
    assert result == []


def test_squared_list_1():
    result = squared_list([4])
    assert result == [16]


def test_squared_list_2():
    result = squared_list([4, 6])
    assert result == [16, 36]


def test_differences_list_empty():
    l1 = []
    l2 = []
    result = differences_list(l1, l2)
    assert result == []


def test_differences_list_3():
    l1 = [2, 3, 4]
    l2 = [1, 1, 1]
    result = differences_list(l1, l2)
    assert result == [1, 2, 3]


def test_differences_list_5():
    l1 = [2, 3, 4, 99, 0]
    l2 = [0, 3, 1, 99, -1]
    result = differences_list(l1, l2)
    assert result == [2, 0, 3, 0, 1]


def test_replace_takis_mr_issaris_1():
    text = "Dag Takis, ik kreeg mijn taken helaas niet afgewerkt... "
    result = replace_takis_mr_issaris(text)
    assert result == "Dag Mr. Issaris, ik kreeg mijn taken helaas niet afgewerkt... "


def test_replace_takis_mr_issaris_2():
    text = "Beste Takis, ik vond de oefeningen echt geweldig!"
    result = replace_takis_mr_issaris(text)
    assert result == "Beste Mr. Issaris, ik vond de oefeningen echt geweldig!"
