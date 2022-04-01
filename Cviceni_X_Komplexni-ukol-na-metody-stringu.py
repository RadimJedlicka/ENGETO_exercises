# Zadany string
muj_string = 'Abc@abc.cz a Matous@1234.cz jsou naše emailové adresy'

# Rozdel string
rozdeleny_string = muj_string.split()

# Tisk promenne 'rozdeleny_string'
print(rozdeleny_string)

# Ziskej emaily
emaily = list()
emaily.append(rozdeleny_string[0])
emaily.append(rozdeleny_string[2])

# Tisk promenne 'emaily'
print(emaily)

# Ziskani domen
domena01 = emaily[0].split("@")[1]
domena02 = emaily[1].split("@")[1]

# Rozdel domeny podle znaku '.' a uloz je do stejne prommene
domena01 = domena01.split(".")[0]
domena02 = domena02.split(".")[0]

# Spoj promenne 'domena01' a 'domena02' s promennou 'bez_cisel'
bez_cisel = ''
# Dopln podminkovy vyraz pro 'domena01'
if domena01.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print(f'Doména {domena01} byla pridána.')
else:
    print(f'Doména {domena01} nebyla pridána, protože obsahuje čísla!')

# Dopln podminkovy vyraz pro 'domena02'
if domena02.isalpha():
    bez_cisel = bez_cisel.join(domena01)
    print('Doména', domena02, 'byla pridána.')
else:
    print(f'Doména {domena02} nebyla pridána, protože obsahuje císla!')

# ZDE NIC NEDOPLNUJ, jde o nasi kontrolu :)
if (len(bez_cisel) + 1) % 4 == 0:
    print('Bezva, dalsí zkouska úspesne za tebou. Jen tak dál!')
else:
    print('Bohuyel, nekde más chybku. Pokud si nevís rady, mrkni se dolů na resení.')