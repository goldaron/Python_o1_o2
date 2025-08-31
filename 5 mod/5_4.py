# Ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin.
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

# Lista kaupungeista
cities = []

for i in range(5):
    # Pyydetään antamaan kaupungin nimi
    city = input("Anna kaupungin nimi: ")
    cities.append(city)
    i += 1

#Tulostetaan kaupungit järjestyksessä
print("Syötetyt kaupungit: ")
for city in cities:
    print(city)

