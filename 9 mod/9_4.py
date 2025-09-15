# Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän.
# Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
# Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km.
# Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.

import random

class Auto:
    def __init__(self, rek, maxspeed, speed=0, travel=0):
        self.rek = rek
        self.maxspeed = maxspeed
        self.speed = speed
        self.travel = travel

    def kiihdyta(self, acc):
        # Laske uusi nopeus
        uusi_nopeus = self.speed + acc
        # Varmista, että nopeus ei ylitä huippunopeutta eikä laske alle nollan
        if uusi_nopeus > self.maxspeed:
            self.speed = self.maxspeed
        elif uusi_nopeus < 0:
            self.speed = 0
        else:
            self.speed = uusi_nopeus
        return

    def kulje(self, hours):
        self.travel += self.speed * hours
        return

# Luodaan lista ja autot
autot = []

for i in range(1, 11):
    rek = f"ABC-{i}"
    maxspeed = random.randint(100, 200)  # Arvotaan huippunopeus 100-200 km/h
    autot.append(Auto(rek, maxspeed))

# Simuloidaan kilpailua, kunnes jokin autoista on kulkenut vähintään 10 000 km
kilpailu_kaynnissa = True

while kilpailu_kaynnissa:
    for auto in autot:
        # Arvotaan nopeuden muutos -10 ja +15 km/h väliltä
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        # Käsketään autoa kulkemaan yhden tunnin ajan
        auto.kulje(1)
        # Tarkistetaan, onko auto kulkenut vähintään 10 000 km
        if auto.travel >= 10000:
            kilpailu_kaynnissa = False

# Tulostetaan kilpailun tulokset
print(f"{'RekNo':<10} {'Huiput':<15} {'Nopeus':<10} {'Kuljettu matka':<15}")
for auto in autot:
    print(f"{auto.rek:<10} {auto.maxspeed:<15} {auto.speed:<10} {auto.travel:<15}")