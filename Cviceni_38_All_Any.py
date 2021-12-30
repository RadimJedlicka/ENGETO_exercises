# Tvým úkolem je vytvořit 2 funkce:
#
# Funkce my_all(), která imituje built-in funkci all().
# Funkce bude brát sekvenci a vrátí True, pokud mají všechny prvky v sekvenci boolean hodnotu True
# nebo pokud je sekvence prázdná. Jinak fuknce vrací False.
#
# Příklad použití naší funkce:
# >>> my_all([43,45,87,21,23])
# True
# >>> my_all([])
# True
# >>> my_all([0,12,431,3])
# False

# Funkce my_any(), která imituje built-in funkci any().
# Funkce bude brát sekvenci a vrátí True, pokud má aspoň jeden prvek v sekvenci boolean hodnotu True.
# V opačném případě a také pokud je sekvence prázdná vrací fuknce False.
#
# Příklad použití naší funkce:
# >>> my_any([43,45,87,21,23])
# True
# >>> my_any([])
# False
# >>> my_any([0,12,431,3])
# True
# >>> my_any(['',[],(),0])
# False

a = [1, 45, 87, 21, 23]
b = [0, 1]

def my_all(x):
    for _ in x:
        if not _:
            return False
    return True


my_all(a)
print(my_all(a))


def my_any(x):
    for _ in x:
        if _:
            return True
    return False


my_any(b)
print(my_any(b))
