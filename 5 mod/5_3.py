# ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku. Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

# Kysytään käyttäjältä kokonaisluku
luku = int(input("Anna kokonaisluku: "))

# Oletetaan aluksi, että luku on alkuluku
on_alkuluku = True

# Alkuluvut ovat suurempia kuin 1
if luku <= 1:
    on_alkuluku = False
elif luku == 2:
    on_alkuluku = True
elif luku % 2 == 0:
    on_alkuluku = False
else:
    # Tarkistetaan jaollisuus parittomilla luvuilla 3:sta neliöjuureen asti
    for i in range(3, int(luku**0.5) + 1, 2):
        if luku % i == 0:
            on_alkuluku = False
            break

# Tulostetaan tulos
if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")