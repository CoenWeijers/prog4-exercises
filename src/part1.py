# Your exercises should appear in this file.


def add(x, y):
    return x + y


def kwadraat(x):
    """Return het kwadraat van x"""
    return x**2


def oppervlakte_kubus(z):
    """Return de oppervlakte van een kubus met zijde z"""
    return z*z*6


def seconds_in_days(days=1):
    """Geef het aantal seconden in het opgegeven aantal dagen

    Als er geen parameter doorgegeven wordt, geef dan het aantal
    seconden in 1 dag terug.
    """
    return days*24*3600


def seconds_in_weeks(weeks):
    """Return het aantal seconden in 'week' weken."""
    return weeks*7*24*3600


def seconds_in_years(years):
    """Return het aantal seconden in 'years' jaren.

    Veronderstel dat ieder jaar uit exact 52 weken bestaat.
    """
    return 3600 * 24 * 7 * 52 * years


def seconds_remaining_in_life(age, is_female=False):
    """Return het aantal seconden dat overblijft in je leven.

    Ga uit van een maximale levensduur van 80 jaren voor mannen,
    en 84 jaren voor vrouwen.
    """
    if is_female == True:
       f =  3600 * 24 * 7 * 52 * (84 - age)
    else:
         f =  3600 * 24 * 7 * 52 * (80 - age)
    return f


def postcodes():
    """Return een dictionary met postcodes"""
    if v == postcode(3650)
    return "Dilsen-Stokkem"



def oneven_getallen(x):
    """Return een lijst met de eerste 'x' oneven getallen."""
    return []