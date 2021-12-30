# Tvým úkolem je vytvořit funkci s názvem my_reversed, která bude imitovat built-in funkci reversed().
# Funkce vezme jakoukoli sekvenci jako vstup a vrátí list prvků v opačném pořadí.
#
# Příklad použití naší funkce:
# >>> my_reversed(range(10))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# >>> my_reversed(['New', 'Years', 'Eve'])
# ['Eve', 'Years', 'New']
# >>> my_reversed('Hello World')
# ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'l', 'e', 'H']
# ===============================================================================

# můžeme použít slicing, abychom obrátili pořadí dané sekvence a potom ji převedeme na list
def my_reversed(x):
    return list(x[::-1])

# nebo můžeme použít for loop, kde každá iterace vloží aktuální prvek na začátek nově vytvořené sekvence
def my_reversed2(x):
    lst = []
    for _ in x:
        lst.insert(0, _)
    return lst


print(my_reversed2(range(10)))
