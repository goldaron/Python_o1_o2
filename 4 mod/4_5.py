#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).

tries = 0
username = "python"
password = "rules"

while tries < 5:
    userinput = input("Anna käyttäjätunnus: ")
    if userinput == username:
        userpw = input("Anna salasana: ") #Ei näin nyt oikeesti kysytä
        if userpw == password:
            print("Tervetuloa! (●'◡'●)")
            break
        else:
            print("Koetappa uuestaa")
            tries += 1
    else:
        tries += 1
        print("Koetappa uuestaa")

    if tries >= 5:
        print("Pääsy evätty. Käyttäjätunnus lukittu 5 yrityksen jälkeen.\nOhjelma sammutetaan.")