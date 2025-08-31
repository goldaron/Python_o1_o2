#  ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
#  Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
#  Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

numbers = []

number = input("Anna numero: ")

while number.isdigit():
    numbers.append(int(number))
    number = input("Anna numero tai lopeta painamalla enter: ")

if len(numbers) >= 5:
    numbers.sort(reverse=True)
    x1 = numbers[0]
    x2 = numbers[1]
    x3 = numbers[2]
    x4 = numbers[3]
    x5 = numbers[4]
    print(f"Viisi suurinta annettua lukua: {x1}, {x2}, {x3}, {x4} ja {x5} tai {numbers[0:5]}")
else:
    numbers.sort(reverse=True)
    print(f"Antamasi luvut: {numbers}")