import re

# Global Constant for alphabets
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

# Encrypted message -> encrypted using Playfair cipher
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Decrypted message
decrypted_message = []

# Cipher key used to encrypt the message
key = "SUPERSPY"

def generate_matrix(key) -> list:
    """
    Generate a 5x5 matrix for a given encryption key.

    Parameters:
        key (str): The encryption key used to generate the matrix.

    Returns:
        list: A 5x5 matrix filled with characters based on the encryption key
              and the remaining characters of the alphabet, excluding 'j'.

    Notes:
        - The key is used to populate the matrix first, with unique characters.
        - The remaining empty spaces in the matrix are filled with the
          remaining characters of the alphabet (excluding 'j', as it is ommitted from our alphabet set) in order, 
          skipping those already used in the key.
        - character_set is used to keep track of the characters already used in the creation of the matrix.
        - The matrix is filled row by row.
    """

    # ALPHABET pointer
    alphabet_pointer = 0
    # Key pointer
    key_pointer = 0
    # Key set
    character_set = set()

    # Create a 5x5 matrix and fill it with empty strings
    matrix = []
    for i in range(5):
        matrix.append([])
        for _ in range(5):
            matrix[i].append('')

    # Fill the matrix with the key
    for letter in key:
        if letter not in character_set:
            character_set.add(letter)
            matrix[key_pointer // 5][key_pointer % 5] = letter
            key_pointer += 1
    
    # Fill the matrix with the remaining alphabets
    for i in range(key_pointer // 5, 5):
        for j in range(key_pointer % 5, 5):
            if ALPHABET[alphabet_pointer] not in character_set:
                matrix[i][j] = ALPHABET[alphabet_pointer]
                alphabet_pointer += 1
                key_pointer += 1
            else:
                while ALPHABET[alphabet_pointer] in character_set:
                    alphabet_pointer += 1
                matrix[i][j] = ALPHABET[alphabet_pointer]
                key_pointer += 1
                alphabet_pointer += 1

    return matrix


def generate_pairs(message) -> list:
    """
    Generate pairs from an input cipher text message for decryption.

    Parameters:
        message (str): The message to generate pairs from.

    Returns:
        list: A list of pairs generated from the message for encryption.

    Notes:
        - If two consecutive characters in the message are the same, 
          'X' is added after the first character to maintain pairs (Application of Rule 1).
        - If the message has an odd length, the last character is paired with 'X' (Application of Rule 1).
        - The generated pairs are returned in a list.
    """

    # pairs list from encrypted message
    pairs = []
    # message pointer
    i = 0

    while i < len(message):
        if i + 1 < len(message) and message[i] == message[i + 1]:
            pairs.append(message[i] + 'X')
            i += 1
        else:
            pairs.append(message[i] + message[i + 1])
            i += 2

    return pairs
    
def decrypt_playfair(ciphertext: str, key: str) -> str:
    """
    Decrypts a Playfair cipher using the given key.

    Parameters:
        ciphertext (str): The encrypted message to decrypt.
        key (str): The encryption key used for the Playfair cipher.

    Returns:
        str: The decrypted plaintext message.

    Notes:
        - The ciphertext and the key should only contain uppercase letters.
        - The plaintext message is returned as a string.
    """

    # Generate the Playfair matrix
    matrix = generate_matrix(key)

    # Generate pairs from the encrypted message
    pairs = generate_pairs(ciphertext)

    # Initialize variables
    plaintext = ""
    for pair in pairs:
        # Get the row and column indices for each letter in the pair
        row1, col1 = None, None
        row2, col2 = None, None
        for i in range(5):
            for j in range(5):
                if matrix[i][j] == pair[0]:
                    row1, col1 = i, j
                elif matrix[i][j] == pair[1]:
                    row2, col2 = i, j

        # Decrypt the pair based on the Playfair rules
        # Application of Rule 2 reversed
        if row1 == row2:  # Same row
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        # Application of Rule 3 reversed
        elif col1 == col2:  # Same column
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        # Application of Rule 4 reversed
        else:  # Forming a rectangle
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    # Remove any 'X' characters added for padding
    plaintext = plaintext.replace('X', '')

    # Remove any spaces in the plaintext
    plaintext = plaintext.replace(' ', '')

    # Remove any special characters and convert to uppercase just in case
    plaintext = re.sub(r'[^A-Za-z]', '', plaintext).upper()

    return plaintext

def main() -> None:
    print(decrypt_playfair(encrypted_message, key))

if __name__ == "__main__":
    main()