import csv
from math import pi
import statistics



def mediaan(lijst):
    """Schrijf een functie die de mediaan berekent van een lijst getallen.
    >>> mediaan([4,8,12])
    8

    >>> mediaan([4,8,10,12])
    9.0
    """
    
    result = statistics.median(lijst)
    return result

    


def volume_korst(R, r):
    """Schrijf een functie die het volume van de korst van een bol berekent.
    R is de straal van de buitenkant van de bol. r is de straal van
    de binnenkant.
    >>> volume_korst(3, 1)
    108.90854532444617
    """


    V = 4/3*pi*R**3
    v = 4/3*pi *r**3
    result = V-v
    return result


def rijm(woord1, woord2):
    """Schrijf een functie die controlleert of twee woorden eindigen op dezelfde twee letters.

    >>> rijm("kat", "rat")
    True
    >>> rijm("kip", "lip")
    True
    >>> rijm("kip", "kat")
    False
        """
    if woord1[:-1] == woord2[:-1]:
        result = True

    if woord1[:-2] == woord2[:-2]:
         result = False

    else: result = False    

    return result


def zoek_rijm(zoekterm, woorden):
    """Maakt een nieuwe lijst met enkel de woorden die rijmen op zoekterm.

    >>> zoek_rijm("kip", ["lip","tip","kat","aap"])
    ['lip', 'tip']
    """
    woorden = []


    pass


def tel_worpen_1_dobbelsteen(worpen):
    """Geef een dictionary terug met voor elk aantal ogen het aantal keer dat het
    gegooid werd, indien telkens met 1 dobbelsteen gegooid werd.

    >>> tel_worpen_1_dobbelsteen([1, 1, 3, 4, 5, 5])
    {1: 2, 2: 0, 3: 1, 4: 1, 5: 2, 6: 0}
    """


    pass


def tel_worpen_2_dobbelstenen(worpen):
    """Geef een dictionary terug met voor elk aantal ogen het aantal keer dat het
    gegooid werd indien telkens 2 dobbelstenen gegooid worden.

    >>> tel_worpen_2_dobbelstenen([2, 3, 4, 5, 5, 7, 8, 8, 12])
    {2: 1, 3: 1, 4: 1, 5: 2, 6: 0, 7: 1, 8: 2, 9: 0, 10: 0, 11: 0, 12: 1}
    """
    pass


def oppervlakte_muren(lengte, breedte, hoogte):
    """Berekent de oppervlakte van de muren van een kamer met opgegeven afmetingen.

    >>> oppervlakte_muren(4, 5, 2.5)
    45.0
    >>> oppervlakte_muren(4, 7, 3)
    66
    """
    result = (lengte*hoogte)*2 + (hoogte*breedte)*2

    return result



def verf_kamer(lengte, breedte, hoogte, lagen):
    """Berekent de hoeveelheid verf die je nodig hebt om een kamer met opgegeven
    afmetingen te verven. De parameter laag geeft aan hoeveel lagen verf je aan
    zal brengen (dus hoeveel keer je de muren verft).

    Je kan met 1 liter verf 10 vierkante meter muur verven /10.

    >>> verf_kamer(4, 5, 2.5, 1)
    4.5
    >>> verf_kamer(4, 5, 2.5, 2)
    9.0
    >>> verf_kamer(4, 7, 3, 1)
    6.6
    """
    result = (((lengte*hoogte)*2)*lagen)/10 + (((hoogte*breedte)*2)*lagen)/10

    return result


def oppervlakte_huis(kamers):
    """Berekent de oppervlakte van alle kamers van een huis.

    >>> oppervlakte_huis([[4,2,3]])
    8
    >>> oppervlakte_huis([[4,2,3], [5,5,3]])
    33
    """
    #kamerseen = kamers[:0]*kamer
#    result = 
    # return result


def verf_huis(kamers, lagen):
    """Berekent de hoeveelheid verf die je nodig hebt om een huis met de opgegeven
    kamers te verven. 'kamers' is een lijst met afmetingen van de kamers van een
    huis.

    >>> verf_huis([[4, 5, 2.5], [4, 7, 3]], 1)
    11.1
    >>> verf_huis([[4, 5, 2.5], [4, 7, 3]], 2)
    22.2
    """
    pass


def teken_svg_rechthoek(x, y, width, height, fill="black"):
    """Teken een SVG rechthoek met gegeven afmetingen.

    >>> teken_svg_rechthoek(0, 10, 300, 200, fill="red")
    '<rect x="0" y="10" width="300" height="200" fill="red"/>'
    """
    result = f'<rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{fill}"/>'
    return result


