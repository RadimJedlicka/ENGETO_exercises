import os
from slova import hadana_slova
from random import choice, seed
from grafika import obesenec, title

def main():
    lives = 7
    running = True
    seed(42)
    word = choice(hadana_slova)
    key = len(word) * ["_"]
    message = ''
    control = []

    while running and lives > 0:
        uvod(key, title, message, lives, control)
        guess = input('           Guess letter/word2: ')
        if guess == word:
            running = False
        elif guess in control:
            message = 'You have tried this one already ;-)'
        elif len(guess) == 1 and guess in word:
            control.append(guess)
            message = 'You have found a letter'
            for index, symbol in enumerate(word):
                if symbol == guess:
                    key[index] = guess
            if '_' not in key:
                running = False
        elif guess not in word:
            control.append(guess)
            message = "WRONG"
            lives -= 1
        else:
            print('WRONG')
            lives -= 1
            if lives == 0:
                running = False
    else:
        if running is False:
            os.system("cls")
            print(title)
            print('BINGO, YOU ARE THE WINNER!'.center(54))
            print('searched word2 was'.upper().center(54), f"'{word}'".center(54), sep="\n")
        else:
            os.system("cls")
            print(title)
            print(f"{lives} lives remaining".center(15 + len(key)))
            print(obesenec[7 - lives])
            print('YOU ARE DEAD')

def uvod(key, title, message, lives, control):
    os.system("cls")
    print(title)
    print('Your task is to guess a letter of our secret word2\n(or the whole word2, if you are brave)'.center(54))
    print('')
    print(' ' * 10, "Searched word2: ", ''.join(key))
    print(message.center(54))
    print('Already used: ', control)
    print(obesenec[7 - lives].center(54))
    print(f"{lives} lives remaining".center(54))


main()