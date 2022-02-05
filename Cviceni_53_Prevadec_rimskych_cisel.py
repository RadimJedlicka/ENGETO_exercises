# Tvým úkolem je vytvořit skript, který bude obsahovat dvě funkce:

# to_roman() - převede arabské říslo na římské,
# to_arab() - převede římské číslo na arabské.
# Příklad
# | Římské číslo | Arabské číslo |
# | I | 1 |
# | V | 5 |
# | X | 10 |
# | L | 50 |
# | C | 100 |
# | D | 500 |
# | M | 1,000 |
# Nezapomínej na pravidla římských čísel. Čísla jako je 4, 40, 90 se zapisují následovně:
# IV = 4, IX = 9, atp. Podobně je to i s vyššími čísly.
# Pokud chceš například vyjádřit číslo 40, zapíšeš před číslici L, číslici X(XL = 40).

# Ve výsledku by funkce měly vypadat následovně:

# to_arab('MMMCMXCIX')
# ...vrátí:
# 3999

# ...a zpátky:

# to_roman(3999)
# ...vrátí:
# MMMCMXCIX

# Převaděč by měl fungovat až do čísla 3999.


def to_arab(roman):
    mapping1 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    mapping2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    # Číslo roman postupně zmenšujeme, nakonec zbyde prázdný string
    while roman:
        if roman[:2] in mapping1:
            num = roman[:2]
            roman = roman[2:]
            mapping = mapping1
        else:
            num = roman[:1]
            roman = roman[1:]
            mapping = mapping2

        result += mapping[num]

    return result

print(to_arab('XXXCV'))


# def to_roman(arab): # 1, 2, 5, 10, 50, 100
#     mapping = {1: 'I', 5: 'V', 10: 'C', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
#     result = ''
#     while arab:
#         if arab in mapping:

def to_roman(num):
    result = ''
    mapping = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
               500: 'D',
               900: 'CM', 1000: 'M'}
    for arab in sorted(mapping, reverse=True):
        roman = mapping[arab]
        result += num // arab * roman
        num %= arab
    return result

print(to_arab("MMXX"))
print(to_roman(2020))






# def to_arab(vstup):
#     cislo = 0
#
#     numbers_1_5(vstup)
#
#     return cislo
#
#
# def numbers_1_5(vstup):
#     cislo = 0
#     konec = vstup[-3:]
#     if 'V' in vstup[0]:
#         cislo += 5
#
#     try:
#         if 'V' in vstup[1]:
#             cislo += 4
#     except IndexError:
#         pass
#
#     if 'I' in konec and 'V' not in konec:
#         cislo += (1 * konec.count('I'))
#
#     return cislo


# print(to_arab('V'))
