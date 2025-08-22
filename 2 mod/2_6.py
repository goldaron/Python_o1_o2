#Ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

# Koodien numeromerkkien välit
start3 = 0
stop3 = 9
start4 = 1
stop4 = 6

#Tulostetaan koodit loopilla
print("Kolminumeroinen koodi on:")
for i in range(3):
    print(random.randint(start3, stop3))

print("\n") #Riviväli vaan koska voi

print("Nelinumeroinen koodi on:")
for i in range(4):
    print(random.randint(start4, stop4))