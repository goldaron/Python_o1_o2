# Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# ICAO-koodeja: KJFK, KLAX, EFHK, EGLL, EHAM

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='golda',
         password='GoldaKoodaa',
         autocommit=True
         )

def hae(point1, point2):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident='{point1}' OR ident='{point2}';"
#    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
#    print(tulos)
    if len(tulos) == 2 : #Tarkistetaan että tuloksia on vain kaksi
        port1, lat1, lon1 = tulos[0]     #Pilkotaan ja tallennetaan eka ja toka tulos muuttujiksi.
        port2, lat2, lon2 = tulos[1]
        point_a = lat1, lon1      #Tallennetaan ne omaan muuttujaan
        point_b = lat2, lon2
        km = distance.distance(point_a, point_b).km     #Lasketaan etäisyys kilometreinä geopy distance kirjaston avulla.
        print(f"Etäisyys {port1} ja {port2} välillä on {km:.2f} kilometriä.")  #Tulostetaan vastaus
    else:
        print("Haku epäonnistui.")
    return

point1 = input("Anna ensimmäinen ICAO-koodi: ").upper()
point2 = input("Anna toinen ICAO-koodi: ").upper()
hae(point1, point2)