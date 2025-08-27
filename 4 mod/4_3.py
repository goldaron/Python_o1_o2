# Ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

luvut = []

while True:
    luku = input("Anna luku tai paina enter lopettaaksesi: ")

    if luku == "":
        print(f"Pienin luku: {min(luvut)} ja suurin luku: {max(luvut)}")
        break
    luvut.append(int(luku))