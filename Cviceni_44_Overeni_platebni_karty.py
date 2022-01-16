# Tvým úkolem je vytvořit funkci luhn, která ověří číslo kreditní karty na základě tzv.
# Luhnova testu. Luhnův test používají některé bankovní společnosti k rozpoznání
# platného čísla dané kreditní karty od náhodně poskládaných číslic.

# Ověření pomocí Luhnova testu vypadá následovně:

# 1. Obrátí se pořadí číslic v čísle.
# 2. Vezme se první, třetí...a každá další lichá číslice v tomto obráceném pořadí a sečte do sumy s1.
# 3. Potom se vezme druhé, čtvrté...a každá sudá číslice a:
#   a. Každá číslice se vynásobí dvěma. Pokud je číslo získané násobením větší než 9, sečteme jeho číslice.
#   b. Sečteme všechny sudé číslici, které prošli násobením a upravením do s2.
# 4. Pokud s1 + s2 končí 0, potom lze původní číslo považovat za platné číslo kreditní karty.

# Výstupem programu by měly být hodnoty True nebo False v závislosti na tom,
# jestli je dané číslo platební karty platné, nebo ne.


# Definice fce
def luhn(num) -> bool:
    num_str = str(num)
    num_rev = num_str[::-1]

    s1 = 0
    s2 = 0

    for index, number in enumerate(num_rev):
        if index % 2 == 0:
            s1 += int(number)
        else:
            number = int(number) * 2
            if number > 9:
                number = int(str(number)[0]) + int(str(number)[1])
            s2 += int(number)

    return True if (s1 + s2) % 10 == 0 else False



# Cislo platebni karty obracene
num = 61789372994

# Zavolani fce
print(luhn(num))