# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina
# ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
# Yksi gallona on 3,785 litraa.

def muunnos():
    """Muutetaan käyttäjän antamat gallonat litroiksi."""
    litrat = gallonat * 3.785
    return litrat


gallonat = float(input("Gallonat: "))

while gallonat > 0:

    litrat = muunnos()

    print(f"{gallonat} gallonaa on {litrat:.2f} litraa.")
    gallonat = float(input("Gallonat: "))