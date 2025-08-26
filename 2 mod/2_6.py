#Ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random

# Koodien numeromerkkien välit
start3 = 0
stop3 = 9
start4 = 1
stop4 = 6

koodi1 = str(random.randint(start3, stop3)) + str(random.randint(start3, stop3)) + str(random.randint(start3, stop3))
koodi2 = str(random.randint(start4, stop4)) + str(random.randint(start4, stop4)) + str(random.randint(start4, stop4)) + str(random.randint(start4, stop4))

#Tulostetaan koodit loopilla
print(f"Kolminumeroinen koodi on: {koodi1}")
print("\n") #Riviväli vaan koska voi
print(f"Nelinumeroinen koodi on: {koodi2}")