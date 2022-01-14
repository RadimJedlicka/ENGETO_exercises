# Tvým úkolem bude vytvořit dvě funkce.
#
# Funkce, která vygeneruje list prvočísel do specifikovaného čísla - list_primes.
# Funkce, která vyhodnotí, zda je dané číslo prvočíslem - is_prime.
# Funkce list_primes
# Abychom mohli generovat list prvočísel, použijeme tzv. algoritmus Eratosthenova síta. Ten provádí následující kroky.
#
# Vytvoří list po sobě jdoucích celých čísel (integers) od 2 do n: (2, 3, 4, ..., n).
#
# Počáteční hodnota p se na začátku rovná 2 - nejmenší prvočíslo.
#
# Zjistí násobky p až do n a smaže je. Příklad: 2p, 3p, 4p, 5p, ...; hodnota p se nesmaže.
#
# Najde v listu první číslo větší než p. Pokud takové číslo v listu není, algoritmus ukončí funkci.
# Pokud existuje, přiřadí tuto hodnotu proměnné p. Tato hodnota je vlastně další prvočíslo.
# Algoritmus opakuje postup kroku 3.
#
# Jakmile se algoritmus ukončí, všechna zbylá čísla jsou prvočísla od 2 do n.

# Definice fce list_primes


def list_primes(n):
    integers = list(range(2, n+1))
    result = list()
    while integers:
        p = integers.pop(0)
        result.append(p)
        for number in integers:
            if number % p == 0:
                integers.remove(number)

    return result


# Definice fce is_prime


def is_prime(n):
    return n in list_primes(n)


# # Volani fce is_prime
print(is_prime(23))

#
# Funkce is_prime
# Předchozí funkce list_primes by měla sloužit jako pomocná funkce uvnitř funkce is_prime.
#
# Příklad použití funkce is_prime() pro kontrolu prvočísla:
#
# >>> is_prime(54)
# False
# >>> is_prime(53)
# True
