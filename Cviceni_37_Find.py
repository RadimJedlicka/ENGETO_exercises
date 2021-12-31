# Tvým úkolem je vytvoři funkci my_find, která bude imitovat built-in metodu pro string .find().
# Funkce bude brát 2 argumenty:
# jakoukoli sekvenci, kterou chceme prohledat
# položku, kterou chceme najít

# Návratová hodnota by měla být:
# index, na kterém se položka nachází v případě, že jsme položku našli
# -1, pokud jsme položku nenašli
# Pamatuj, že velká a malá písmena jsou rozdílné položky.
#
# Příklad fungující funkce:
#
# >>> my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , {'name': 'John'})
# 4
# >>> my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}] , 'banana')
# -1

def my_find(sekvence, findit):
    if findit in sekvence:
        return sekvence.index(findit)
    return -1


print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}], {'name': 'John'}))
print(my_find(['pear', 'apple', (23, 45), 653, {'name': 'John'}], 'banana'))
print(my_find('aaaaaaaab', 'b'))
print('aaaaaaaaaaabbbbeeeee'.find('b'))


# jine reseni:

def my_find2(seq, item):
    for i, obj in enumerate(seq):
        if obj == item:
            return i
    return -1


print(my_find2(['pear', 'apple', (23, 45), 653, {'name': 'John'}], {'name': 'John'}))
