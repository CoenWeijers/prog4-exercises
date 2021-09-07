import pytest

from .part3 import *


def test_list_search_1():
    data = [
        "Jan",
        "Piet",
        "Klaas",
    ]
    assert list_search(data, "Piet") == 1


def test_list_search_2():
    data = [
        "Jan",
        "Piet",
        "Klaas",
    ]
    assert list_search(data, "Klaas") == 2


def test_phonebook_search():
    phonebook = [
        ["Jan Peters", "+32 470 998301"],
        ["Piet Dirkx", "+32 483 313220"],
        ["Klaas Gadeyne", "+32 453 231456"],
    ]
    assert phonebook_search(phonebook, "Klaas Gadeyne") == "+32 453 231456"


def test_phonebook_search_not_found():
    phonebook = [
        ["Jan Peters", "+32 470 998301"],
        ["Piet Dirkx", "+32 483 313220"],
        ["Klaas Gadeyne", "+32 453 231456"],
    ]
    assert phonebook_search(phonebook, "Herman Bruyninckx") == None


def test_phonebook_empty_add():
    phonebook = []
    phonebook_add(phonebook, "Jan", "123")

    assert phonebook == [["Jan", "123"]]


def test_phonebook_add():
    phonebook = [
        ["Pieter", "456"],
    ]
    phonebook_add(phonebook, "Jan", "123")

    expected = [
        ["Pieter", "456"],
        ["Jan", "123"],
    ]
    assert phonebook == expected


def test_phonebook_add_duplicate(capsys):
    phonebook = [
        ["Pieter", "456"],
    ]
    phonebook_add(phonebook, "Pieter", "456")

    expected = [
        ["Pieter", "456"],
    ]
    assert phonebook == expected

    captured = capsys.readouterr()
    assert captured.out == "data reeds in telefoonboek\n"


def test_phonebook_add_duplicate_name(capsys):
    phonebook = [
        ["Pieter", "456"],
    ]
    phonebook_add(phonebook, "Jan", "456")

    expected = [
        ["Pieter", "456"],
    ]
    assert phonebook == expected

    captured = capsys.readouterr()
    assert captured.out == "ander persoon met deze nummer in telefoonboek\n"


def test_phonebook_remove_not_found(capsys):
    phonebook = [
        ["Pieter", "456"],
    ]
    phonebook_remove(phonebook, "Jan", "123")

    expected = [
        ["Pieter", "456"],
    ]
    assert phonebook == expected

    captured = capsys.readouterr()
    assert captured.out == "persoon niet gevonden in telefoonboek\n"


def test_phonebook_remove_entry(capsys):
    phonebook = [
        ["Pieter", "456"],
        ["Klaas", "111"],
        ["Jan", "123"],
    ]
    phonebook_remove(phonebook, "Jan", "123")

    expected = [
        ["Pieter", "456"],
        ["Klaas", "111"],
    ]
    assert phonebook == expected


def test_phonebook_print_empty(capsys):
    phonebook = []
    phonebook_print(phonebook, "Jan")

    captured = capsys.readouterr()
    assert captured.out == "niets gevonden\n"


def test_phonebook_print(capsys):
    phonebook = [
        ["Pieter", "456"],
        ["Klaas", "111"],
        ["Jan", "123"],
    ]
    phonebook_print(phonebook, "Jan")

    captured = capsys.readouterr()
    assert captured.out == "123\n"


def test_phonebook_print_multiple(capsys):
    phonebook = [
        ["Pieter", "456"],
        ["Klaas", "111"],
        ["Jan", "123"],
        ["Jan", "124"],
    ]
    phonebook_print(phonebook, "Jan")

    captured = capsys.readouterr()
    assert captured.out == "123\n124\n"
