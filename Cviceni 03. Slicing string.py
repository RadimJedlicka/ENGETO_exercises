# Vytvoř prográmek, který využije indexingu tak, aby vytiskl a extrahoval:
#
# prvních 5 písmen slova 'indexování' a ulož je do proměnné prvnich_pet,
# posledních 5 písmen slova 'indexování' a ulož je do proměnné poslednich_pet,
# každé třetí písmeno slova 'indexování' (počínaje prvním písmenem "i") a ulož je do proměnné kazde_treti.

# Extrahuj a vytiskni prvních 5 písmen
prvnich_pet = "indexování"[:5]
print("Prvnich 5 pismen:", prvnich_pet)

# Extrahuj a vytiskni posledních 5 písmen
poslednich_pet = "indexování"[5:]
print("Poslednich pet pismen:", poslednich_pet)

# Extrahuj a vytiskni každé 3 písmeno
kazde_treti = "indexování"[::3]
print("Kazde treti pismeno (pocinaje prvnim):", kazde_treti)