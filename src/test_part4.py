import pytest

from .part4 import *


def test_addressbook_search():
    addressbook = [
        {"name": "Jan Peters", "address": "Dorpsstraat 11"},
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    assert addressbook_search(addressbook, "Jan Peters") == "Dorpsstraat 11"


def test_addressbook_search_not_found():
    addressbook = [
        {"name": "Jan Peters", "address": "Dorpsstraat 11"},
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    assert addressbook_search(addressbook, "Jan Leenders") == None


def test_addressbook_add():
    addressbook = [
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    addressbook_add(addressbook, "Jan Peters", "Dorpsstraat 11")
    assert len(addressbook) == 3
    assert {"name": "Jan Peters", "address": "Dorpsstraat 11"} in addressbook


def test_addressbook_add_duplicate(capsys):
    addressbook = [
        {"name": "Jan Peters", "address": "Dorpsstraat 11"},
        {"name": "Piet Dirkx", "address": "Kerkstraat 32"},
        {"name": "Klaas Gadeyne", "address": "Groenstraat 44"},
    ]
    addressbook_add(addressbook, "Jan Peters", "Dorpsstraat 11")
    assert len(addressbook) == 3
    assert {"name": "Jan Peters", "address": "Dorpsstraat 11"} in addressbook

    captured = capsys.readouterr()
    assert captured.out == "persoon reeds in adresboek\n"
