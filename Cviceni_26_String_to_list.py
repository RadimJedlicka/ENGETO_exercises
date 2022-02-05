# Tvým úkolem bude napsat skript, který příjme od uživatele string s čísly, která jsou oddělena čárkou
# _ vygeneruje sequence celých čísel ze zadaného stringu (datový typ integer). Program by měl následně sequence vypsat.
#
# Také budeš muset ošetřit kód tak, aby si uměl poradit se situací, kdy by součástí stringu byly mezery.
#
# Příklad fungování kódu:
#
# Hello, please write your numbers and press enter to confirm: '23, 54, 645, 76'
# List: [23, 54, 645, 76]
# Pracuj s následujícími proměnnými:
#
# inpt - získej vstup uživatele
# nums - vlož čísla do listu s mezerama
# result - vlož čísla do listu bez mezer

inpt = str(input("Hello, please write your numbers and press enter to confirm: "))
nums = inpt.split(",")
result = []

for cislo in nums:
    result.append(int(cislo))

print(result)



