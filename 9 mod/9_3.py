#
#

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

# Luo uusi auto-olio
auto1 = Auto("ABC-123", 142, 60, 1000)

auto1.kulje(2.5)
print(f"{auto1.rek:<10} {auto1.maxspeed:<15} {auto1.speed:<10} {auto1.travel:<15}")
