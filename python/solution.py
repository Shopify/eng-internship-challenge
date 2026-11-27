def create_playfair_key_square(key):
    """
    Generates a 5x5 key square for the Playfair cipher using the provided key.
    The key square is filled with unique characters from the key followed by the remaining
    letters of the alphabet (excluding 'J', which is merged with 'I').

    Args:
        key (str): The keyword used to generate the key square.

    Returns:
        list: A 5x5 matrix representing the Playfair key square.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")

    # Initialize a set to keep track of seen characters and a list for the key square
    seen_chars = set()
    key_square = []

    # Add unique characters from the key to the key square
    for char in key:
        if char.isalpha() and char not in seen_chars:
            seen_chars.add(char)
            key_square.append(char)

    # Add remaining characters from the alphabet to the key square
    for char in alphabet:
        if char not in seen_chars:
            seen_chars.add(char)
            key_square.append(char)

    # Convert the list into a 5x5 matrix
    return [key_square[i:i+5] for i in range(0, 25, 5)]


def decrypt_playfair_cipher(cipherText, keySquare):
    """
    Decrypts a ciphertext encrypted with the Playfair cipher using the provided key square.

    Args:
        ciphertext (str): The encrypted message.
        key_square (list): The 5x5 matrix used for decryption.

    Returns:
        str: The decrypted message.
    """

    def find_position(char):
        """
        Finds the row and column of a character in the key square.

        Args:
            char (str): The character to locate in the key square.

        Returns:
            tuple: A tuple containing the row and column of the character.
        """
        for i, row in enumerate(keySquare):
            if char in row:
                return i, row.index(char)
        return None

    decription = ""

    # Process the ciphertext in pairs of two characters
    for i in range(0, len(cipherText), 2):
        a, b = cipherText[i], cipherText[i+1]
        row_a, col_a = find_position(a)
        row_b, col_b = find_position(b)

        # If the characters are in the same row, replace them with the letters to their immediate left
        if row_a == row_b:
            decription += keySquare[row_a][(col_a - 1) % 5]
            decription += keySquare[row_b][(col_b - 1) % 5]
        # If the characters are in the same column, replace them with the letters immediately above
        elif col_a == col_b:
            decription += keySquare[(row_a - 1) % 5][col_a]
            decription += keySquare[(row_b - 1) % 5][col_b]
        # If the characters form a rectangle, replace them with the letters on the same row but at the opposite corners
        else:
            decription += keySquare[row_a][col_b]
            decription += keySquare[row_b][col_a]

    # replace 'X' from the final string
    return decription.replace("X", "")


if __name__ == '__main__':
    key = "SUPERSPY"
    encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    keySquare = create_playfair_key_square(key)
    decryptedText = decrypt_playfair_cipher(encryptedText, keySquare)
    print(decryptedText)
