# Výsledkem této úlohy bude jednoduchý převaděč jednotek, který bude umět převádět z kilogramů na libry,
# z kilometrů na míle _ z litrů na galony.
# V Python oknu už máš vypsané převodní poměry k jednotkám. Vytvoř proměnné s počtem jednotek
# (kg_pocet ,km_pocet ,l_pocet) k převedení _ proměnné s výpočtem (kg_vysledek ,km_vysledek ,l_vysledek).
# Tvým úkolem je převést:
# 80 kg na lb
# 54 km na míle
# 5 l na gal
# Nakonec výsledky přehledně vypiš ve větách.

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

# provadim zmeny
