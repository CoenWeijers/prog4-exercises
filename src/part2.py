from math import pi, sqrt

# Your exercises should appear in this file.


def oppervlakte_kegel(r, h):
    # Zoek via Google naar "area cone"
    # l = vierkantswortel(r^2 + h^2)
    # A = π * r * l + π * r^2
    l = sqrt(r**2 + h**2)
    return pi * r * l + pi * r**2


def last_element(l):
    """Return het laatste element uit een lijst"""
    
    return l[-1]


def sum_of_list(l):
    """Return de som van alle elementen uit een lijst"""
    return sum(l)


def average_of_list(l):
    """Return het gemiddelde van alle elementen uit een lijst"""
    
    return sum(l) / len(l)

def min_max_of_list(l):
    """Return het minimum en het maximum van de elementen uit een lijst"""
    return min(l) , max(l) 



def squared_list(l):
    """Return een nieuwe lijst met de kwadraten van de elementen uit de gegeven lijst

    squared_list([2,3]) == [4, 9]
    """
    n = [x**2 for x in (l)]
    return n

def differences_list(l1, l2):
   
    result = []
    for i in zip(l1,l2):
    
         l3 = (i[0]-i[1])
         result.append(l3)

    return result

def replace_takis_mr_issaris(text):

    text = text.replace('Takis', 'Mr. Issaris') 

    return text