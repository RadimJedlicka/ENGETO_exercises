start = int(input("start: ".upper()))
stop = int(input("stop: ".upper()))
divisor = int(input("divisor:".title()))

if divisor == 0:
    print("Cannot divide by zero")
else:
    vysledek = []
    for number in range(start, stop + 1):
        if number % divisor == 0:
            vysledek.append(number)
    print(
        f"Numbers in range ({start},{stop}) divisible by {divisor}:",
        vysledek, sep="\n"
    )