# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

def listan_summa(list):
    """Laske listan lukujen summa ja palauta summa"""
    summa = sum(list)
    return summa

lista = []

print("Anna kokonaislukuja ja laske lopuksi summa painamalla enter.")
luku = input("Anna kokonaisluku: ")

while True:
    if luku.isdigit():
        lista.append(int(luku))
        luku = input("Anna kokonaisluku: ")
    else:
        summa = listan_summa(lista)
        print(f"Listan summa: {summa}")
        print("Ohjelma päättyy.")
        break