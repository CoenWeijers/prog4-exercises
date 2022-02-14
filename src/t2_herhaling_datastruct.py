def maak_videokaart_dict(merk, naam, architectuur, geheugen, busbreedte, diesize, jaar):
    """Geef een dictionary terug met alle gegevens die als parameters aan
    de functie meegegeven werden.

    Bijvoorbeeld:
    >>> maak_videokaart_dict("NVIDIA", "RTX 3080", "Ampere", 10, 320, 628, 2020)
    {'merk': 'NVIDIA', 'naam': 'RTX 3080', 'architectuur': 'Ampere', 'geheugen': 10, 'busbreedte': 320, 'diesize': 628, 'jaar': 2020}
    """

    videokaarten = { "merk":merk,
                     "naam":naam,
                     "architectuur":architectuur,
                     "geheugen":geheugen,
                     "busbreedte":busbreedte,
                     "diesize":diesize,
                     "jaar":jaar,
                    }

    return videokaarten


def tel_videokaarten(lijst_videokaarten):
    """Geef het totaal aantal videokaarten in de lijst van videokaarten terug."""

    
    totaalvideokaarten = len(lijst_videokaarten)

    return totaalvideokaarten



def tel_videokaarten_per_merk(lijst_videokaarten):
    """Geef het aantal videokaarten per merk in de lijst van videokaarten terug.

    Het resultaat is dus een dictionary met 2 keys:
    {
        "AMD": x,
        "NVIDIA": y,
    }
    Met x het aantal AMD videokaarten in de lijst en y het aantal NVIDIA
    videokaarten in de lijst.
    """
    telleramd = 0
    tellernvidia = 0

    for videokaart in lijst_videokaarten:
        if videokaart["merk"] == "AMD":
            telleramd += 1
        if videokaart["merk"] == "NVIDIA" :
            tellernvidia +=1

    dict = {"AMD": telleramd,
                "NVIDIA": tellernvidia,
                }
        
    return dict


def grootste_videokaart(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een de naam terug
    van de grootste videokaart.

    Bijvoorbeeld:
    >>> grootste_videokaart([{'naam': 'RTX 3080', 'diesize': 628}])
    'RTX 3080'
    """
    grootste = 0
    naamgrootestekaart = None
    for videokaart in lijst_videokaarten:
        if videokaart["diesize"] >= grootste:
            grootste = videokaart["diesize"]
            naamgrootestekaart = videokaart["naam"]    
    return naamgrootestekaart





def grootste_videokaartgrootte_per_merk(lijst_videokaarten):
    """Gegeven een lijst met videokaarten, geef je een dictionary terug met
    voor ieder merk de omvang van de grootste kaart.

    Bijvoorbeeld:
    >>> grootste_videokaartgrootte_per_merk([{'merk': 'NVIDIA', 'naam': 'RTX 3080', 'diesize': 628}])
    {'AMD': 0, 'NVIDIA': 628}
    """
    grootte = {'AMD': 0, 'NVIDIA' : 0}
    
    for videokaart in lijst_videokaarten:
        if videokaart["merk"] == "AMD":
            if videokaart["diesize"] > grootte["AMD"]:
                grootte["AMD"] = videokaart["diesize"]

        if videokaart["merk"] == "NVIDIA":
            if videokaart["diesize"] > grootte['NVIDIA']:
                grootte["NVIDIA"] = videokaart["diesize"]
    
    return grootte



def diesizes_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over vidoekaarten,
    geef je een lijst van diesizes terug.

    Bijvoorbeeld:
    >>> diesizes_videokaarten([{"diesize": 500}, {"diesize": 300}])
    [500, 300]
    """

    diesizes = []
    
    for GPU in lijst_videokaarten:
        die = GPU['diesize']
        diesizes.append(die)
        
    return diesizes


def gemiddelde_diesize_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je de gemiddelde diesize terug.

    Bijvoorbeeld:
    >>> gemiddelde_diesize_videokaarten([{"diesize": 500}, {"diesize": 300}])
    400.0
    """
    som = 0
    for GPU in lijst_videokaarten:
        som += GPU["diesize"]
        gem = som/len(lijst_videokaarten)

    return gem




def jaren_videokaarten(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van jaartalen terug waarin de videokaarten uitgebracht werden.

    Bijvoorbeeld:
    >>> jaren_videokaarten([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}])
    [2020, 2021]
    """
    jaar = []

    for GPU in lijst_videokaarten:
        jaartal = GPU["jaar"]
        jaar.append(jaartal)
    return jaar




def videokaarten_voor_jaar(lijst_videokaarten, jaar):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een lijst van dictionaries terug met informatie over videokaarten
    voor het opgegeven jaar.

    Bijvoorbeeld:
    >>> videokaarten_voor_jaar([{"jaar": 2020, "diesize": 500}, {"jaar": 2021, "diesize": 300}], 2020)
    [{'jaar': 2020, 'diesize': 500}]
    """


def grootste_geheugen_per_jaar(lijst_videokaarten):
    """Gegeven een lijst van dictionaries met informatie over videokaarten,
    geef je een dictionary terug met de grootste geheugengrootte per jaar.

    Bijvoorbeeld:
    >>> grootste_geheugen_per_jaar([{"jaar": 2020, "geheugen": 4}, {"jaar": 2021, "geheugen": 8}])
    {2020: 4, 2021: 8}
    """
    GPUjaar = []
    for GPU in lijst_videokaarten:
        if GPU["jaar"] == jaar:
            GPUjaar.append(GPU)
    return GPUjaar
