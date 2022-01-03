# vstupni hodnoty
MESTA = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
CENY = (150, 200, 120, 120, 100, 180)
ODDELOVAC = "=" * 35

# uvitani uzivatele
print("Vitejte v nasi aplikaci DESTINATIO!")
print(ODDELOVAC)
print("1 - Praha    | 150")
print("2 - Viden    | 200")
print("3 - Olomouc  | 120")
print("4 - Svitavy  | 120")
print("5 - Zlin     | 100")
print("6 - Ostrava  | 180")
print(ODDELOVAC)

# vkladani udaju
lokalita = int(input("Vyberte cislo lokality: "))
jmeno = input("Jmeno: ")
prijmeni = input("Prijmeni:")
rok_narozeni = input("Rok narozeni: ")
email = input("E-mail: ")
heslo = input("Heslo: ")

# uprava zadanych hodnot
destinace = MESTA[lokalita - 1]
cena = CENY[lokalita -1]
# vypisovani vystupu
print(ODDELOVAC)
print("Listek do:", destinace, "Cena:", cena)
print("Dekuji,", jmeno, "na e-mail", email, "Ti prijde kratky dotaznik.")