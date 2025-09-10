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
    sql = f"SELECT name, municipality FROM airport WHERE iso_country='{maakoodi}';"
    print(sql)
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]}, {rivi[1]}")
    return

maakoodi = input("Anna maakoodi: ").upper()
hae_lentokentat(maakoodi)