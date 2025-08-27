#Ohjelma joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen arvon.

while True:
    tuumat = float(input("Tuumat: "))

    # Tarkistetaan onko annettu arvo negatiivinen
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    # Muunnetaan tuumat senttimetreiksi
    cm = tuumat * 2.54

    # Tulostetaan vastaus
    print(f"{tuumat} tuumaa = {cm:.2f}cm")