# Function to generate a Playfair key matrix
def generate_playfair_key(key):
    # Remove duplicates from the key and convert to uppercase
    key = "".join(dict.fromkeys(key.upper()))
    # Define the Playfair alphabet (excluding 'J')
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Initialize an empty list to store the key matrix
    key_matrix = []

    # Iterate through characters in the key
    for char in key:
        # Check if the character is not already in the key matrix and is in the Playfair alphabet
        if char not in key_matrix and char in alphabet:
            # Add the character to the key matrix
            key_matrix.append(char)

    # Iterate through characters in the Playfair alphabet
    for char in alphabet:
        # If the character is not in the key matrix, add it
        if char not in key_matrix:
            key_matrix.append(char)

    # Initialize an empty matrix to store the Playfair key
    matrix = []
    # Populate the matrix with rows of length 5
    for i in range(5):
        row = key_matrix[i*5:(i+1)*5]
        matrix.append(row)

    return matrix

# Function to find the position of a character in the Playfair key matrix
def find_position(matrix, char):
    # Iterate through rows and columns of the matrix
    for i in range(5):
        for j in range(5):
            # If the character is found, return its position
            if matrix[i][j] == char:
                return i, j
    # If the character is not found, return None
    return None, None

# Function to decrypt a pair of characters using the Playfair cipher rules
def decrypt_char_pair(matrix, char_pair):
    # Find the positions of the characters in the key matrix
    row1, col1 = find_position(matrix, char_pair[0])
    row2, col2 = find_position(matrix, char_pair[1])

    # Decrypt the characters based on their positions
    if row1 == row2:
        decrypted_char1 = matrix[row1][(col1 - 1) % 5]
        decrypted_char2 = matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        decrypted_char1 = matrix[(row1 - 1) % 5][col1]
        decrypted_char2 = matrix[(row2 - 1) % 5][col2]
    else:
        decrypted_char1 = matrix[row1][col2]
        decrypted_char2 = matrix[row2][col1]

    # Concatenate the decrypted characters
    return decrypted_char1 + decrypted_char2

# Function to decrypt a ciphertext using the Playfair cipher
def decrypt_playfair(ciphertext, key):
    # Convert the ciphertext to uppercase and remove spaces
    ciphertext = ciphertext.upper().replace(' ', '')
    # Generate the Playfair key matrix
    matrix = generate_playfair_key(key)
    # Initialize an empty string to store the decrypted plaintext
    plaintext = ""

    # Iterate through the ciphertext in pairs
    i = 0
    while i < len(ciphertext):
        char_pair = ciphertext[i:i+2]
        # If the pair is incomplete, add 'X' to complete it
        if len(char_pair) < 2:
            char_pair += 'X'
        # Decrypt the character pair and append to the plaintext
        decrypted_char_pair = decrypt_char_pair(matrix, char_pair)
        plaintext += decrypted_char_pair
        i += 2

    # Remove any 'X' characters that are not part of a digraph
    decrypted_message = []
    for idx in range(len(plaintext)):
        if plaintext[idx] == 'X' and (idx == 0 or idx == len(plaintext) - 1 or plaintext[idx-1] == plaintext[idx+1]):
            continue
        decrypted_message.append(plaintext[idx])
    
    # Concatenate the characters to form the decrypted message
    return "".join(decrypted_message)

# Main function to decrypt a specific ciphertext using a specific key
if __name__ == "__main__":
    # Define the key and ciphertext
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    # Decrypt the ciphertext using the key
    decrypted_message = decrypt_playfair(ciphertext, key)
    # Print the decrypted message, removing leading/trailing whitespaces
    print(decrypted_message.strip())
