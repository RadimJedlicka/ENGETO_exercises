# Vytvoř funkci, která spočítá průměrnou hodnotu pro danou sekvenci číselných hodnot.

# Definice funkce mean
def my_mean(x):
    result = 0
    for item in x:
        result += item
    return result / len(x)

# zkracene:
# def mean(values):
#     return sum(values)/len(values)


# Nase data
data = [32, 43, 54, 54, 76, 21, 62, 83, 52, 58]

# Pouziti a funkce mean a tisk vysledku
print(my_mean(data))
