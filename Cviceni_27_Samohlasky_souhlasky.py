# Napiš skript, který spočítá kolik samohlásek _ souhlásek obsahuje následující string s anglickou větou:
#
# sentence = 'A speech sound that is produced by comparatively open configuration of the vocal tract.'
# Výstup:
#
# No. consonants: 43 | No. vowels: 30
# V řešení svého kódu použij:
#
# membership test,
# metody stringu,
# vkládání nových hodnot do slovníku,
# vnořené smyčky.

sentence = 'iiiiicdeio.'

vowels = "aeiouy"

pocty = {"consonants": 0,
         "vowels": 0}

for letter in sentence:
    if not letter.isalpha():
        continue
    if letter in vowels:
        pocty["vowels"]+=1
    else:
        pocty["consonants"]+=1

print(pocty["consonants"])
print(pocty["vowels"])
