# Nyní dostaneš zadání úkolů, které prověří tvé porozuměnní novým metodám. Dej si na ně čas a ber jeden úkol po druhém. Pokud nevíš, neváhej se podívat do nápovědy nebo rovnou otevři řešení. Pojďme na to:
#
# TODO Na řádku 5 do proměnné rozdeleny_string ulož muj_string jako list rozdělený podle mezer.
# TODO Na řádku 12 a 13 do proměnné emaily přidej pouze emailové adresy pomocí jejich indexu v proměnné rozdeleny_string.
# TODO Na řádku 19 a 20 získej pouze domény (text za znakem '@') z emailů v listu emaily. První doménu ulož do proměnné domena01 a druhou do domena02.
# TODO Na řádku 23 a 24 rozděl stringy v promměnných domena01 a domena02 podle znaku '.' a ulož pouze první prvek (na indexu 0) do stejné proměnné.
# TODO Na řádku 29 ověř pomocí podmínky if, zda proměnná domena01 neobsahuje žádná čísla.
# TODO Na řádku 30 přiřaď kód pod příkaz if, který spojí s prázdným stringem bez_cisel pouze tu doménu, která neobsahuje číslice.
# TODO Na řádku 31 přiřaď pod příkaz if funkci print(), která vypíše následující: 'Doména', <doména>, 'byla přidána.'.
# TODO Na řádku 33 přiřaď pod příkaz else funkci print(), která vypíše následující: 'Doména <doména> nebyla přidána, protože obsahuje čísla!'.
# TODO To samé proveď na řádku 36, 37, 38 (if), a 40 (else) proměnnou domena02.

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

