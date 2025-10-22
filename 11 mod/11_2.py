# Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. 
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. 
# Polttomoottoriauton ominaisuutena on bensatankin koko litroina. 
# Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, 
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi 
# sekä asettaa oman kapasiteettinsa. 
# Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton 
# (ACD-123, 165 km/h, 32.3 l). 
# Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran 
# ja tulosta autojen matkamittarilukemat.

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

class Sahkoauto(Auto):
    def __init__(self, rek, maxspeed, speed, akkukapasiteetti):
        super().__init__(rek, maxspeed, speed)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottoriauto(Auto):
    def __init__(self, rek, maxspeed, speed, bensatankin_koko):
        super().__init__(rek, maxspeed, speed)
        self.bensatankin_koko = bensatankin_koko

tesla = Sahkoauto("SAH-KO", 180, 123, 52.5)
audi = Polttomoottoriauto("AUDI-123", 165, 134, 32.3)

for auto in [tesla,audi]:
    auto.kulje(3)
    print(f"{auto.rek}: {auto.travel} km")