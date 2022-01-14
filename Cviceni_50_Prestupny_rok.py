# Vytvoř funkci, která vezme jako vstup integer, který reprezentuje rok a vrátí hodnotu True, pokud je rok přestupný.
# V opačném případě by funkce měla vrátit hodnotu False.
#
# Přestupný rok
# Přestupný rok nastává jednou za 4 léta. Ale tahle podmínka neplatí absolutně.
# Pokud je číslo roku dělitelné 100, rok není přestupný. Tohle ale neplatí, když je číslo roku dělitelné 400.
# tomto případě rok přestupný je.
#
# Příklady:
#
# Roky 1600 a 2000 jsou přestupné, protože jsou dělitelné 4.
    # Čísla 1600 a 2000 jsou ale dělitelná 100, v tom případě by se nemělo jednat o přestupné roky.
    # Je ale splněna další podmínka přestupného roku - dělitelnost 400. Proto jsou roky 1600 a 2000 přestupné.
# Roky 1500 a 1900 jsou dělitelné 4, ale také dělitelné 100. A protože nejsou dělitelné 400, nejsou přestupnými roky.
# Roky 1996 a 2004 jsou přestupné, protože jsou dělitelné 4, ale ne 100 (podmínka dělitelnosti 400 tedy nemusí být dodržena).
#
# Příklad fungující funkce:
# >>> is_leap(1600)
# True
# >>> is_leap(1700)
# False

def is_leap(year):
    if year % 4 == 0 and year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False


is_leap(1700)

# KRATSI VERZE S IF

# def is_leap(y):
# # Pokud je prestupny
# if ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)):
# return True
#
# # Pokud neni prestupny
# else:
# return False

# KRATSI VERZE BEZ IF

# def is_leap(y):
# # Vrati True nebo False v zavislosti na tom, jestli je prestupny
# return ((y % 400 == 0) or (y % 4 == 0 and y % 100 != 0))
