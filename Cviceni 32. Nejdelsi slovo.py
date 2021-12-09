# Napiš program, který z listu slova vybere nejdelší slovo _ vytiskne do terminálu
# tuple s tímto nejdelším slovem _ jeho délkou.
#
# Použij prosím tento list:

slova = [
'Python', 'is', '_', 'widely', 'used',
'high-level', 'programming', 'language',
'for', 'general-purpose', 'programming,',
'created', 'by', 'Guido', 'van', 'Rossum',
'and', 'first', 'released', 'in', '1991.',
]

# moje reseni
# list = []
# for slovo in slova:
#     list.append((len(slovo), slovo))
#
# vysledek = (sorted(list, reverse=True))
#
# print(vysledek[0][1],vysledek[0][0])

# reseni pomoci while cyklu
nejdelsi_slovo  = ('', 0)

while slova:
    slovo = slova.pop(0)
    if len(slovo) > nejdelsi_slovo[1]:
        nejdelsi_slovo = (slovo, len(slovo))

print(nejdelsi_slovo)
