import enchant


def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the input text using the Caesar cipher algorithm.

    Args:
        text (str): Input text to be encrypted or decrypted.
        shift (int): Number of positions to shift the letters in the alphabet.
        mode (str): 'e' for encryption, 'd' for decryption.

    Returns:
        str: Encrypted or decrypted text.
    """
    result = ''
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for char in text:
        if char.isalpha():
            char = char.upper()
            if mode == 'e':
                shifted_index = (alphabet.index(char) + shift) % 26
                shifted_char = alphabet[shifted_index]
            elif mode == 'd':
                shifted_index = (alphabet.index(char) - shift) % 26
                shifted_char = alphabet[shifted_index]
        else:
            shifted_char = char
        result += shifted_char
    return result


def is_english_word(word):
    """
    Checks if a given word is an English word.

    Args:
        word (str): Word to be checked.

    Returns:
        bool: True if the word is English, False otherwise.
    """
    dictionary = enchant.Dict('en_US')
    return dictionary.check(word)


def brute_force_attack(ciphertext):
    """
    Performs a brute-force attack to decrypt the Caesar cipher encrypted message.

    Args:
        ciphertext (str): Encrypted message to be decrypted.
    """
    for shift in range(26):
        decrypted_message = caesar_cipher(ciphertext, shift, 'd')
        words = decrypted_message.split()
        all_english = all(is_english_word(word) for word in words)
        if all_english:
            print(f'Shift {shift}: {decrypted_message}')


def main():
    """
    Main function to execute the program.
    """
    ciphertext = input('Enter the encrypted message:\n>')
    brute_force_attack(ciphertext)


if __name__ == "__main__":
    main()
