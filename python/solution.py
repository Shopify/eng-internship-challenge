def generate_matrix(key):
    """
    The function `generate_matrix` creates a 5x5 matrix for a Playfair cipher key by normalizing the key
    and populating the matrix with unique characters from the key and the alphabet.
    
    param key: The `generate_matrix` function takes a key as input and generates a 5x5 matrix (key
    matrix) for the Playfair cipher algorithm. The key is normalized by converting it to uppercase,
    removing duplicates, and replacing 'J' with 'I'. The remaining characters are filled with the
    alphabet

    return: The function `generate_matrix(key)` returns a 5x5 matrix (list of lists) representing the
    key matrix used in the Playfair cipher encryption algorithm.
    """

    # Normalize the key by converting to uppercase and removing duplicates
    normalized_key = ''
    seen_chars = set()
    for char in key.upper():
        if char.isalpha() and char not in seen_chars:
            # Replace 'J' with 'I' as per Playfair cipher convention
            if char == 'J':
                char = 'I'
            seen_chars.add(char)
            normalized_key += char

    # Populate the rest of the key matrix with non-duplicate characters from the alphabet
    remaining_alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # excluding 'J'
    full_key = normalized_key + ''.join([ch for ch in remaining_alphabet if ch not in seen_chars])

    # Create a 5x5 matrix for the key
    key_matrix = []
    for i in range(0, 25, 5):
        row = full_key[i:i + 5]
        key_matrix.append(row)
        
    return key_matrix


def decrypt_playfair(text, key):
    """
    The function `decrypt_playfair` decrypts a Playfair cipher text using a given key matrix.
    
    param text: Please provide the text that you want to decrypt using the Playfair cipher:

    param key: The `key` parameter in the Playfair cipher is a keyword used to create the key matrix
    for encryption and decryption. It is typically a word or phrase without repeating letters that
    determines the arrangement of letters in the key matrix. The key matrix is a 5x5 grid of unique
    letters (excluding 'J') that is used to encrypt and decrypt the text.

    return: The function `decrypt_playfair(text, key)` returns the decrypted text after applying the
    Playfair cipher decryption algorithm. The decrypted text is filtered to remove 'X' characters and
    non-alphabetic characters before being returned as a string in uppercase.
    """
    # Generate the key matrix
    key_matrix = generate_matrix(key)
    
    # Create a dictionary to map characters to their positions in the key matrix
    letter_pos = {}
    for i, row in enumerate(key_matrix):
        for j, ch in enumerate(row):
            letter_pos[ch] = (i, j)

    # Split the text into digrams
    digrams = []
    for i in range(0, len(text), 2):
        digram = text[i:i + 2]
        digrams.append(digram)

    decrypted_text = []

    # Decrypt each digram
    for a, b in digrams:
        # Get the positions of characters a and b in the key matrix
        row_a, col_a = letter_pos[a]
        row_b, col_b = letter_pos[b]

        # Decrypt based on the positions of the characters in the key matrix
        if row_a == row_b:  # Same row
            col_a = (col_a - 1) % 5
            col_b = (col_b - 1) % 5
            new_a = key_matrix[row_a][col_a]
            new_b = key_matrix[row_b][col_b]
            
        elif col_a == col_b:  # Same column
            row_a = (row_a - 1) % 5
            row_b = (row_b - 1) % 5
            new_a = key_matrix[row_a][col_a]
            new_b = key_matrix[row_b][col_b]

        else:  # Rectangle
            new_a = key_matrix[row_a][col_b]
            new_b = key_matrix[row_b][col_a]

        # Append the decrypted characters to the result
        decrypted_text.extend([new_a, new_b])

    # Filter out 'X' and non-alphabetic characters and return the decrypted text
    filtered_chars = []
    for char in decrypted_text:
        if char != "X" and char.isalpha():
            filtered_chars.append(char.upper())
    return ''.join(filtered_chars)

def main():
    key = "SUPERSPY"
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt_playfair(encrypted, key))

if __name__ == '__main__':
    main()