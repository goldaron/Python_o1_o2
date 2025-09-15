# Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus, tämänhetkinen nopeus ja kuljettu matka.
# Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
# Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.

class Auto:
    def __init__(self, rek, maxspeed, speed=0, travel=0):
        self.rek = rek
        self.maxspeed = maxspeed
        self.speed = speed
        self.travel = travel

auto1 = Auto("ABC-123", 142)

cars = [auto1]
for car in cars:
    carno = 0+1
    print(f"\nAuto {carno}"
          f"\nRekisterinumero: {car.rek}"
          f"\nHuippunopeus: {car.maxspeed} km/h"
          f"\nNopeus tällä hetkellä: {car.speed} km/h"
          f"\nKilometrejä mittarissa {car.travel} km")