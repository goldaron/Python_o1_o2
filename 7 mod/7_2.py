# Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
# Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
# syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
# mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

nimet = set()  # Luodaan tyhjä joukko nimien tallentamiseen

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break  # Lopetetaan, jos syöte on tyhjä

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)  # Lisätään nimi joukkoon

print("\nSyötetyt nimet:")
for nimi in nimet:
    print(nimi)