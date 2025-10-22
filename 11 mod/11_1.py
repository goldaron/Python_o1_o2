# Toteuta seuraava luokkahierarkia Python-kielellä: 
# Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi. 
# Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. 
# Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. 
# Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). 
# Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla.

class Julkaisu:
    def __init__(self, nimi: str):
        self.nimi = nimi


class Kirja(Julkaisu):
    def __init__(self, nimi: str, kirjoittaja: str, sivumaara: int):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self) -> None:
        print(f"{self.nimi}, kirjailija {self.kirjoittaja}, {self.sivumaara} sivua")


class Lehti(Julkaisu):
    def __init__(self, nimi: str, paatoimittaja: str):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self) -> None:
        print(f"{self.nimi}, päätoimittaja {self.paatoimittaja}")


if __name__ == "__main__":
    aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
    hytti = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    aku_ankka.tulosta_tiedot()
    hytti.tulosta_tiedot()