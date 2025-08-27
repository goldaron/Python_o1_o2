# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

import random

answer = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa mitä lukua ajattelen 1 ja 10 väliltä: "))
    if arvaus == answer:
        print("Arvasit oikein!")
        break
    elif arvaus < answer:
        print("Liian pieni arvaus!")
    else:
        print("Liian suuri arvaus!")
