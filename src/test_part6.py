import pytest

from .part6 import *


def test_find_problematic_scores():
    puntenlijst = [7, 4, 8, 2, 9, 8]
    assert find_problematic_scores(puntenlijst) == 2


def test_find_problematic_scores_none():
    puntenlijst = [7, 9, 8, 7, 9, 8]
    assert find_problematic_scores(puntenlijst) == 0


def test_count_ice_cream_flavors_empty():
    ice_creams = []
    expected = {
        "vanille": 0,
        "chocolade": 0,
        "banaan": 0,
        "aardbei": 0,
    }
    assert count_ice_cream_flavors(ice_creams) == expected


def test_count_ice_cream_flavors():
    ice_creams = [
        "vanille",
        "chocolade",
        "vanille",
        "vanille",
        "vanille",
        "vanille",
        "banaan",
        "chocolade",
        "vanille",
        "chocolade",
        "aardbei",
        "banaan",
    ]
    expected = {
        "vanille": 6,
        "chocolade": 3,
        "banaan": 2,
        "aardbei": 1,
    }
    assert count_ice_cream_flavors(ice_creams) == expected


def test_count_words_zero():
    text = """"""

    assert count_words(text) == 0


def test_count_words_3():
    text = "The Dunwich Horror"

    assert count_words(text) == 3


def test_count_words():
    text = """Above the waist it was semi-anthropomorphic though its chest, where
the dogs rending paws still rested watchfully, had the leathery,
reticulated hide of a crocodile or alligator. The back was piebald
with yellow and black, and dimly suggested the squamous covering of
certain snakes. Below the waist, though, it was the worst for here
all human resemblance left off and sheer fantasy began. The skin was
thickly covered with coarse black fur, and from the abdomen a score of
long greenish-gray tentacles with red sucking mouths protruded limply."""

    assert count_words(text) == 88


def test_count_word_frequency_zero():
    text = """"""

    assert count_word_frequency(text) == {}


def test_count_word_frequency_3():
    text = "The Dunwich Horror"

    expected = {
        "The": 1,
        "Dunwich": 1,
        "Horror": 1,
    }
    assert count_word_frequency(text) == expected


def test_count_word_frequency():
    text = """Above the waist it was semi-anthropomorphic though its chest, where
the dogs rending paws still rested watchfully, had the leathery,
reticulated hide of a crocodile or alligator. The back was piebald
with yellow and black, and dimly suggested the squamous covering of
certain snakes. Below the waist, though, it was the worst for here
all human resemblance left off and sheer fantasy began. The skin was
thickly covered with coarse black fur, and from the abdomen a score of
long greenish-gray tentacles with red sucking mouths protruded limply."""

    result = count_word_frequency(text)
    assert result["a"] == 2
    assert result["and"] == 4
    assert result["crocodile"] == 1
    assert result["it"] == 2
    assert result["of"] == 3
    assert result["the"] == 7
    assert result["The"] == 2
    assert result["Above"] == 1


def test_count_word_frequency_nocase():
    text = """Above the waist it was semi-anthropomorphic though its chest, where
the dogs rending paws still rested watchfully, had the leathery,
reticulated hide of a crocodile or alligator. The back was piebald
with yellow and black, and dimly suggested the squamous covering of
certain snakes. Below the waist, though, it was the worst for here
all human resemblance left off and sheer fantasy began. The skin was
thickly covered with coarse black fur, and from the abdomen a score of
long greenish-gray tentacles with red sucking mouths protruded limply."""

    result = count_word_frequency_nocase(text)
    assert result["a"] == 2
    assert result["and"] == 4
    assert result["crocodile"] == 1
    assert result["it"] == 2
    assert result["of"] == 3
    assert result["the"] == 9
    assert result["above"] == 1
