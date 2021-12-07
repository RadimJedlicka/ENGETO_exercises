# Prevodni pomery
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

# Pocet jednotek, ktery ma byt preveden.
kg_pocet = 80
km_pocet = 54
l_pocet = 5

# Vypocty pro prevod
kg_vysledek = kg_pocet * kg_lb
km_vysledek = km_pocet * km_mile
l_vysledek = l_pocet * l_gal

# Vysledne odpovedi
print(kg_pocet, "kilogramu se rovna", kg_vysledek, "liber.")
print(km_pocet, "kilometru se rovna", km_vysledek, "mil.")
print(l_pocet, "litru se rovna", l_vysledek, "galonu.")
print("Uz tu umim docela dost veci")
