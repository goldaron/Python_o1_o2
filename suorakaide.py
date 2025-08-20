#kerätään mitat ja tallennetaan arvot muuttujiin'
kanta = float(input("Anna suorakaiteen kanta: "))
korkeus = float(input("Anna suorakaiteen korkeus: "))
ala = kanta * korkeus

# print("Pinta-ala: "+str(ala))
print(f"Pinta-ala on {ala:.5f}")