# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.
import math

def is_it_worth(halkaisija, hinta):
    """Muuttaa pizzan halkaisijan metreiksi ja laskee pizzan pinta-alan sekä hinnan per neliömetri"""
    halkaisija_m = halkaisija / 100 # 1m = 100cm
    ala = math.pi / 4 * halkaisija_m**2 # A = pi*r^2 tai A = pi/4*d^2 r = säde, d = halkaisija
    worth = hinta / ala # neliöhinta saadaan jakamalla hinta pinta-alalla.
    return worth

koko1 = float(input("Anna pizzan koko sentteinä: "))
hinta1 = float(input("Anna pizzan hinta euroina: "))
koko2 = float(input("Anna pizzan koko sentteinä: "))
hinta2 = float(input("Anna pizzan hinta euroina: "))

vastine1 = is_it_worth(koko1, hinta1)
vastine2 = is_it_worth(koko2, hinta2)

if vastine1 > vastine2:
    print(f"Pizza 2, {koko2}cm on enemmän wörtti, {vastine2:.2f}€/neliömetri.")
elif vastine1 < vastine2:
    print(f"Pizza 1, {koko1}cm on enemmän wörtti. {vastine1:.2f}€/neliömetri.")
elif vastine1 == vastine2:
    print(f"Pizzat ovat yhtä wörttejä. Hinta {vastine1:.2f}€/neliömetri")
else:
    print("Jotain meni pieleen, ei pizzaa sinulle.")