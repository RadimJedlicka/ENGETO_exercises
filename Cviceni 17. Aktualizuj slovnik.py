# Cílem této úlohy je vložit slovníky slovnik_1, slovnik_2 a slovnik_3 do našeho hlavního slovníku databaze.
# komentar navic

databaze = {
    'id123': {},
    'id124': {},
    'id125': {}
}

slovnik_1 = {
    'jmeno': 'Thomas',
    'vek': 45,
    'zeme': 'Czechia',
    'mesto': 'Brno'
}

slovnik_2 = {
    'jmeno': 'Daniel',
    'vek': 34,
    'zeme': 'Czechia',
    'mesto': 'Prague'
}

slovnik_3 = {
    'jmeno': 'Eva',
    'vek': 43,
    'zeme': 'Czechia',
    'mesto': 'Olomouc'
}

# reseni bez metody
# databaze["id123"] = slovnik_1
# databaze["id124"] = slovnik_2
# databaze["id125"] = slovnik_3

# reseni s metodou
databaze.update(id123 = slovnik_1)
databaze.update(id124 = slovnik_2)
databaze.update(id125 = slovnik_3)

import pprint
pprint.pprint(databaze)

x = databaze["id124"]["vek"]
y = databaze["id123"].keys()

print(y)