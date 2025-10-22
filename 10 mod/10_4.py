# Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. 
# Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. 
# Luokassa on alustaja, joka saa parametreinaan nimen, 
# kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. 
# Luokassa on seuraavat metodit: tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut 
# tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia. 
# tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna. 
# kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. 
# Muussa tapauksessa palautetaan False.

# Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". 
# Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. 
# Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, 
# jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. 
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random

class Kilpailu:
    def __init__(self, nimi, pituus_km, autot):
        self.nimi = nimi
        self.pituus_km = pituus_km
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.travel >= self.pituus_km:
                return True
        return False
    def tulosta_tilanne(self):
        print(f"\n{'RekNo':<10} {'Huiput':<10} {'Nopeus':<10} {'Kuljettu matka':<10}")
        for auto in self.autot:
            print(f"{auto.rek:<10} {auto.maxspeed:<10} {auto.speed:<10} {auto.travel:<10}")

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

kilpailu_kaynnissa = True

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)
tunnit = 0

while kilpailu.kilpailu_ohi() == False:
    kilpailu.tunti_kuluu()
    tunnit += 1
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

# Tulostetaan kilpailun tulokset
print(f"\nKilpailun {kilpailu.nimi} tulokset:")
print(f"\n{'RekNo':<10} {'Huiput':<10} {'Nopeus':<10} {'Kuljettu matka':<10}")
for auto in autot:
    print(f"{auto.rek:<10} {auto.maxspeed:<10} {auto.speed:<10} {auto.travel:<10}")