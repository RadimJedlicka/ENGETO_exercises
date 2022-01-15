import random

### Funkce main()
# Definice funkce
def main(words):
    # Náhodný výběr hádaného slova
    word = random.choice(words)

    # My jme se rozhodli nastavit pocet pokusu na 1.6 delky slova
    lives = int(len(word))

    # Promenna pro vizualizaci
    status = ['_'] * len(word)

    # Veta na uvod
    print('I am thinking of a word. What word is it?')
    # While loop
    while True:

        # Pouziti 2. funkce get_letter
        letter = get_letter(status, lives)

        # Pouziti 3. funkce replace_letters
        replace_letters(letter, word, status, lives)

        # Odecteni pokusu

        lives = lives - 1
        print('No, the letter ' + letter + ' is not in my word')

        # While konci pokud je vse uhadnuto
        if '_' not in status:
            print('\nCongatulations, you have won!\n')
            break

        # While konci pokud dojdou pokusy
        if not lives:
            print('\nYou have lost. The word was:\n' + word)
            break


### Funkce get_letter()
# Definice funkce
def get_letter(status, lives):
    # Vizualizace
    print(' '.join(status))

    # Ziskani vstupu od uzivatele
    letter = input('Guess a letter | guesses available: '
                   + str(lives) + '\n')

    # Vraceni vstupu od uzivatele
    return letter


### Funkce replace_letters()
# Definice funkce
def replace_letters(letter, word, status, lives):
    # Pocet nahrazeny pismen
    count_replaced = 0

    # For loop pro zjisteni poctu a nahrazeni uhadnuteho pismene
    for i, char in enumerate(word):
        if char == letter:
            status[i] = letter
            count_replaced += 1
    # Pokud jsme neco nahradili
    if count_replaced:
        print(f'Yes, there is {count_replaced} letter {letter.title()}.')
    # Pokud jsme nic nenahradili




### Spuštění programu
# Nase slova
words = ['Hangman', 'available', 'increase']
# Spusteni fce main a vlozeni slov
main(words)
