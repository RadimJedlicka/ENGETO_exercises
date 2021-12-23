import os
from random import choice, seed
from slova import hadana_slova
from grafika import obesenec


zivoty = 7
hra_bezi = True
# slovo = "obesenec"  # TODO: nahodny vzber pomoci random.choice()
seed(42)              # zafixuji nahodny vyber
slovo = choice(hadana_slova)
tajenka = len(slovo) * ["_"]
print(slovo)
control = []
# quit()

# 1. smycka pro clou hru, hlidani zivotu
while hra_bezi and zivoty > 0:
    os.system("cls ")
    print(f"Tajenka: {' '.join(tajenka)}")
    print(obesenec[7 - zivoty])
    # 2. Hadani slova/pismena - input()
    hadani = input("hadej pismeno/slovo: ")
    # je zadane slovo stejne jako tajenka?
    if hadani == slovo:
        hra_bezi = False
    elif len(hadani) == 1 and hadani in control:
        print("Pismeno uz jsi hadal!")              # TODO: rozsirit na seznam kontrol
    # je zadane pismeno v tajence?
    elif len(hadani) == 1 and hadani in slovo:
        print(obesenec[7 - zivoty])
        for index, symbol in enumerate(slovo):
            if symbol == hadani:
                tajenka[index] = hadani
                print("Uhodl jsi pismeno!")

    # zadane slovo ani pismeno neni v tajence
    else:
        control.append(hadani)
        zivoty = zivoty - 1  # zkracene zivoty -= 1
        print('Chyba!')
# 3. Vyhodnoceni vysledku hry
else:
    # slovo je uhadnuto
    if not hra_bezi:
        os.system("cls ")
        print(f"tajenka: {slovo}", "Gratulujeme, vyhral jsi!", sep="\n")
    # dosly zivoty
    else:
        print(f"Prohral jsi, tajenka byla {slovo}")
        print(obesenec[7 - zivoty])

# TODO: Uklid vypisu v konzoli - os.system("cls")

# TODO: Vykreslieni figurky
