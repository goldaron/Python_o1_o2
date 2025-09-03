# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen.
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def heita_noppaa():
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..6."""
    # Generoidaan satunnainen kokonaisluku väliltä 1 ja 6
    return random.randint(1, 6)

while True:

    # Kutsutaan heita_noppaa-funktiota ja tallennetaan tulos muuttujaan
    silmaluku = heita_noppaa()

    # Tulostetaan heiton tulos
    print(f"Heiton tulos: {silmaluku}")

    # Tarkistetaan, onko saatu silmäluku kuutonen
    if silmaluku == 6:
        # Jos saatiin kuutonen, tulostetaan viesti ja lopetetaan silmukka
        print("Kuutonen saatu, ohjelma päättyy.")
        break