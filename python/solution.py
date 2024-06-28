def generate_matrix(key):
    """
    Creates a 5x5 matrix for the Playfair cipher from the given key.
    Converts the key to uppercase and treats 'I' and 'J' as the same letter.
    """
    key = key.upper().replace('J', 'I')  # Replace 'J' with 'I'
    key_and_letter = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    unique_characters = ""
    seen = set()

    for char in key_and_letter:
        if char not in seen and char.isalpha():  # Check for unique alphabetic characters
            seen.add(char)
            unique_characters += char

    return unique_characters

def locate_character(char, matrix):
    """
    Finds the row and column of a character in the matrix string.
    """
    index = matrix.index(char)
    return divmod(index, 5)

def playfair_decrypt(ciphertext, key):
    """
    Decrypts a ciphertext using the Playfair cipher decryption method.
    """
    matrix = generate_matrix(key)
    decrypted_text = ""

    for i in range(0, len(ciphertext), 2):
        row1, col1 = locate_character(ciphertext[i], matrix)
        row2, col2 = locate_character(ciphertext[i + 1], matrix)

        if row1 == row2:
            # If the characters are in the same row, shift left
            decrypted_text += matrix[(row1 * 5) + ((col1 - 1) % 5)]
            decrypted_text += matrix[(row2 * 5) + ((col2 - 1) % 5)]
        elif col1 == col2:
            # If the characters are in the same column, shift up
            decrypted_text += matrix[5 * ((row1 - 1) % 5) + col1]
            decrypted_text += matrix[5 * ((row2 - 1) % 5) + col2]
        else:
            # If the characters form a rectangle, swap columns
            decrypted_text += matrix[(row1 * 5 + col2)]
            decrypted_text += matrix[(row2 * 5 + col1)]

    # Clean up the decrypted text by removing 'X' used as padding
    decrypted_text = decrypted_text.replace("X", "")
    decrypted_text = decrypted_text.replace(" ", "")

    return decrypted_text

if __name__ == "__main__":
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = playfair_decrypt(encrypted_message, key)
    print(decrypted_message)
