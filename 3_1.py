#Ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle, montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm.

fish = float(input("Anna kuhan mitta sentteinä: "))

if fish<=37:
    erotus = 37-fish
    print(f"Kuha on alamittainen, mittaa puuttuu {erotus:.0f}cm")
if fish>=37:
    print("Kuha on yli alamitan, hieno vonkale!")