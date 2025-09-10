# Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.)

lentoasemat = { # Sanakirja lentoasemien tallentamiseen muutamalla lentokentällä
        "EFHK": "Helsinki-Vantaa",
        "EHAM": "Amsterdam Schiphol",
        "KJFK": "John F. Kennedy International",
        "EGLL": "London Heathrow",
        "LFPG": "Charles de Gaulle",
    }

while True:
    print("\nValitse toiminto:")
    print("1. Syötä uusi lentoasema")
    print("2. Hae lentoaseman tiedot")
    print("3. Lopeta")
    valinta = input("Anna valintasi (1, 2 tai 3): ").strip() # formatoidaan käyttäjän syötteestä vahingot alusta ja lopusta pois

    if valinta == "1": #Lisätään uusi lentoasema, formatoidaan käyttäjän syöte
        icao = input("Anna lentoaseman ICAO-koodi: ").strip().upper() # Format ICAO ISOIKSI kirjaimiksi
        nimi = input("Anna lentoaseman nimi: ").strip()
        if icao in lentoasemat:#Jos kenttä on jo syötetty palautetaan sanakirjasta vastaus
            print(f"Lentoasema {icao} on jo tallennettu nimellä {lentoasemat[icao]}.")
        else:
            lentoasemat[icao] = nimi #"ICAO": "Lentoaseman nimi"
            print(f"Lentoasema {icao} nimellä {nimi} tallennettu.")

    elif valinta == "2": #Haku joka tulostaa nimen, formatoidaan käyttäjän syöte
        icao = input("Anna haettavan lentoaseman ICAO-koodi: ").strip().upper() #Formatoidaan koodi ISOIKSI
        if icao in lentoasemat: # Katsotaan sanakirjasta ja palautetaan jos löytyy
            print(f"Lentoasema ICAO-koodilla {icao} on {lentoasemat[icao]}")
        else: # Ja jos ei löydy
            print(f"Lentoasemaa ICAO-koodilla {icao} ei löydy.")

    elif valinta == "3": #Lopetetaan ohjelma
        print("Ohjelma lopetetaan.")
        break

    else: #Kun ei osata käyttää ohjelmaa ohjeista huolimatta...
        print("Virheellinen valinta, yritä uudelleen.")