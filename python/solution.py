import string


# Function to generate a Playfair matrix from a given key
def generate_playfair_matrix(key):
    # Replace 'J' with 'I' in the key
    key = key.replace("J", "I")

    # Remove duplicates from the key
    key = "".join(dict.fromkeys(key))

    # Generate the alphabet without 'J'
    alphabet = string.ascii_uppercase.replace('J', '')

    # Remove characters from alphabet that are already in the key
    remaining_alphabet = ''.join(char for char in alphabet if char not in key)

    # Fill the matrix with characters from the key and the remaining alphabet
    matrix_set = key + remaining_alphabet
    matrix = [[''] * 5 for _ in range(5)]
    mapping = {}

    for i in range(5):
        for j in range(5):
            letter = matrix_set[i * 5 + j]
            matrix[i][j] = letter
            mapping[letter] = (i, j)

    return matrix, mapping


# Function to decrypt the message
def decrypt_message(message):
    decrypted_message = ''
    for i in range(0, len(message), 2):
        # Separate the message into pairs of letters
        letter1 = message[i]
        letter2 = message[i + 1]

        # Get the row and column of each letter
        row1, col1 = letter_to_cell_mapping[letter1]
        row2, col2 = letter_to_cell_mapping[letter2]

        # Case 1: Same row
        if row1 == row2:
            decrypted_message += playfair_matrix[row1][(col1 - 1) % 5] + playfair_matrix[row2][(col2 - 1) % 5]
        # Case 2: Same column
        elif col1 == col2:
            decrypted_message += playfair_matrix[(row1 - 1) % 5][col1] + playfair_matrix[(row2 - 1) % 5][col2]
        # Case 3: Rectangle
        else:
            decrypted_message += playfair_matrix[row1][col2] + playfair_matrix[row2][col1]

    # Post-processing: Remove 'X' characters
    decrypted_message = decrypted_message.replace('X', '')

    return decrypted_message


# Function to validate the key
def validate_key(key):
    # Convert key to upper case
    key = key.upper()

    # Remove non-alphabetic characters
    key = ''.join(char for char in key if char.isalpha())

    return key


# Function to validate the ciphertext
def validate_ciphertext(ciphertext):
    # Check if ciphertext length is even
    if len(ciphertext) % 2 != 0:
        raise ValueError("Ciphertext length should be even.")

    # Check if ciphertext contains only upper-case alphabets excluding 'J'
    valid_chars = string.ascii_uppercase.replace('J', '')
    for index, char in enumerate(ciphertext):
        if char == 'J':
            raise ValueError("The algorithm only works with 'I' instead of 'J'.")
        if char not in valid_chars:
            raise ValueError(f"Invalid character '{char}' at index {index} in the ciphertext.")


# Run
playfair_key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# I am conducting some input validations based on my assumptions
# 1. The key cannot have any characters other than alphabets. Lower-case alphabets will be converted to upper-case
# 2. If they key has any characters other than alphabets, they will be removed and program will continue
# 3. The ciphertext can only have upper-case alphabets, excluding 'J'.
# 4. If the ciphertext has any characters other than upper-case alphabets, program shall exit with an error
# 5. The ciphertext length should be even
playfair_key = validate_key(playfair_key)

playfair_matrix, letter_to_cell_mapping = generate_playfair_matrix(playfair_key)
# print(playfair_matrix)
# print(letter_to_cell_mapping)

decrypted_message_result = decrypt_message(encrypted_message)
print(decrypted_message_result)
