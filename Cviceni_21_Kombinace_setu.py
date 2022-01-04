# Prirazeni promennych
str1 = 'New York'
str2 = 'Yorkshire'

# Najde spolecne prvky
spolecne = set(str1).intersection(set(str2))
# nebo:
spolecne = set(str1) & set(str2)

# Najde unikatni prvky
unikatni = set(str1).difference(set(str2))
# nebo:
unikatni = set(str1) - set(str2)

# Najde nesdilene prvky
nesdilene = set(str1).symmetric_difference(set(str2))
# nebo:
nesdilene = set(str1) ^ set(str2)

# Najde vsechny prvky
vsechny = set(str1).union(set(str2))
# nebo:
vsechny = set(str1) | set(str2)

# Vypis vsechno
print("Spolecne: ", spolecne)
print("Unikatni: ", unikatni)
print("Nesdilene: ", nesdilene)
print("Vsechny: ", vsechny)
