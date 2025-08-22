#Ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

user = input("Oletko mies vai nainen: ").lower()
print(user)
hemoglobin_val = int(input("Anna hemoglobiiniarvo g/l:"))
print(hemoglobin_val)

if user=="mies":
    if hemoglobin_val>195:
        print("Sinulla on korkea hemoglobiini.")
    elif hemoglobin_val<=195 and hemoglobin_val>=134:
        print("Sinulla on normaali hemoglobiini.")
    else:
        print("Sinulla on alhainen hemoglobiini.")
if user=="nainen":
    if hemoglobin_val>175:
        print("Sinulla on korkea hemoglobiini.")
    elif hemoglobin_val<=175 and hemoglobin_val>=117:
        print("Sinulla on normaali hemoglobiini.")
    else:
        print("Sinulla on alhainen hemoglobiini.")
else:
    print("Tarkistuksen tekemiseksi, vastaa oletko mies vai nainen")
