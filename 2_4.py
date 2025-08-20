#Ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.
a1 = float(input("Anna ensimmäinen kokonaisluku: "))
a2 = float(input("Anna toinen kokonaisluku: "))
a3 = float(input("Anna kolmas kokonaisluku: "))

#Lasketaan pyydetyt arvot
summa = a1 + a2 + a3
tulo = a1 * a2 * a3
keskiarvo = (a1+a2+a3)/3

print(f"Lukujen summa on {summa}, tulo on {tulo} ja keskiarvo kahden desimaalin tarkkuudella on {keskiarvo:.2f}")