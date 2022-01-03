# Vytvoř prográmek, který využije indexingu tak, aby vytiskl _ extrahoval:
#
# prvních 5 písmen slova 'indexování' _ ulož je do proměnné prvnich_pet,
# posledních 5 písmen slova 'indexování' _ ulož je do proměnné poslednich_pet,
# každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i") _ ulož je do proměnné kazde_treti.

# Extrahuj _ vytiskni prvních 5 písmen
prvnich_pet = "indexování"[:5]
print("Prvnich 5 pismen:", prvnich_pet)

# Extrahuj _ vytiskni posledních 5 písmen
poslednich_pet = "indexování"[5:]
print("Poslednich pet pismen:", poslednich_pet)

# Extrahuj _ vytiskni každé 3 písmeno
kazde_treti = "indexování"[::3]
print("Kazde treti pismeno (pocinaje prvnim):", kazde_treti)