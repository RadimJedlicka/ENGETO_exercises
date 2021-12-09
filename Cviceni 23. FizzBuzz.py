# Napiš program, který tiskne celá čísla od 1 do 100 (včetně).
#
# Ale:
#
# pro násobky 3 vytiskni Fizz (namísto čísla)
# pro násobky 5 vytiskni Buzz (namísto čísla)
# pro násobky 3 _ 5 zároveň vytiskni FizzBuzz (namísto čísla)

for cislo in range(1, 101):
    if cislo % 3 ==0 and cislo % 5 == 0:     # taky slo zapsat if cislo % 15 == 0:
        print("FizzBuzz")
    elif cislo % 5 == 0:
        print("Buzz")
    elif cislo % 3 == 0:
        print("Fizz")
    else:
        print(cislo)