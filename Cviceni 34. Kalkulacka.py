# Tvým úkolem v této části bude napsat jednoduchý skript, který bude umět provádět se dvěma zadanými hodnotami
# volitelné matematické operace (součet, odčítání, násobení, dělení)
# Řekněme, že si uživatel vybere cislo01 = 3 _ cislo02 = 4.
# Dále si vybere, že chce provést operaci soucet. Výsledkem by měl vypsaný výpočet 3 + 4 = 7.
#
# Nejprve si ukážeme, jak bychom měli u tvorby takového kódu přemýšlet.
#
# Na začátek budeme chtít pozdravit uživatele _ říct, aby vepsal dvě libovolná čísla.
# Další částí bude nadepsaný výběr operací, které může s čísly provádět.
# Nakonec budeme potřebovat spojit operaci, kterou uživatel vybral s výpočtem, který má provést _ následně vypsat.
# Pomocí cyklu bychom chtěli zopakovat, aby se uživateli nabízely operace tak dlouho, dokud je nebude chtít příkazem ukončit.


cislo01 = (input("Hello, choose 1. number: "))
cislo02 = (input("Hello, choose 2. number: "))
# vstup = input('Vyber si operaci:')
operace = ['+','-','*','/']

while True:
    vstup = input('''
--------------------------------
Choose operation from available:
for addition:       type '+'
for subtraction:    type '-'
for multiplication: type '*'
for  division:      type '/'
     press 'X' to finish
--------------------------------
What is your selection?
''')
    if vstup == '+':
        print(str(cislo01), vstup, str(cislo02), '=', int(cislo01) + int(cislo02))
    elif vstup == '-':
        print(str(cislo01), vstup, str(cislo02), '=', int(cislo01) - int(cislo02))
    elif vstup == '*':
        print(str(cislo01), vstup, str(cislo02), '=', int(cislo01) * int(cislo02))
    elif vstup == '/':
        print(str(cislo01), vstup, str(cislo02), '=', int(cislo01) / int(cislo02))
    else:
        vstup = 'x' or vstup not in operace
        print('See you next time')
        break

# vzorove reseni z webu

# # Pozdrav uživatele _ umožni mu zapsat dvě vstupní proměnné
# print('Ahoj, nejprve vyber dvě čísla! :)')
# print()
# number01 = int(input('Prosím, zadejte prvni číslo: '))
# number02 = int(input('Prosím, zadejte druhé číslo: '))
# # Tento text nechceme opakovat, proto patří před smyčku while
# print('Nyní vyber operaci, kterou chceš s čísly provést: ')
# print()
# # Zapiš nekonečnou smyčku
# # mod kalkulacky je ON
# # Podminka nekonecne smycky
# mod = True
# while mod == True:
# # Vypiš jaké operace může uživatel provádět _ možnost zapsat input()
#     choice = str(input('''
# ------------------------
# Sčítání:    "sci",
# Odčítání:   "odc",
# Násobení:   "nas",
# Dělení:     "del",
# Ukonči:     "off",
# ----------------------
# Vyber si operaci: '''))
#     # Sem zapiš podmínky, které spojí tebou nabízené operace _ následný print() výsledku
#     if choice == 'sci':
#         print(str(number01)+ ' + ' + str(number02) + ' = ' + str(number01 + number02))
#     elif choice == 'odc':
#         print(str(number01) + ' - ' + str(number02) + ' = ' + str(number01 - number02))
#     elif choice == 'nas':
#         print(str(number01) + ' * ' + str(number02) + ' = ' + str(number01 * number02))
#     elif choice == 'del':
#         print(str(number01) + ' / ' + str(number02) + ' = ' + str(number01 / number02))
#     elif choice == 'off': # prepnu mod OFF
#         print('Počtům zdar!')
#         mod = False


