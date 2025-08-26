#Ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C)
# ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.
# LUX on parvekkeellinen hytti yläkannella.
# A on ikkunallinen hytti autokannen yläpuolella.
# B on ikkunaton hytti autokannen yläpuolella.
#C  on ikkunaton hytti autokannen alapuolella.

print("Hyttiluokat: LUX, A, B tai C")
hyttiluokka = input("Anna hyttiluokka: ").upper()

if hyttiluokka=="LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka=="A":
    print("A on ikkunallinen hytti on autokannen yläpuolella.")
elif hyttiluokka=="B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka=="C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Hyttiluokkaa ei löytynyt. Voit ostaa lipun asiakaspalvelusta. :)")
