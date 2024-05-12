import string

# Define the key and the encrypted message
key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

def create_playfair_matrix(key):
    """
    Creates a 5x5 Playfair cipher matrix from a given key.
    'J' is excluded from the matrix, and the matrix is filled with non-duplicate letters.
    """
    # Initialize a string for the cipher letters and a set for tracking used letters
    cipher_letters = ""
    used_letters = set("J")  # 'J' is typically merged with 'I' in Playfair cipher

    # Append the uppercase alphabet to the key for matrix creation
    key_extended = key + string.ascii_uppercase

    # Fill cipher_letters with unique letters from the extended key
    for letter in key_extended:
        if letter not in used_letters:
            cipher_letters += letter
            used_letters.add(letter)

    # Create the cipher matrix as a list of 5-character chunks
    cipher_matrix = [list(cipher_letters[i:i+5]) for i in range(0, len(cipher_letters), 5)]

    return cipher_matrix

def decrypt_playfair(digraphs, matrix):
    """
    Decrypts a list of digraphs using a given Playfair cipher matrix.
    """
    # Map each letter in the matrix to its row and column coordinates
    location_index = {matrix[row][col]: (row, col) for row in range(5) for col in range(5)}
    
    def decrypt_pair(pair):
        """
        Decrypts a pair of letters according to Playfair cipher rules.
        """
        row1, col1 = location_index[pair[0]]
        row2, col2 = location_index[pair[1]]

        # Same row: shift letters to the left
        if row1 == row2:
            return matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        # Same column: shift letters up
        elif col1 == col2:
            return matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        # Rectangle: swap columns
        else:
            return matrix[row1][col2] + matrix[row2][col1]
    
    # Join decrypted pairs into the decrypted message
    return ''.join(decrypt_pair(pair) for pair in digraphs)

def split_into_digraphs(message):
    """
    Splits the encrypted message into digraphs (pairs of two letters).
    """
    return [message[i:i+2] for i in range(0, len(message), 2)]

# Generate the cipher matrix and digraphs
playfair_matrix = create_playfair_matrix(key)
message_digraphs = split_into_digraphs(encrypted_message)

# Decrypt the message using Playfair cipher
decrypted_message = decrypt_playfair(message_digraphs, playfair_matrix)

# Remove any 'X' used as padding in the decryption process
decrypted_message = decrypted_message.replace('X', '')

# Output the decrypted message
print(decrypted_message)
