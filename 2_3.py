#Ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.
kanta = float(input("Anna suorakaiteen kanta: "))
korkeus = float(input("Anna suorakaiteen korkeus: "))

#Lasketaan annettujen arvojen mukaan
ala = kanta * korkeus
piiri = (kanta * 2) + (korkeus * 2)

#Tulostetaan vastaus kahden desimaalin tarkkuudella.
print(f"Suorakulmion piiri on {piiri:.2f} ja pinta-ala on {ala:.2f}")