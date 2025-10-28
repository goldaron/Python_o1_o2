# Toteuta taustapalvelu, joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa. 
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta. Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: 
# http://127.0.0.1:3000/kenttä/EFHK. Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

from flask import Flask, Response
import json
import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='golda',
         password='GoldaKoodaa',
         autocommit=True
         )

app = Flask(__name__)
@app.route('/kenttä/<icao>')

def kentta(icao):
    sql = f"SELECT ident, name, municipality FROM airport WHERE ident='{icao}';"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    if tulos:
        ident, name, municipality = tulos
        tilakoodi = 200
        vastaus = {
            "status": tilakoodi,
            "ICAO": ident,
            "Name": name,
            "Municipality": municipality
        }
    else:
        tilakoodi = 404
        vastaus = {
            "status": tilakoodi,
            "teksti": "Lentokenttää ei löydy"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)