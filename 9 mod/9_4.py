# Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
# Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
# Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne.
# Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#
# Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä.
# Tämä tehdään kutsumalla kiihdytä-metodia.

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
        self.travel = self.travel + (self.speed * hours)
        return

auto1 = Auto("TIS-517", 142, 60, 2000)

cars = [auto1]
for car in cars:
    carno = 0+1
    print(f"\nAuto {carno}"
        f"\nRekisterinumero: {car.rek}"
        f"\nHuippunopeus: {car.maxspeed} km/h"
        f"\nNopeus tällä hetkellä: {car.speed} km/h"
        f"\nKilometrejä mittarissa {car.travel} km")

matka = int(input("\nAnna matka-aika tunteina: "))

auto1.kulje(matka)

for car in cars:
    carno = 0+1
    print(f"\nAuto {carno}"
        f"\nRekisterinumero: {car.rek}"
        f"\nHuippunopeus: {car.maxspeed} km/h"
        f"\nNopeus tällä hetkellä: {car.speed} km/h"
        f"\nKilometrejä mittarissa {car.travel} km")