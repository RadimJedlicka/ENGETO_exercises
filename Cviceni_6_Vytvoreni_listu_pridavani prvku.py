# Tvým úkolem je napsat kód, který:
#
# proměnné kandidati přiřadí prázdný list,
# vytiskne obsah proměnné kandidati za větu 'Kandidáti na začátku: ',
# do proměnné zamestnanci přiřadí list, který bude obsahovat stringy: 'František', 'Anna', 'Jakub', 'Klára',
# vytiskne obsah zamestnanci za větu 'Zaměstnanci na začátku: ',
# do prázdného listu kandidáti přidá jména 'Bruno' a 'Anežka',
# vytiskne obsah listu kandidati za string 'Nová jména přidána do kandidati: ',
# vloží jméno 'Bruno', uložené v listu kandidati, do listu zamestnanci na pozici index 1,
# vytiskne obsah proměnné zamestnanci za string: 'Nová jména vložena do zamestnanci:

# Vytvoreni kandidatu
kandidati = []

# Tisk kandidatu na zacatku
print("Kandidati na zacatku:", kandidati)

# Vytvoreni zamestnancu
zamestnanci = ["Frantisek", "Anna", "Jakub", "Klara"]

# Tisk zamestnancu na zacatku
print("Zamestnanci na zacatku:", zamestnanci)

# Pridani novych kandidatu
kandidati.append("Bruno")
kandidati.append("Anezka")

# Tisk novych kandidatu
print("Nova jmena pridana do kandidati:", kandidati)

# Vlozeni jmena
zamestnanci.insert(1, kandidati[0])

# Tisk listu zamestnanci po vlozeni noveho jmena
print("Nova jmena vlozena do zamestnanci:", zamestnanci)
