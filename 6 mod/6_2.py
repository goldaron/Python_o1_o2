# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku,
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

tahkot = int(input("Montako sivuista noppaa heitetään? "))

def heita_noppaa():
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..tahkot."""
    # Generoidaan satunnainen kokonaisluku väliltä 1 ja tahkot
    return random.randint(1, tahkot)

while True:

    # Kutsutaan heita_noppaa-funktiota ja tallennetaan tulos muuttujaan
    silmaluku = heita_noppaa()

    # Tulostetaan heiton tulos
    print(f"Heiton tulos: {silmaluku}")

    # Tarkistetaan, onko saatu silmäluku annettu luku
    if silmaluku == tahkot:
        # Jos saatiin maksimiluku, tulostetaan viesti ja lopetetaan silmukka
        print(f"{tahkot} saatu, ohjelma päättyy.")
        break