#Ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
#Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskä = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

#Muunnetaan leiviskät nauloiksi ja naulat luodeista grammoiksi
naulat_total = (leiviskä * 20) + naulat
luodit_total = naulat_total * 32
grammat_total = luodit_total * 13.3
kg = grammat_total //1000
g = grammat_total %1000
print(grammat_total)

#Tulos
print(f"Massa nykymittojen mukaan: {kg:.0f}kg {round(g)}g")