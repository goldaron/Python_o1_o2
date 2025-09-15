# Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi, joka saa parametrinaan nopeuden muutoksen (km/h).
# Jos nopeuden muutos on negatiivinen, auto hidastaa. Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
# Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
# Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h, sitten +70 km/h ja lopuksi +50 km/h.
# Tulosta tämän jälkeen auton nopeus. Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
# Kuljettua matkaa ei tarvitse vielä päivittää.

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

auto1 = Auto("ABC-123", 142)

# Kiihdytä autoa
auto1.kiihdyta(30)  # Nosta nopeutta +30 km/h
auto1.kiihdyta(70)  # Nosta nopeutta +70 km/h
auto1.kiihdyta(50)  # Nosta nopeutta +50 km/h

# Tulosta auton nopeus
print(f"Auton nopeus: {auto1.speed} km/h")

# Hätäjarrutus
auto1.kiihdyta(-200)  # Vähennä nopeutta -200 km/h

# Tulosta uusi nopeus
print(f"Auton nopeus hätäjarrutuksen jälkeen: {auto1.speed} km/h")


# cars = [auto1]
# for car in cars:
#    carno = 0+1
#    print(f"\nAuto {carno}"
#          f"\nRekisterinumero: {car.rek}"
#          f"\nHuippunopeus: {car.maxspeed} km/h"
#          f"\nNopeus tällä hetkellä: {car.speed} km/h"
#          f"\nKilometrejä mittarissa {car.travel} km")