import os # os.system('cls')

status = '+', '-', '*', '/', 'prum', 'pow', 'quit'

# TODO: zobrazit nabidku
# TODO: nechat uzivatle vybrat
# TODO: provest vybrany proces
# TODO: .. a znovu

def zobraz_nabidku(*args):
    vypis = ' | '.join(*args)
    oddelovac = '-' * len(vypis)
    print(oddelovac, vypis, oddelovac, sep='\n')


while True:
    zobraz_nabidku(status)
    proces = input('Vyber: ')

    if proces == 'quit':
        print('Ukoncuji kalkulacku..')
        break
    elif proces in ('+', '-', '*', '/'):
        print('Zakladni matematicke operace')
    elif proces == 'prum':
        print('Pocitam prumer')
    elif proces == 'pow':
        print('Umocnuji')
    else:
        print('Neni v nabidce')