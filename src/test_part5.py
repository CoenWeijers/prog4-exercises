import pytest

from .part5 import *


def test_addressbook_search():
    addressbook = {
        "Jan Peters": "Dorpsstraat 11",
        "Piet Dirkx": "Kerkstraat 32",
        "Klaas Gadeyne": "Groenstraat 44",
    }
    assert addressbook_search(addressbook, "Jan Peters") == "Dorpsstraat 11"


def test_addressbook_search_not_found():
    addressbook = {
        "Jan Peters": "Dorpsstraat 11",
        "Piet Dirkx": "Kerkstraat 32",
        "Klaas Gadeyne": "Groenstraat 44",
    }
    assert addressbook_search(addressbook, "Jan Leenders") == None


def test_addressbook_add():
    addressbook = {
        "Piet Dirkx": "Kerkstraat 32",
        "Klaas Gadeyne": "Groenstraat 44",
    }
    addressbook_add(addressbook, "Jan Peters", "Dorpsstraat 11")
    assert "Jan Peters" in addressbook
    assert addressbook["Jan Peters"] == "Dorpsstraat 11"


def test_addressbook_add_duplicate(capsys):
    addressbook = {
        "Jan Peters": "Dorpsstraat 11",
        "Piet Dirkx": "Kerkstraat 32",
        "Klaas Gadeyne": "Groenstraat 44",
    }
    addressbook_add(addressbook, "Jan Peters", "Dorpsstraat 11")
    assert "Jan Peters" in addressbook
    assert addressbook["Jan Peters"] == "Dorpsstraat 11"

    captured = capsys.readouterr()
    assert captured.out == "persoon reeds in adresboek\n"
