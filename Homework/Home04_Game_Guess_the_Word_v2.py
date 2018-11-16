__author__ = 'stanislav-kuhtinski'

import random
import traceback

MAX_ERRORS = 10
EXIT_FLAG = None


# generates random word from tuple
def generate_random_word():
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
    return random.choice(words_to_guess)


def init_word_statuses(rnd_word):
    statuses = []
    print('\n!!!New game!!!')
    # print('Random word is {}, its length is {}'.format(rnd_word, len(rnd_word)))
    for letter in rnd_word:
        statuses.append(False)
    return statuses


def check_word_statuses(rnd_word, answ_letter, statuses):
    if answ_letter not in rnd_word:
        print('Oops, this word does not contain this letter ', answ_letter)
        return False

    for index, letter in enumerate(rnd_word):
        if answ_letter == letter:
            statuses[index] = True
    print('Great, you have guessed the letter right!')
    return True


def ask_user_input():
    try:
        user_input = str(input('Please guess the letter: '))
        return user_input
    except ValueError:
        print('Error value, all values should be letters')
    except TypeError:
        print('Error type, all values should be letters')
    except Exception as error:
        message = traceback.format_exc()
        print('Exception! Error code is ', error, message)


def check_game_status(statuses, mistakes_counter, usr_answer):
    if mistakes_counter >= MAX_ERRORS:
        return True
    elif usr_answer == ('exit'):
        global EXIT_FLAG
        EXIT_FLAG = True
        return True
    for status in statuses:
        if not status:
            return False
    return True


def print_word(word, statuses):
    print('Here is the word looks like now: ')
    for index, letter in enumerate(word):
        if statuses[index]:
            print(letter, end=' ')
        else:
            print('*', end=' ')
    print(' ')


def print_afterword(mistakes, rnd_word):
    if mistakes >= MAX_ERRORS:
        print('Too many mistakes! You lose! Game over!')
    elif check_for_exit():
        print('Exiting the game!')
    else:
        print('Great! You have guessed the word correctly! The word I\'ve picked up was - ', rnd_word)
        print('Game over!\n')


def check_for_exit():
    if EXIT_FLAG:
        return True
    return False


def main():
    print(
        'Hi, I would like to play a game with you. \nI will pick up an English word, try to guess the letters.\nYou have {} lives. Type "Exit" to leave.'.format(
            MAX_ERRORS))
    print('Let\'s begin!\n')
    while not check_for_exit():
        random_word = generate_random_word()
        statuses = init_word_statuses(random_word)
        mistakes_counter = 0

        for i in range(0, len(random_word) + MAX_ERRORS - 1):
            print_word(random_word, statuses)
            usr_answer = ask_user_input()
            result = check_word_statuses(random_word, usr_answer, statuses)

            if check_game_status(statuses, mistakes_counter, usr_answer):
                break
            elif not result:
                mistakes_counter += 1

        print_afterword(mistakes_counter, random_word)


main()