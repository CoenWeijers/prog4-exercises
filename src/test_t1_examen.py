from src.t1_examen import *

PRECISIE = 0.1


def test_mediaan_a():
    lijst = [3]
    result = mediaan(lijst)
    assert result == 3


def test_mediaan_b():
    lijst = [1, 2, 3]
    result = mediaan(lijst)
    assert result == 2


def test_mediaan_c():
    lijst = [1, 2, 3, 4]
    result = mediaan(lijst)
    assert result == 2.5


def test_mediaan_d():
    lijst = [1, 3, 3, 6, 7, 8, 9]
    result = mediaan(lijst)
    assert result == 6


def test_mediaan_e():
    lijst = [1, 2, 3, 4, 5, 6, 8, 9]
    result = mediaan(lijst)
    assert result == 4.5


def test_volume_korst():
    result = volume_korst(4, 2)
    assert abs(result - 234.57) < PRECISIE


def test_volume_korst_aarde():
    result = volume_korst(6371, 6371 - 35)
    assert abs(result - 17754362185.921997) < PRECISIE


def test_rijm_0():
    result = rijm("bon", "ton")
    assert result == True


def test_rijm_1():
    result = rijm("kan", "man")
    assert result == True


def test_rijm_2():
    result = rijm("tof", "lof")
    assert result == True


def test_rijm_3():
    result = rijm("mat", "gat")
    assert result == True


def test_rijm_4():
    result = rijm("mat", "mot")
    assert result == False


def test_rijm_5():
    result = rijm("ben", "bon")
    assert result == False


def test_rijm_6():
    result = rijm("tas", "tak")
    assert result == False


def test_zoek_rijm_0():
    woorden = ["kat", "rat", "kip", "giraf"]
    result = zoek_rijm("mat", woorden)
    assert result == ["kat", "rat"]


def test_zoek_rijm_1():
    woorden = ["kat", "rat", "kip", "giraf"]
    result = zoek_rijm("mop", woorden)
    assert result == []


def test_zoek_rijm_2():
    woorden = ["kat", "rat", "kip", "giraf"]
    result = zoek_rijm("lip", woorden)
    assert result == ["kip"]


def test_zoek_rijm_3():
    woorden = ["kat", "rat", "kip", "giraf"]
    result = zoek_rijm("laf", woorden)
    assert result == ["giraf"]


def test_tel_worpen_1_dobbelsteen_a():
    worpen = []
    result = tel_worpen_1_dobbelsteen(worpen)
    expected = {1: 0, 2: 0, 4: 0, 3: 0, 5: 0, 6: 0}
    assert result == expected


def test_tel_worpen_1_dobbelsteen_b():
    worpen = [1, 5, 2, 4, 1, 3, 5]
    result = tel_worpen_1_dobbelsteen(worpen)
    expected = {1: 2, 2: 1, 4: 1, 3: 1, 5: 2, 6: 0}
    assert result == expected


def test_tel_worpen_1_dobbelsteen_c():
    worpen = [1, 1, 1, 1, 5, 5, 5, 6, 2, 2, 2, 4, 1, 3, 5]
    result = tel_worpen_1_dobbelsteen(worpen)
    expected = {1: 5, 2: 3, 4: 1, 3: 1, 5: 4, 6: 1}
    assert result == expected


def test_tel_worpen_2_dobbelstenen_a():
    worpen = []
    result = tel_worpen_2_dobbelstenen(worpen)
    expected = {
        2: 0,
        4: 0,
        3: 0,
        5: 0,
        6: 0,
        7: 0,
        8: 0,
        9: 0,
        10: 0,
        11: 0,
        12: 0,
    }
    assert result == expected


def test_tel_worpen_2_dobbelsteen_b():
    worpen = [2, 7, 8, 9, 4, 2, 12]
    result = tel_worpen_2_dobbelstenen(worpen)
    expected = {
        2: 2,
        3: 0,
        4: 1,
        5: 0,
        6: 0,
        7: 1,
        8: 1,
        9: 1,
        10: 0,
        11: 0,
        12: 1,
    }
    assert result == expected


def test_tel_worpen_2_dobbelsteen_c():
    worpen = [
        5,
        6,
        7,
        6,
        5,
        10,
        4,
        7,
        8,
        5,
        11,
        6,
        5,
        8,
        6,
        4,
        4,
        7,
        10,
        10,
        8,
        7,
        9,
        9,
        7,
        4,
        7,
        6,
        8,
        6,
        6,
        4,
        7,
        4,
        8,
        7,
        5,
        8,
        6,
        4,
        9,
        4,
        6,
        4,
        12,
        9,
        3,
        8,
        10,
        7,
        5,
        5,
        5,
        11,
        7,
        11,
        8,
        7,
        6,
        10,
    ]
    result = tel_worpen_2_dobbelstenen(worpen)
    expected = {
        2: 0,
        3: 1,
        4: 9,
        5: 8,
        6: 10,
        7: 11,
        8: 8,
        9: 4,
        10: 5,
        11: 3,
        12: 1,
    }
    assert result == expected


