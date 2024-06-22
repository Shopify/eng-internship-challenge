'''
"Attention spy network! You've been assigned a task of the utmost importance! We've received an encrypted message from an agent in the field containing the password to a top secret club for super spies. The encrypted message reads as follows: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV". We've been told if we can crack this code and give the password to the door-person at the corner of 32nd Street, we will gain access to the illustrious spy club Spy City! We must get inside! However the password has been encrypted with an older system known as a Playfair Cipher. Our agent in the field says the key to the cipher is the string "SUPERSPY". However, for the life of us we cannot crack this code! Devise an application that can solve this encryption, get the password, and join us inside Spy City for what we are sure will be a night to remember!"
'''

def generate_key_matrix(key):
    # Replace 'J' with 'I' in the key to avoid having 'J' in the matrix, and convert key to uppercase
    key = key.replace("J", "I").upper()
    matrix = []  # Initialize an empty list to store the key matrix
    used_chars = set()  # A set to track characters already added to the matrix
    
    # Iterate over each character in the key
    for char in key:
        # Add the character to the matrix if it is alphabetic and not already used
        if char not in used_chars and char.isalpha():
            used_chars.add(char)  # Mark the character as used
            matrix.append(char)  # Add the character to the matrix
    
    # Define the alphabet without 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # Add the remaining characters of the alphabet to the matrix
    for char in alphabet:
        if char not in used_chars:
            used_chars.add(char)  # Mark the character as used
            matrix.append(char)  # Add the character to the matrix
    
    # Convert the flat list into a 5x5 matrix
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(matrix, char):
    # Iterate over each row and column in the matrix to find the position of the character
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)  # Return the row and column indices of the character
    return None  # Return None if the character is not found

def decrypt_playfair_cipher(ciphertext, key):
    matrix = generate_key_matrix(key)  # Generate the key matrix from the key
    ciphertext = ciphertext.upper().replace("J", "I")  # Replace 'J' with 'I' in ciphertext and convert to uppercase
    plaintext = []  # Initialize an empty list to store the decrypted text
    
    i = 0
    # Iterate over the ciphertext two characters at a time
    while i < len(ciphertext):
        a = ciphertext[i]  # First character of the pair
        b = ciphertext[i + 1]  # Second character of the pair
        
        # Find the positions of the characters in the matrix
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # If both characters are in the same row
        if row_a == row_b:
            # Move left in the same row (with wrap-around using modulo)
            decrypted_a = matrix[row_a][(col_a - 1) % 5]
            decrypted_b = matrix[row_b][(col_b - 1) % 5]
        # If both characters are in the same column
        elif col_a == col_b:
            # Move up in the same column (with wrap-around using modulo)
            decrypted_a = matrix[(row_a - 1) % 5][col_a]
            decrypted_b = matrix[(row_b - 1) % 5][col_b]
        # If the characters form a rectangle
        else:
            # Swap columns
            decrypted_a = matrix[row_a][col_b]
            decrypted_b = matrix[row_b][col_a]

        # Append the decrypted characters to the plaintext list
        plaintext.append(decrypted_a)
        plaintext.append(decrypted_b)
        
        i += 2  # Move to the next pair of characters
    
    # Join the plaintext list into a single string
    decrypted_text = "".join(plaintext)
    final_plaintext = []  # Initialize a list to store the final plaintext without 'X'
    
    # Iterate through the decrypted text
    for j in range(len(decrypted_text)):
        if decrypted_text[j] == 'X':
            # If 'X' is between duplicate letters, skip it
            if j > 0 and j < len(decrypted_text) - 1 and decrypted_text[j-1] == decrypted_text[j+1]:
                continue
        final_plaintext.append(decrypted_text[j])  # Add the character to the final plaintext
    
    return "".join(final_plaintext)  # Return the final plaintext as a string

# Example usage

key="SUPERSPY"
ciphertext="IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

plaintext = decrypt_playfair_cipher(ciphertext, key)
# replace X with empty string
plaintext = plaintext.replace("X", "")
print(plaintext)

