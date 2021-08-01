import random

# Hangman game available words
hangman_word_bank = ['python', 'java', 'kotlin', 'javascript']


# Function for selecting a word from the word bank at random using system time as the seed
def word_selector(word_list):
    return random.choice(word_list)


# Function for obscuring the selected game word with all '-' so that the player cannot see the word at first.
def hide_the_word(word):
    split_dashed_word = list(word)
    for y in range(0, len(split_dashed_word)):
        split_dashed_word[y] = '-'
    return split_dashed_word


# Function for printing the game word as a string (not a list) at each iteration of the game as the player unlocks
# letters
def hidden_game_word_print(word):
    print()
    word_string = ''.join(word)
    print(word_string)
    return word_string


# Function for properly formatting and printing the selected game word if the player wins the game.
def game_end_excitement(word):
    word_excitement = word + '!'
    print('You guessed the word', word_excitement)
    print('You survived!')


# Function for checking if the player already guessed a word within the hidden word list and if not then it replaces
# the index of the hidden word list with the letter from the selected word list.
def hidden_game_word_reveal(guess, word, hidden_word_list):
    i = 0
    if guess not in hidden_word_list:
        for _ in word:
            if _ == letter_guess:
                del hidden_word_list[i]
                hidden_word_list.insert(i, guess)
            i += 1


# Function for giving the player the option to either play the game and return to the following code for the game or
# exit the game and therefore not run the game code.
def hangman_game_menu():
    print('H A N G M A N')
    selection = str(input('Type "play" to play the game, "exit" to quit: '))
    if selection == "play":
        return
    elif selection == "exit":
        exit()


# Initialize the hangman game by first calling the function to select a word for the game.
# Then call the function to hide the word.
# Then form a set out of the selected game word.
# Then create an empty set for the letters the player guesses.
# Then set the initial number of guesses the player has guessed to 0 because they have not guessed anything yet.
selected_game_word = word_selector(hangman_word_bank)
hidden_game_word_list = hide_the_word(selected_game_word)
selected_game_word_set = set(selected_game_word)
letter_guess_set = set()
number_of_guesses = 0

# Start the hangman game with a menu for the player.
hangman_game_menu()

# The player will get 8 guesses so as long as they have not guessed an incorrect letter 8 times they can keep playing.
while number_of_guesses <= 7:

    # Print the hidden game word after each letter guess
    hidden_game_word_string = hidden_game_word_print(hidden_game_word_list)

    # This loop checks to see if the player has finished the game.
    if hidden_game_word_string != selected_game_word:

        letter_guess = str(input('Input a letter: '))  # Get the guess from the player for each loop.

        # This loop checks to see if the player enters a valid character and if the player has guessed the same
        # character previously.
        if len(letter_guess) != 1:
            print("You should input a single letter")

        elif letter_guess in letter_guess_set:
            print("You've already guessed this letter")

        elif letter_guess.isalpha() and letter_guess.islower():

            # If the player enters a valid character then this loop checks to see if that character exists within the
            # selected game word set. If the character is found then reveal it from the hidden game word. If it is
            # not found then the player loses a guess out of 8.
            if letter_guess in selected_game_word_set:

                hidden_game_word_reveal(letter_guess, selected_game_word, hidden_game_word_list)

            elif letter_guess not in selected_game_word_set:
                print("That letter doesn't appear in the word")
                number_of_guesses += 1

            # Always add the character the player guesses to the letter_guess_set if it is a valid entry. This is to
            # check and see if the player has guessed the valid character previously. The reason this statement
            # appears here in the code is because the set is empty until the player guesses something valid at least
            # one time.
            letter_guess_set.add(letter_guess)

        else:
            print("Please enter a lowercase English letter")

    else:
        # If the player is finished with the game then call the end game function.
        game_end_excitement(selected_game_word)
        break

# Once the player runs out of guesses (8 in this case) print the lose game condition message.
if number_of_guesses >= 8:
    print('You lost!')
