import random

hangman_word_bank = ['python', 'java', 'kotlin', 'javascript']


def word_selector(word_list):
    return random.choice(word_list)


def hide_the_word(word):
    split_dashed_word = list(word)
    for y in range(0, len(split_dashed_word)):
        split_dashed_word[y] = '-'
    return split_dashed_word


def hidden_game_word_print(word):
    print()
    word_string = ''.join(word)
    print(word_string)
    return word_string


def game_end_excitement(word):
    word_excitement = word + '!'
    print('You guessed the word', word_excitement)
    print('You survived!')


def hidden_game_word_reveal(guess, word, hidden_word_list):
    i = 0
    if guess not in hidden_word_list:
        for _ in word:
            if _ == letter_guess:
                del hidden_word_list[i]
                hidden_word_list.insert(i, guess)
            i += 1


def menu():
    selection = str(input('Type "play" to play the game, "exit" to quit: '))
    if selection == "play":
        return
    elif selection == "exit":
        exit()


print('H A N G M A N')

selected_game_word = word_selector(hangman_word_bank)
hidden_game_word_list = hide_the_word(selected_game_word)
selected_game_word_set = set(selected_game_word)
letter_guess_set = set()
number_of_guesses = 0

menu()

while number_of_guesses <= 7:
    hidden_game_word_string = hidden_game_word_print(hidden_game_word_list)
    if hidden_game_word_string != selected_game_word:
        letter_guess = str(input('Input a letter: '))
        if len(letter_guess) != 1:
            print("You should input a single letter")
        elif letter_guess in letter_guess_set:
            print("You've already guessed this letter")
        elif letter_guess.isalpha() and letter_guess.islower():
            if letter_guess in selected_game_word_set:
                hidden_game_word_reveal(letter_guess, selected_game_word, hidden_game_word_list)
            elif letter_guess not in selected_game_word_set:
                print("That letter doesn't appear in the word")
                number_of_guesses += 1
            letter_guess_set.add(letter_guess)
        else:
            print("Please enter a lowercase English letter")
    else:
        game_end_excitement(selected_game_word)
        break
if number_of_guesses >= 8:
    print('You lost!')