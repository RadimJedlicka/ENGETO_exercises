# Cílem této úlohy je nechat uživatele přidávat do proměnné kosik, tak dlouho, dokud bude chtít.
# Celá situace bude představovat proces virtuálního nákupu.

# Celá úloha se bude skládat z těchto kroků:

# Pozdravit uživatele a vypsat mu aktuální nabídku (proměnná nabidka),
# zapsat cyklus, který umožní postupně zadávat hodnoty do košíku (proměnná kosik) tak dlouho,
    # dokud si to bude uživatel přát,
# pokud uživatel zadá vstup do proměnné zbozi takové zboží, které není v proměnné potraviny,
    # vypiš: "Zboží <zbozi> není v nabídce",
# pokud zboží v proměnné kosik není, přidej 1 kus do košíku a odeber 1 kus z proměnné potraviny (index 1),
# pokud zboží v proměnné kosik je, uprav původní hodnotu +1 kus a z proměnné potraviny opět odeber 1 kus,
# pokud se v proměnné potraviny, na indexu 1 objeví u konkrétní potraviny hodnota 0,
    # potom vypiš: "Zboží <zbozi> není skladem",
# na závěr vypiš pomocí funkce print obsah proměnné kosik.

# Zadané hodnoty
kosik = dict()
oddelovac = "="
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}
nabidka = """
+-----------+----------+
| POTRAVINA |   CENA   |
+-----------+----------+
| mleko     |    30,-  |
| maso      |   100,-  |
| banan     |    30,-  |
| jogurt    |    10,-  |
| chleb     |    20,-  |
| jablko    |    10,-  |
| pomeranc  |    15,-  |
+-----------+----------+
 stiskni 'x' pro konec
"""

# Úvodní sekce s uvítáním a výpisem zboží
greetings = 'Vitejte u naseho nakupniho kosiku!'
print(greetings, oddelovac * len(greetings), sep='\n', end='')
print(nabidka)

# Cyklus, který přidává zboží do košíku tak dlouho, jak uživatel zamýšlí
while True:
    zbozi = (input('Zadej zbozi: '))
    if zbozi == 'x':
        break
    # .. pokud uživatel nezadá zboží z nabídky
    elif zbozi not in potraviny:
        print(f"Zboží {zbozi} není v nabídce")

    # .. pokud zboží ještě v košíku není
    elif zbozi not in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi] = [potraviny[zbozi][0], 1]
        potraviny[zbozi][1] -= 1

    # .. pokud se již vybrané zboží nachází v košíku
    elif zbozi in kosik and potraviny[zbozi][1] > 0:
        kosik[zbozi][1] += 1
        potraviny[zbozi][1] -= 1

    # .. pokud hodnota na indexu 1 odpovídá 0 (není skladem)
    elif potraviny[zbozi][1] == 0:
        print(f'Zboží {zbozi} není skladem')

    # print(kosik)
    # print(potraviny)

celkova_cena = 0
for item in kosik:
    celkova_cena += kosik[item][0] * kosik[item][1]

# Finální výpis košíku po nákupu
print(oddelovac * (len(greetings)))
print('Vase uctenka'.upper().center(len(greetings)))
print(oddelovac * (len(greetings)))
for item in kosik:
    print(f'| {kosik[item][1]}x {item} = '
          f'{kosik[item][0] * kosik[item][1]},- Kc |'.center(len(greetings), '-'))
print(oddelovac * (len(greetings)))
print(f'Celkova cena nakupu: {celkova_cena},-Kc'.rjust(len(greetings), '.'))




