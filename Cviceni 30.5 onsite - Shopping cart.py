kosik = {}
oddelovac = "=" * 40
potraviny = {
    "mleko": [30, 5],  # index '0'-> cena, index '1' -> pocet
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}

print(oddelovac, f'Viteje u naseho nakupniho kosiku!'.center(len(oddelovac)), oddelovac, sep='\n')

for goods in potraviny:
    print(f'| POTRAVINA: {goods:<9} | CENA: {potraviny[goods][0]:>3},-Kc |'.center(len(oddelovac)))
print('pro ukonceni stiskni \'x\''.center(len(oddelovac)), oddelovac, sep='\n')

# ALTERNATIVA
# for potravina, detaily in potraviny.items():
#     print(
#         f"| POTRAVINA: {potravina: <10}| CENA: {detaily[0]: <3}|".center(len(oddelovac))
#     )
# else:
#     print(oddelovac)

while True:
    select = (input('Vlozit do kosiku: '))
    if select == 'x':
        break

    elif select not in potraviny:
        print(f'{select} neni v nabidce')

    elif select not in kosik and potraviny[select][1] > 0:
        kosik[select] = [potraviny[select][0], 1]
        potraviny[select][1] -= 1

    elif select in kosik and potraviny[select][1] > 0:
        kosik[select][1] += 1
        potraviny[select][1] -= 1

    elif potraviny[select][1] == 0:
        print('Toto zbozi jiz neni skladem')

# print(kosik)

suma = []
for cena in kosik:
    suma.append(kosik[cena][1]*kosik[cena][0])
# print(suma)
celkem = sum(suma)

print(oddelovac, 'Vase uctenka'.center(len(oddelovac)), oddelovac, sep='\n')

for item in kosik:
    print(f'| {kosik[item][1]}x {item: <10}    ={kosik[item][0]*kosik[item][1]: >4},-Kc |'.center(len(oddelovac)))

print(oddelovac)
print(f'Celkova cena za nakup: {celkem},-Kc'.rjust(len(oddelovac)))