def teken_svg_tekst(x, y, text):
    """Teken SVG text met gegeven tekst op de gegeven positie.

    >>> teken_svg_tekst(0, 10, "konijn")
    '<text x="0" y="10" class="small">konijn</text>'
    """

    result = f'<text x="{x}" y="{y}" class="small">{text}</text>'
    return result

COUNTRIES = [
    "Venezuela",
    "North Korea",
    "Australia",
    "USA",
    "Taiwan",
    "Spain",
    "Panama",
    "Mexico",
    "South Korea",
    "Russia",
    "UAE",
    "Germany",
    "Turkey",
    "South Africa",
    "Indonesia",
    "Bahrain",
    "UK",
    "Israel",
    "Austria",
    "Poland",
    "Thailand",
    "Philippines",
    "China",
    "Japan",
    "Canada",
    "Netherlands",
    "Singapore",
    "Belgium",
    "Saudi Arabia",
    "Malaysia",
    "Kuwait",
    "Qatar",
]


def maak_kleuren(data):
    """Maakt voor ieder element in de lijst 'data' een verschillende kleur.
    De rood en groen componenten van de de kleur komen overeen met het volgnummer
    in de lijst maal 10. De blauwe component van de kleur komt overeen met de lengte
    van het woord maal 25.

    Dus, "os" zou als groen component 50 krijgen omdat de lengte van het woord 2
    is.

    >>> maak_kleuren(["konijn", "kip"])
    {'konijn': 'rgb(10,10,150)', 'kip': 'rgb(20,20,75)'}
    >>> maak_kleuren(["kip", "konijn", "aap"])
    {'kip': 'rgb(10,10,75)', 'konijn': 'rgb(20,20,150)', 'aap': 'rgb(30,30,75)'}
    """
    return {}


COLORS = maak_kleuren(COUNTRIES)


def maak_grafiek_gebouwen_hoogtes_landkleurcodes_sv(input_filename, output_filename):
    """Maak een grafiek door het CSV bestand 'input_filename' te lezen.
    Dit bestand informatie over de 100 hoogste gebouwen ter wereld.
    Iedere regel in dit bestand bevat:
    1. de range-nummer
    2. de naam van het gebouw
    3. de stad waarin het gebouw staat
    4. het land waarin het gebouw staat
    5. de hoogte van het gebouw in meters
    6. het aantal verdiepingen in het gebouw
    7. het jaartal waarin het gebouw klaar was

    Voer volgende deelopdrachten uit:
    A. In het bestand 'output_filename' maak je een SVG met 1 rechthoek
    per gebouw. De breedte van iedere rechthoek komt overeen met de hoogte
    van het gebouw. De hoogte van iedere rechthoek is vast: 8. Gebruik hiervoor
    je eerder gemaakte 'teken_svg_rechthoek' functie. Maak de rechthoeken
    telkens rood ('red').

    B. Gebruik de COLORS dictionary om de kleuren van de rechthoeken te laten
    overeenkomen met de landen. Zo krijgen bijvoorbeeld alle gebouwen in China
    telkens dezelfde kleur in de grafiek.

    C. Schrijf bij iedere rechthoek de naam van het land.

    D. Schrijf bij iedere rechthoek de naam van het gebouw en het bouwjaar.
    """

    # De 'header' en 'footer' van het SVG bestand krijg je reeds:
    # Deze SVG-header schrijf je als eerste naar je SVG bestand.
    header = """<svg viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
    <style>
    .small { font: italic 8px sans-serif;dominant-baseline:hanging; }
    </style>
    <rect x="0" y="0" width="1000" height="1000" fill="lightgrey"/>
    """

    # Maak hier een SVG-bestand.
    # Lees hier regel voor regel uit je CSV bestand.
    # Schrijf telkens een rechthoek naar je SVG-bestand.

    # En voor deel C en D, schrijf je hier ook telkens tekst.

    # Deze SVG-footer schrijf je als laatste naar je SVG bestand.
    footer = "</svg>"


# Maak een Django project met naam gebouwen
# Maak hierin een app met naam buildings
# In deze app maak je een model om informatie over gebouwen bij te houden
#
# Je voorziet per gebouw de volgende velden:
# - naam
# - stad
# - land
# - hoogte
# - aantal verdiepingen
# - bouwjaar
#
# Voer via de admin de eerste 5 gebouwen uit de CSV in.
#
# Zorg dat je in de admin in het lijstoverzicht de volgende kolommen ziet:
# naam, land, hoogte, bouwjaar
#
# Zorg dat je via de admin kan zoeken op land.


if __name__ == "__main__":
    maak_grafiek_gebouwen_hoogtes_landkleurcodes_sv("gebouwen.csv", "gebouwen.svg")
