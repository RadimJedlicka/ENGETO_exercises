# Nyní bude tvým úkolem vytvořit funkci horizont_hist(), která vezme list čísel jako argument
# a na základě hodnot v tomto listu vytiskne histogram v terminálu.
# Výška sloupce by měla odpovídat hodnotě odpovídajícího čísla v listu.
# Výsledek by měl vypadat nějak takto:
#
# horizont_hist([4,5,7,10,6,3,2])
# Výstup v konzole:
#
# |****
# |*****
# |*******
# |**********
# |******
# |***
# |**


def horizont_hist(list):
    for number in list:
        print(f"|{'*' * number}")


horizont_hist([4,5,7,10,6,3,2])