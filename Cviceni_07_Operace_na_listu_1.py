# Pokračujeme v práci s listem, s kódem z minulé úlohy. Napiš kód, který:
#
# odstraní prvek 'Bruno' z listu kandidati,
# vytiskne obsah proměnné kandidati za string: 'Bruno odstraněn z kandidati: ',
# zopakovat jméno 'Anežka' uvnitř listu kandidati,
# vytisknout obsah listu kandidati za string: 'Opakování prvku Anežka v kandidati:',
# spoj list zamestnanci s listem kandidati do nového listu, který zachová název zamestnanci,
# vytiskni obsah nového listu zamestnanci za string: 'Spojeni kandidati a zamestnanci: ',
# vytisknout jméno na indexu 2 za string: 'Na indexu 2 je: ',
# vytisknout jméno na posledním indexu za string: 'Na <posledni_index> indexu je: '
# <posledni_index> by mělo být nahrazeno číslem posledního indexu z našeho nově spojeného listu zamestnanci.

# Výsledky z minulé úlohy
kandidati = ['Bruno', 'Anežka']
zamestnanci = ['František', 'Bruno', 'Anna', 'Jakub', 'Klára']

# Odstraneni jmena z kandidati
kandidati.remove("Bruno")

# Tisk zbylych kandidatu
print("Bruno odstranen z kandidati:", kandidati)

# Opakovani prvku
kandidati = kandidati * 3

# Tisk opakovani prvku v listu kandidati
print("Opakovani prvku Anezka v kandidati:", kandidati)

# Spojeni listu
zamestnanci = zamestnanci + kandidati

# Tisk spojenych listu
print(zamestnanci)

# Index 2
print("Na indexu 2 je:", zamestnanci[2])

# Zjisteni posledniho indexu a prirazeni do promenne
posledni_index = len(zamestnanci) - 1

# Posledni index
print("Na", posledni_index, "indexu je:", zamestnanci[posledni_index])