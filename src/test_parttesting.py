# Schrijf testen voor de functies die je in part_testing.py vindt.
from .part_testing import bmi, maximum, pythagoras


def test_maximum():
    assert maximum(4, 5) == 9



def test_maximum():
    assert maximum(2000, 5 ) == 2000



def test_bmi():
    m = bmi(81, 1.83)
    assert abs(m - 24) < 0.5

def test_bmi2():
    m = bmi(81, 0)
    assert abs(m - 24) < 0.5


def test_pythagoras():
    schuinezijde = pythagoras(3, 4)
    assert schuinezijde == 5

def test_pythagoras2():
    schuinezijde = pythagoras(3, 4)
    assert schuinezijde == 5



