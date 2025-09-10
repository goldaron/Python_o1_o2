# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='golda',
         password='GoldaKoodaa',
         autocommit=True
         )

def hae_lentokentat(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}';"
#    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]}, {rivi[1]}")
    return

icao = input("Anna ICAO-koodi: ").upper() #EFHK
hae_lentokentat(icao)