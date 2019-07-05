# gra szubienica

from random import choice

words_database = ['rabarbar']

searched_word = choice(words_database)

hidden_word = ['_ '] * len(searched_word)
#hidden_word = '_ ' * len(searched_word)

attempt_number = 0
is_game_won = False
while attempt_number < 2*len(searched_word):
    letter = input('Guess a letter: ')

    index = 0
    for character in searched_word:
        if character == letter:
            hidden_word[index] = letter
        index += 1
    print(hidden_word)
    print(' '.join(hidden_word))

    if'_' not in hidden_word:
        is_game_won = True
        break

    attempt_number += 1
if is_game_won:
    print('You won!')
else:
    print('You lost!')

if attempt_number == 5:
    break

