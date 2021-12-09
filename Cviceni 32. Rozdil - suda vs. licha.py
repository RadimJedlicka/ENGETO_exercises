# Napiš Python skript, který sečte odděleně všechna sudá a všechna lichá čísla ze seznamu. Na konci by měl program
# vytisknout absolutní hodnotu rozdíu mezi těmito součty.
#
# Ukázka, jak by měl program fungovat:
#
# Máme seznam čísel: [1, 2, 3, 4, 5, 6, 7, 8],
# sečteme všechna sudá čísla a výsledek uložíme do proměnné suda = 2 + 4 + 6 + 8,
# sečteme všechna lichá čísla a výsledek uložíme do proměnné licha = 1 + 3 + 5 + 7,
# nakonec získáme rozdíl mezi těmito dvěma součty (proměnná vysledek),
# měli bychom zajistit, že výsledek nebude záporné číslo (k tomu by ti mohly pomoci built-in funkce pro numerické typy,
# zmiňované v první lekci).
# Tvým ukolem je zjistit, jak iterovat každým prvkem v seznamu čísel, ne psát součet manuálně.

cisla = [386, 462, 47, 418, 907, 344, 236, 375, 823,
        566, 597, 978, 328, 615, 953, 345, 399, 162,
        758, 219, 918, 237, 412, 566, 826, 248, 866,
        950, 626, 949, 687, 217, 815, 67, 104, 58, 512,
        24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
        742, 717, 958,743, 527]

suda = 0
licha = 0

for cislo in cisla:
        if cislo % 2 == 0:
                suda = suda + cislo
        else:
                licha = licha + cislo
print(suda)
print(licha)

vysledek = abs(suda - licha)
print(vysledek)

print(f"Rozdil je: {vysledek}")


# Čísla uložíme do proměnné cisla,
# vytvoříme 2 proměnné (suda a licha),
# v proměnné cisla procházím jedno číslo za druhým,
# pokud je číslo sudé, navýšíme proměnnou suda,
# pokud je číslo liché, navýšíme proměnnou licha,
# nakonec vypočítáme rozdíl mezi suda a licha, získáme jeho absolutní hodnotu pomocí funkce abs()

