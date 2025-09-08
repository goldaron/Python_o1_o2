# Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = (
        "talvi",  # Tammikuu
        "talvi",  # Helmikuu
        "kevät",  # Maaliskuu
        "kevät",  # Huhtikuu
        "kevät",  # Toukokuu
        "kesä",   # Kesäkuu
        "kesä",   # Heinäkuu
        "kesä",   # Elokuu
        "syksy",  # Syyskuu
        "syksy",  # Lokakuu
        "syksy",  # Marraskuu
        "talvi"   # Joulukuu
    )

kuukaudet = ("tammikuu", "helmikuu", "maaliskuu","huhtikuu","toukokuu","kesäkuu","heinäkuu",
    "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")

# Kysytään käyttäjältä kuukauden numero
kuukausi = int(input("Anna kuukauden numero (1-12): "))

# Tarkistetaan, että annettu numero on kelvollinen
if 1 <= kuukausi <= 12:
    # Tulostetaan vastaava vuodenaika
    print(f"Vuoden {kuukausi}. kuukausi eli {kuukaudet[kuukausi-1]} on {vuodenajat[kuukausi-1]} kuukausi.")
else:
    print("Yrittäisit edes, ohjelma loppuu.")