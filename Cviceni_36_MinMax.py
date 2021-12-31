# Tvým úkolem je vytvořit dvě funkce:
# Funkce my_min(), která imituje built-in funkci min(). Funkce by měla přijmout jakoukoli sekvenci
# a vrátit položku s nejmenší hodnotou.
# Příklad použití:
# >>> my_min([43,45,87,21,23])
# 21

# Funkce my_max(), která imituje built-in funkci max(). Funkce by měla přijmout jakoukoli sekvenci
# a vrátit položku s největší hodnotou.
# Příklad použití:
# >>> my_max([43,45,87,21,23])
# 87

def my_min(x):
    min_num = x[0]
    for number in x[1:]:
        if number < min_num:
            min_num = number
    return min_num


def my_max(x):
    max_num = x[0]
    for number in x[1:]:
        if number > max_num:
            max_num = number
    return max_num


print(my_min([43, 45, 87, 21, 23]))
print(my_max([43, 45, 87, 21, 23]))
