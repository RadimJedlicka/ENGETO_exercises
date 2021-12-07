# slovniky
slovnik01 = {'jmeno': 'David', 'prijmeni': 'Novak', 'vek': 33}
slovnik02 = {'pismena': ['a', 'b', 'c', 'd'], 'cisla': [1,2,3,4,5]}
slovnik03 = {
    'zamestnanci': {
        'id01': 'Marek',
        'id02': 'Matous',
        'id03': 'Anna'
    },
    'adresy': {
        'id01': 'Brno',
        'id02': 'Praha',
        'id03': 'Praha'
    }
}

klice_hodnoty = slovnik01.items()

klice = slovnik02.keys()

hodnoty = slovnik03.values()

vyzva = slovnik03["zamestnanci"].values()

print("Klice a hodnoty: ", klice_hodnoty)
print("Klice: ", klice)
print("Hodnoty: ", hodnoty)
print("Vyzva: ", vyzva)
