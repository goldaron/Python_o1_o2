# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
# paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
# jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def karsi(list):
    """Köydöön käyttäjän antama lista läpi karsitaan listasta kaikki parittomat luvut,
    eli jakojäännös/modulo % 2 ei mene tasan ja lisätään ne uuteen listaan."""
    uusi = []
    for n in list:
        if n % 2 != 0:
            uusi.append(n)
    return uusi

org = []

print("Listaa lukuja, karsi lista painamalla enter.")
luku = input("Anna kokonaisluku: ")

while True:
    if luku.isdigit():
        org.append(int(luku))
        luku = input("Anna kokonaisluku: ")
    else:
        new = karsi(org)
        print(f"Alkuperäinen lista: {org} \nKarsittu lista: {new}")
        print("Ohjelma päättyy.")
        break