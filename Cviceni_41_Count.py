# Vytvoř funkci, která zjišťuje počet výskytů daného prvku.
# Jako vstup bere prvek, který hledáme a sekvenci, ve které ho chceme najít.

# Definice funkce count
def my_count(x, y):
    count = 0
    for item in y:
        if item == x:
            count += 1
    return count


# Nase data
names = ['Rob', 'Jim', 'Mark', 'Mark', 'Mark', 'Bob', 'Mark', 'Bob', 'Bob', 'Rob', 'Jim', 'Mark', 'Mark', 'Bob', 'Mark']

# Pouziti funkce count a tisk vysledku

print(my_count('Rob', names))