def test_oppervlakte_muren():
    o = oppervlakte_muren(2, 3, 1)
    assert abs(o - 10) < PRECISIE


def test_oppervlakte_muren_kinderslaapkamer():
    o = oppervlakte_muren(4.3, 2.5, 2.85)
    assert abs(o - 38.76) < PRECISIE


def test_oppervlakte_muren_slaapkamer():
    o = oppervlakte_muren(4.3, 4, 2.85)
    assert abs(o - 47.31) < PRECISIE


def test_oppervlakte_muren_keuken():
    o = oppervlakte_muren(4.3, 7.1, 2.95)
    assert abs(o - 67.26) < PRECISIE


def test_verf_slaapkamer():
    l = verf_kamer(4.3, 2.5, 2.85, 2)
    assert abs(l - 7.752) < PRECISIE


def test_verf_living():
    l = verf_kamer(4.3, 7.1, 2.95, 2)
    assert abs(l - 13.452) < PRECISIE


HUIS_A = [
    [1, 2, 2.85],  # inkom
    [3, 2, 2.85],  # berging
    [5, 5, 2.85],  # living
    [4, 3, 2.85],  # keuken
    [4, 3, 2.85],  # slaapkamer
    [3, 3, 2.85],  # kinderslaapkamer
    [2, 2, 2.85],  # badkamer
    [0.9, 1.7, 2.85],  # toilet
    [4, 0.95, 2.85],  # gang
]

HUIS_B = [
    [1.4, 2.8, 2.85],  # inkom
    [2.15, 2.3, 2.85],  # berging
    [4.2, 7.1, 2.85],  # living
    [4.2, 7.1, 2.85],  # keuken
    [0.9, 1.7, 2.85],  # toilet 1
    [6.6, 1, 2.85],  # gang 1
    [2.2, 2.3, 2.85],  # trappenhal 2
    [1.2, 0.6, 2.85],  # kapstok
    [4.2, 4.7, 2.80],  # slaapkamer
    [4.2, 2.3, 2.80],  # kinderslaapkamer 1
    [3.1, 2.3, 2.80],  # kinderslaapkamer 2
    [4.2, 2.3, 2.80],  # kinderslaapkamer 3
    [4.2, 2.3, 2.80],  # badkamer 1
    [2.15, 2.3, 2.40],  # badkamer 2
    [0.9, 2.3, 2.40],  # toilet 2
    [6.6, 1, 2.40],  # gang 1
    [2.2, 2.3, 2.40],  # trappenhal 2
    [4.15, 7, 2.40],  # bureau
    [4.15, 7, 2.40],  # hobbyruimte
    [3.15, 2.25, 2.40],  # kelder
    [1.4, 1.65, 2.40],  # kelder
    [2.2, 2.3, 2.40],  # trappenhal 3
    [6.6, 0.95, 2.40],  # gang 3
]


def test_oppervlakte_huis_b():
    opp = oppervlakte_huis(HUIS_B)
    assert abs(opp - 235.7675) < PRECISIE


def test_oppervlakte_huis_a():
    opp = oppervlakte_huis(HUIS_A)
    assert abs(opp - 75.33) < PRECISIE


def test_verf_huis_a():
    l = verf_huis(HUIS_A, 2)
    assert abs(l - 56.487) < PRECISIE


def test_verf_huis():
    l = verf_huis(HUIS_B, 2)
    assert abs(l - 152.339) < PRECISIE


def test_teken_svg_rechthoek_a():
    result = teken_svg_rechthoek(10, 20, 30, 40)
    expected = """<rect x="10" y="20" width="30" height="40" fill="black"/>"""
    assert result == expected


def test_teken_svg_rechthoek_b():
    result = teken_svg_rechthoek(100, 320, 130, 340)
    expected = """<rect x="100" y="320" width="130" height="340" fill="black"/>"""
    assert result == expected


def test_teken_svg_tekst_a():
    result = teken_svg_tekst(10, 20, "aap")
    expected = """<text x="10" y="20" class="small">aap</text>"""
    assert result == expected


def test_teken_svg_tekst_b():
    result = teken_svg_tekst(5, 120, "haas")
    expected = """<text x="5" y="120" class="small">haas</text>"""
    assert result == expected
