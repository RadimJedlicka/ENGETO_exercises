import os


status = '+', '-', '*', '/', 'prum', 'pow', 'quit'

# TODO: prohlidnout video z utery a dodelat

def main():
    while True:
        zobraz_nabidku(status)
        proces = input('Vyber: ')
        os.system('cls')

        if proces == 'quit':
            print('Ukoncuji kalkulacku..')
            break
        elif proces in ('+', '-', '*', '/'):
            zakladni_operace()
        elif proces == 'prum':
            prumer()
        elif proces == 'pow':
            umocni_hodnotu()
        else:
            print('Neni v nabidce')

def zobraz_nabidku(*args):
    vypis = ' | '.join(*args)
    oddelovac = '-' * len(vypis)
    print(oddelovac, vypis, oddelovac, sep='\n')


def zakladni_operace():
    celkem = '('        # eval(celkem)
    while True:
        tlacitko = input('Zadavej cisla a po nich operatory, nakonec \'=\': ')

        if tlacitko.isnumeric():
            celkem += tlacitko
        elif tlacitko in ('+', '-'):
            celkem += tlacitko
        elif tlacitko in ('*', '/'):
            celkem += f') {tlacitko} ('
        elif tlacitko == '=':
            celkem += ')'
            print(f'{celkem} = {eval(celkem)}')
            break


def umocni_hodnotu():
    cislo = int(input('Vloz hodnotu: '))
    exponent = int(input('Vloz exponent: '))
    print(f'Vysledek: {cislo ** exponent}')


def prumer():
    # TODO posouzeni vstupu
    text = 'Zadavej postupne cisla (\'quit\' pro konec): '
    zadane_hodnoty = list()

    while (vstup := input(text)) != 'quit':
        if vstup.isnumeric():
            zadane_hodnoty.append(int(vstup))
    print(f'Vysledek: {sum(zadane_hodnoty) / len(zadane_hodnoty)}')





main()

