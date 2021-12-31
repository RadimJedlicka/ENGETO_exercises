# Definice funkce sum

# Data k secteni
data = [32,43,54,54,76,21,62,83,52,58]

# Pouziti a funkce sum na data a tisk vysledku


def my_sum(x):
    result = 0
    for number in x:
        result += number
    return result


print(my_sum(data))