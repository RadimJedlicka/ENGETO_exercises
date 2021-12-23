import os
from slova import hadana_slova
from random import choice, seed
from grafika import obesenec
from grafika import title

lives = 7
running = True
seed(42)
word = choice(hadana_slova)
key = len(word) * ["_"]
message = ''
control = []

while running and lives > 0:
    os.system("cls")
    print(title)
    print('Your task is to guess a letter of our secret word'.center(54))
    print('(or the whole word, if you are brave)'.center(54))
    print("Searched word: ", ''.join(key).center(54))
    print(obesenec[7-lives])
    print(f"{lives} lives remaining".center(54))
    print(message.center(54))
    guess = input('Guess letter/word: '.center(54))
    if guess == word:
        running = False
    elif guess in control:
        message = 'You tried this one already ;-)'
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
    if running == False:
        os.system("cls")
        print(title)
        print('BINGO, YOU ARE THE WINNER!')
    else:
        os.system("cls")
        print(title)
        print(f"{lives} lives remaining".center(15 + len(key)))
        print(obesenec[7 - lives])
        print('YOU ARE DEAD')
