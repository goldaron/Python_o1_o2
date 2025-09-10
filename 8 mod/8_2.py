# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta,
# helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='golda',
         password='GoldaKoodaa',
         autocommit=True
         )

def hae_lentokentat(maakoodi):
    sql = f"SELECT type, COUNT(*) AS 'amount' FROM airport WHERE iso_country='{maakoodi}' GROUP BY type;"
#    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]} {rivi[1]} kappaletta")
    return

maakoodi = input("Anna maakoodi: ").upper()
hae_lentokentat(maakoodi)