import os


status = '+', '-', '*', '/', 'prum', 'pow', 'quit'


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


def zobraz_nabidku(*args) -> None:
    """
    Popisek:
    Metodou 'join' spoji hodnoty v parametrech 'args', na zacatku a na konci bude '|'
    Potom doplni oddelovac pred a za parametry

    Ukazka:
    args = ('a', 'b', 'c')

    Vysledek:
    -------------
    | a | b | c |
    -------------
    """
    vypis = ' | '.join(*args)
    oddelovac = '-' * len(f"| {vypis} |")
    print(oddelovac, f"| {vypis} |", oddelovac, sep='\n')


def ciselny_vstup(popisek='Hodnota: ') -> int:
    while True:
        vstup = input(popisek)
        if je_vstup_ciselny(vstup):
            return int(vstup)
        else:
            print('Neplatny vstup, zadej znovu')


def je_vstup_ciselny(vstup) -> bool:
    return (vstup[0] == '-' and vstup[1:].isdigit()) or vstup.isdigit()


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


def umocni_hodnotu() -> None:
    cislo = ciselny_vstup()
    exponent = ciselny_vstup('Mocnina: ')
    print(f'Vysledek: {cislo} ** {exponent} = {cislo ** exponent}')  # printout exponent jde, viz google
    # return cislo ** exponent -> int


def prumer() -> None:
    text = 'Zadavej postupne cisla (nakonec zadej \'=\'): '
    zadane_hodnoty = list()

    while (vstup := input(text)) != '=':
        if je_vstup_ciselny(vstup):
            zadane_hodnoty.append(int(vstup))
    print(f'Prumer zadanych hodnot {tuple(zadane_hodnoty)} \n'
          f'se rovna: {sum(zadane_hodnoty) / len(zadane_hodnoty)}')


main()
