# V Python oknu už máš vypsané ceny Mercedesu, Rolls-Royce _ příplatkové výbavy. Poté bude třeba spočítat _ uložit do proměnných:
#
# Cenu za dva Mercedesy,
# cenu za Mercedes _ Rolls-Royce,
# cenu za dva Rolls-Royce s příplatkovou výbavou (každý z nich),
# cenu za Mercedes s příplatkovou výbavou.
# následně vytvoř proměnnou, která si od uživatele vyžádá libovolnou slevu na mercedes _ do další proměnné ulož slevu na mercedes.
# Nakonec by měl program všechno přehledně vypsat. Pusť se do toho.

# Cenik
mercedes    = 150000
rolls_royce = '400000'
vybava = 50000

mer2 = mercedes * 2
mer_rols = mercedes + int(rolls_royce)
rols_vybava = (int(rolls_royce) + vybava) * 2
mer_vybava = mercedes + vybava

sleva = input("O kolid USD zlevnime mercedes?")
sleva_mer = int(sleva)

print("Cena za dva Mercedesy je:", mer2)
print("Cena za Mercedes _ Rolls-Royce:", mer_rols)
print("Cena za dva Rolls-Royce s priplatkovou vybavou:", rols_vybava)
print("Cena za Mercedes s priplatkovou vybavou:", mer_vybava)
print("Cena za Mercedes po sleve:", mercedes - sleva_mer)