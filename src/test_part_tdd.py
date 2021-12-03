# Schrijf hier testen voor je oefeningen.
# Begin iedere testfunctie met naam "test_" gevolgd door de
# naam van de functie die je gaat testen, gevold door 
# een naam die aangeeft wat je gaat testen.
# 
# B.v.
# Om een functie "kwadraat" te testen, kan je als eerste test
# een functie met naam "test_kwadraat_2" die test dat het
# kwadraat van 2 4 is.
import pytest
from .part_tdd import *

def test_palindroom1():
    result = palindroom("lol")
    assert result == True

def test_palindroom2():
    result = palindroom("Programmeren")
    assert result == False



def test_anagram1():
    result = anagram("nee", "wow")
    assert result == False

def test_anagram2():
    result = anagram("wow", "wow")
    assert result == True

def test_anagram3():
    result = anagram("kikker", "rekkik")
    assert result == True



def test_age1():
    result = age(2004, 12, 3)
    assert result == 16

def test_age2():
    result = age(1966, 4, 16)
    assert result == 55

