#Ohjelma joka kysyy ympyrän säteen ja tulostaa sen pinta-alan
#Math tuo piin arvon
import math
pi = math.pi

sade = float(input("Anna ympyrän säde: "))
#Pinta-ala lasketaan A=pi*r²
ala = pi * pow(sade, 2)
print(f"Ympyrän pinta-ala (A) on {ala:.5f} jotain yksikköä.")