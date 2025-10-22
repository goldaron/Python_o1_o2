# Jatka edellisen tehtävän ohjelmaa siten, että Talo-luokassa on parametriton metodi palohälytys, 
# joka käskee kaikki hissit pohjakerrokseen. Jatka pääohjelmaa siten, että talossasi tulee palohälytys.

class Hissi:    
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros
        
    def siirry_kerrokseen(self, kerros):
        while self.nykyinen_kerros < kerros:
            self.kerros_ylös()
        while self.nykyinen_kerros > kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        if self.nykyinen_kerros < self.ylin_kerros:
            self.nykyinen_kerros += 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo ylimmässä kerroksessa.")

    def kerros_alas(self):
        if self.nykyinen_kerros > self.alin_kerros:
            self.nykyinen_kerros -= 1
            print(f"Hissi on nyt kerroksessa {self.nykyinen_kerros}.")
        else:
            print("Hissi on jo alimmassa kerroksessa.")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissiä(self, hissi_numero, kohde_kerros):
        if 0 <= hissi_numero < len(self.hissit):
            print(f"Ajetaan hissiä {hissi_numero} kerrokseen {kohde_kerros}.")
            self.hissit[hissi_numero].siirry_kerrokseen(kohde_kerros)
        else:
            print("Virhe: Hissin numero on väärä.")
            
    def palohälytys(self):
        print("Palohälytys! Kaikki hissit alas pohjakerrokseen.")
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)

# Testataan Talo-luokkaa
talo = Talo(1, 10, 3)  # Talo, jossa on 3 hissiä kerroksissa 1-10
talo.aja_hissiä(0, 5)  # Ajetaan ensimmäistä hissiä kerrokseen 5
talo.aja_hissiä(1, 8)  # Ajetaan toista hissiä kerrokseen 8
talo.aja_hissiä(2, 1)  # Ajetaan kolmatta hissiä kerrokseen 1
talo.palohälytys()     # Kutsutaan palohälytystä