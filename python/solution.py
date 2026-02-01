import string


# Function to generate matrix from a given key
def generate_matrix(key):

    #Check validity of key
    key = ''.join(char for char in key.upper() if char.isalpha())

    if not key:
        raise ValueError("Invalid key")

    # Process the key: convert to uppercase and remove 'J'
    key = key.upper().replace('J', '')

    # Remove duplicate letters from the key while maintaining order
    processed_key = ""
    for char in key:
        if char not in processed_key and char in string.ascii_uppercase:
            processed_key += char

    # Generate the remaining alphabet without 'J'
    alphabet = ''.join([char for char in string.ascii_uppercase if char != 'J' and char not in processed_key])

    # Combine the processed key and the remaining alphabet
    full_key = processed_key + alphabet

    # Create a 5x5 matrix
    matrix = []
    for i in range(0, 25, 5):
        matrix.append(list(full_key[i:i+5]))

    # Create a mapping dictionary for quick lookup of character positions
    mapping = {char: (i, j) for i, row in enumerate(matrix) for j, char in enumerate(row)}

    return matrix, mapping


# Function to decrypt the message
def decrypt(message):

    # Validate the ciphertext before proceeding
    if len(message) % 2 != 0:
        raise ValueError("Length of ciphertext should be even.")

    valid_chars = string.ascii_uppercase.replace('J', '')
    for index, char in enumerate(message):
        if char == 'J':
            raise ValueError("The algorithm soes not work with 'J'.")
        if char not in valid_chars:
            raise ValueError(f"Invalid character '{char}' at index {index}.")
    
    # Function to decrypt a pair of letters
    def decrypt_pair(letter1, letter2):
        row1, col1 = letter_to_cell_mapping[letter1]
        row2, col2 = letter_to_cell_mapping[letter2]

        if row1 == row2:
            return playfair_matrix[row1][(col1 - 1) % 5] + playfair_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            return playfair_matrix[(row1 - 1) % 5][col1] + playfair_matrix[(row2 - 1) % 5][col2]
        else:
            return playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

    # Process message in pairs and decrypt
    pairs = [message[i:i+2] for i in range(0, len(message), 2)]
    decrypted_pairs = [decrypt_pair(pair[0], pair[1]) for pair in pairs]
    decrypted_message = ''.join(decrypted_pairs)

    # Post-processing: Remove 'X' characters
    decrypted_message = decrypted_message.replace('X', '')

    return decrypted_message



# Run
playfair_key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Generate the Playfair matrix and mapping
playfair_matrix, letter_to_cell_mapping = generate_matrix(playfair_key)

# Decrypt the message
decrypted_message = decrypt(encrypted_message)
print(decrypted_message)
