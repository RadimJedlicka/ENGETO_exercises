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
