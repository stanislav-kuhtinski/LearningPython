__author__ = 'stanislav-kuhtinski'

import random

words_to_guess = (
    'gentle', 'pickle', 'kneel', 'cruel', 'flash', 'dead', 'jealous', 'pray', 'hospital', 'babies', 'slimy',
    'ubiquitous',
    'unpack', 'idea', 'sparkle', 'son', 'colour', 'thick', 'young', 'pedal', 'pest', 'one', 'position',
    'shelf',
    'clean', 'combative', 'truthful', 'exultant', 'reflective', 'naive', 'start', 'permit', 'crush', 'shallow',
    'market',
    'remember', 'farm', 'hunt', 'head', 'tour', 'trip', 'pocket', 'consist', 'magic', 'holiday', 'embarrass', 'lie',
    'want',
    'classy', 'screeching', 'mama',)

print(
    'Hi, I would like to play a game with you. \nI will pick up an English word, try to guess the letters.\nYou have 5 lives. Type "Exit" to leave.')
print('Let\'s begin!\n')

answer_letter = 'not exit'


def match_letters(rnd_word, answ_letter, answ_word='*'):
    chars_rnd_word = list(rnd_word)
    chars_answ_word = list(answ_word)
    match = False
    for i in range(len(chars_rnd_word)):
        if chars_rnd_word[i] == answ_letter:
            match = True
            chars_answ_word[i] = answ_letter
    if match:
        return (''.join(chars_answ_word), True)
    else:
        return (''.join(chars_answ_word), False)


while answer_letter != 'exit':
    lives_count = 5
    random_word = random.choice(words_to_guess)
    answer_word = '*' * len(random_word)
    print('\n!!!New game!!!')
    print('Random word is {}, its length is {}'.format(random_word, len(random_word)))

    print('I have picked up a word, please guess letter by letter')

    for i in range(0, len(random_word) + lives_count - 1):
        answer_letter = input('Please guess the letter: ')
        print('The i is ', i)
        answer_word, match_found = match_letters(random_word, answer_letter, answer_word)
        if answer_word == random_word:
            print('Great! You have guessed the word correctly! The word I\'ve picked up was - ', random_word)
            print('Game over!\n')
            break
        elif match_found:
            print('So far you have guessed  ', answer_word)
        else:
            lives_count -= 1
            print(
                'This word does not contain any letters "{}", you have {} tries left. So far you have guessed {}'.format(
                    answer_letter,
                    lives_count,
                    answer_word))
            if lives_count == 0:
                print('All attempts are used! Game over!\n')
                break