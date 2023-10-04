def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts the input text using the Caesar cipher algorithm.

    Parameters:
        text (str): The input message to be encrypted or decrypted.
        shift (int): The key to shift the letters in the alphabet.
        mode (str): 'e' for encryption, 'd' for decryption.

    Returns:
        str: The encrypted or decrypted message.
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


def main():
    """
    Main function to handle user input and execution of the Caesar cipher.
    """
    print("Welcome to the Caesar Cipher program!")
    mode = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ')
    shift = int(input('Please enter the key (0 to 25) to use.\n> '))

    if mode == 'e':
        text = input('Enter the message to encrypt.\n> ')
    elif mode == 'd':
        text = input('Enter the message to decrypt.\n> ')
    else:
        print('Invalid choice. Please enter either "e" or "d".')
        return

    result = caesar_cipher(text, shift, mode)
    print('Result:', result)


if __name__ == "__main__":
    main()
