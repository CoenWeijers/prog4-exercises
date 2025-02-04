from datetime import date

# Schrijf voor onderstaande oefeningen eerst de testen in test_part_tdd.py
# Implementeer ze vervolgens in dit bestand.

# Oefening 1
# ==========
# Schrijf een functie palindroom, die controlleert of een bepaalde string
# een palindroom is.
# > palindroom("lol")
# True
def palindroom(x):
    mirrored = x[::-1]
    if mirrored == x:
        return True
    return False

# Oefening 2
# ==========
# Schrijf een functie anagram, die controlleert of een twee gegeven woorden
# anagrammen zijn van elkaar.
# > anagram("lol", "lot")
# False
# > anagram("tol", "lot")
# True
def anagram(first, second):
    sorted1 = sorted(first)
    sorted2 = sorted(second)
    if sorted1 == sorted2:
        return True
    else: 
        return False

# Oefening 3
# ==========
# Schrijf een functie leeftijd, die gegeven een datum, je leeftijd in jaren
# teruggeeft:
# > leeftijd(1976, 12, 20)
# 44
# > leeftijd(1976, 2, 10)
# 45
# 
# Tip: Gebruik de datetime module:
# datetime.date.now() geeft de huidige datum
# datetime.date.date(year=2021, month=1, day=1) stelt 1 januari voor
# Je kan data van elkaar aftrekken.
def age(year, month, day):
    today = date.today()
    age = today.year - year
    if month == today.month:
        if day > today.day:
            age -= 1
    elif month > today.month:
        age -= 1
    return age