# Zadej rozměry šachovnice
size = 3

# Zadej symboly
symbols = ("[O]", "[_]")

# Vytvoř šachovnici

# Doplň smyčky for, které by měly postupně nahrát celou
# šachovnici do proměnné 'desk'

# Naše šachovnice na začátku je prázdný sequence, který má být naplněn dalšími listy. Další listy představují jednotlivé linie šachovnice.
# Využíváme 2členného listu (symbols), který obsahuje symbol '#' _ mezeru ' '.
# Z tohoto pak pomocí vnořených for loop nahráváme dané symboly do linie (vnitřní for loop) _ tu pak do šachovnice (vnější for loop).
desk = []
for row in range(size):
    line = []
    for cell in range(size):
        i = (row+cell) % len(symbols)
        line.append(symbols[i])

# Jádrem celého skriptu je příhodné použití operátorů v tomto zápise i = (row+cell) % len(symbols).
# Tato rovnice vlastně vybere vhodný index (0, nebo 1) pro náš 2členný sequence (symbols)
# _ nahraje buď '#', když je zbytek rovnice 0, nebo ' ', když je zbytek rovnice 1

    desk.append(''.join(line))
print("\n".join(desk))
# Vytiskni šachovnici.
   #
   #      <^>
   #     '/g\'
   #    '/$$g\'
   #   '/$#$#g\'
   #  '//VESELE\'
   # '///VANOCE\\'
   #     _|_|_

