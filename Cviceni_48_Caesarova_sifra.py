# Caesarova šifra je typ nahrazovací šifry, ve které je každé písmeno nahrazeno písmenem,
# které se abecedně nachází o pevně určený počet míst dále. Tato metoda šifrování se jmenuje po Juliu Caesarovi,
# který šifrování používal ve své osobní korespondenci.

# Ceasarova šifra v praxi:

# S posunem o 3 DOLEVA (-3) by písmeno D bylo nahrazeno písmenem A, E by bylo nahrazeno B, atd.
# S posunem o 3 DOPRAVA (3) by písmeno D bylo nahrazeno písmenem G, E by bylo nahrazeno H, atd.

# Příklad fungující funkce:
# >>> message = 'abc def ghi jkl mno pqr stu vwx Yz'
# >>> caesar(message,2)
# cde fgh ijk lmn opq rst uvw xyz Ab
# >>> caesar(message,-2)
# yza bcd efg hij klm nop qrs tuv Wx
# --------------------------------------------------

# Zprava
message = 'abc def ghi jkl mno pqr stu vwx Yz'
shift = -1


# Definice fce caesar
def caesar(seq, shift: int):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_string = []

    for letter in seq:
        if letter.lower() not in alphabet:
            new_string.append(letter)
            continue

        position = alphabet.index(letter.lower())
        index = (position + shift) % len(alphabet)

        if letter.isupper():
            new_letter = alphabet[index].upper()
        else:
            new_letter = alphabet[index]

        new_string.append(new_letter)

    return ''.join(new_string)


# Zavolani fce
print(caesar(message, shift))
