import random

#Montako noppaa heitetään
lkm = int(input("Kuinka montaa noppaa heitetään? "))

#Heittojen summa
summa = 0

#Heitetään noppaa X kertaa ja lisätään se summaan
for i in range(lkm):
    summa += random.randint(1, 6)

#Tulostetaan vastaus, ekstrana heittojen keskiarvo.
print(f"Summa {lkm} heiton jälkeen: {summa}")
print(f"Heittojen keskiarvo {summa/lkm:.2f}")