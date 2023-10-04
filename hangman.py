import random


def choose_word():
    '''Choose a word randomly from a predefined list of words.'''
    words = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
    return random.choice(words)


def display_word(word, guessed_letters):
    '''
    Display the word with guessed letters filled in, rest as underscores.

    Args:
    word (str): The word to guess.
    guessed_letters (list): List of letters guessed by the player.

    Returns:
    str: The word with correctly guessed letters filled in, rest as underscores.
    '''
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word.strip()


def hangman():
    '''Main function for the hangman game.'''
    word_to_guess = choose_word()
    guessed_letters = []
    tries = 6  # Number of allowed wrong guesses

    print('You have 6 tries left.')
    print('Used letters:')
    print(f'Word: {display_word(word_to_guess, guessed_letters)}')

    while tries > 0:
        guess = input('Guess a letter: ').lower()

        if guess in guessed_letters:
            print('You already guessed that letter.')
        elif guess in word_to_guess:
            guessed_letters.append(guess)
            print('You guessed correctly!')
        else:
            guessed_letters.append(guess)
            tries -= 1
            print(f'Incorrect guess. You have {tries} tries left.')

        print('You have', tries, 'tries left.')
        print('Used letters:', ' '.join(guessed_letters))
        print(f'Word: {display_word(word_to_guess, guessed_letters)}')

        if '_' not in display_word(word_to_guess, guessed_letters):
            print(f'You guessed the word {word_to_guess}!')
            break

    if '_' in display_word(word_to_guess, guessed_letters):
        print(f'Sorry, you ran out of tries. The word was {word_to_guess}.')


# Run the game
if __name__ == "__main__":
    hangman()
