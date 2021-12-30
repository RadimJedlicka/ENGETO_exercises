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

# ['New', 'Years', 'Eve']
def my_reversed(x):
    return list(x[::-1])


print(my_reversed('New'))
