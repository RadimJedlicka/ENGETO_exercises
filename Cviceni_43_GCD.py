# NSD (GCD v angličtině) je zkratka pro největší společný dělitel (Greatest common divisor).
# Tvým úkolem je vytvořit funkci my_gcd, která spočítá NSD dvou celých čísel (integer).
#
# Jak spočítat NSD?
# Můžeme použít modulo operátor. Tím opakovaně spočítáme zbytek dělení mezi číly A a B.
# Pokud se zbytek != 0 (nerovná 0), potom se A stane B a B se stane zbytkem v další iteraci.
# Takto postupujeme, dokud zbytek dělení mezi A a B není 0.

# Reseni vhodne pro cela cisla (integer)
# def my_GCD(x, y):
#     result = []
#     for item in range(1, y+1):
#         if x % item == 0 and y % item == 0:
#             result = item
#     return result


def my_gcd(a, b):
    while b > 1:
        remainder = a % b
        if remainder == 0:
            break
        a, b = b, remainder
    return b


print(my_gcd(4.2658, 81.57))
print(6 % 18)
# print(my_GCD(1.5, 6))


# Vice k GCD zde: https://www.geeksforgeeks.org/gcd-in-python/