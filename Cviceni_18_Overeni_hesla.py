data = {'uzivatel1': 'heslo1', 'Marek': '1234', 'Danko': 'qwert'}

# V tomto úkolu se pokusíme ověřit, jestli heslo vložené uživatelem skutečně patří k jeho účtu.

name = input("Uzivatelske jmeno: ")
password = input("Heslo: ")

if data.get(name) == password:
    print("Povoleni pokracovat!")
else:
    print("Heslo nebo uzivatelske jmeno je spatne!")
