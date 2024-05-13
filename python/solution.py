import numpy as np

key_row = 5
key_col = 5

def generate_key_matrix(secret_key):
    key_matrix = np.zeros((key_row, key_col), dtype=str)
    m, n = 0, 0
    stored_characters = ""

    # Place unique characters from the secret key into the key matrix
    for character in secret_key:
        if character not in stored_characters:
            key_matrix[m][n] = character
            stored_characters += character
            n += 1
            if n == key_col:
                m += 1
                n = 0

    # Fill the remaining spaces in the key matrix with the alphabet (except 'J')
    for c in range(ord('A'), ord('Z')+1):
        if chr(c) not in stored_characters and chr(c) != 'J':
            key_matrix[m][n] = chr(c)
            n += 1
            if n == key_col:
                m += 1
                n = 0

    return key_matrix

def find_position(character, key_matrix):
    # Replace 'J' with 'I' for consistency
    if character == 'J':
        character = 'I'

    # Find the position of the character in the key matrix
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == character:
                return (i, j)

def decryption(cipher_text, key_matrix):
    decrypted_text = ""

    # Decrypt each pair of characters
    for i in range(0, len(cipher_text), 2):
        pair = cipher_text[i:i+2]
        position1 = find_position(pair[0], key_matrix)
        position2 = find_position(pair[1], key_matrix)

        if position1[0] == position2[0]:
            # If characters are in the same row, shift them left cyclically
            decrypted_text += key_matrix[position1[0]][(position1[1]-1) % 5]
            decrypted_text += key_matrix[position2[0]][(position2[1]-1) % 5]
        elif position1[1] == position2[1]:
            # If characters are in the same column, shift them up cyclically
            decrypted_text += key_matrix[(position1[0]-1) % 5][position1[1]]
            decrypted_text += key_matrix[(position2[0]-1) % 5][position2[1]]
        else:
            # If characters form a rectangle, swap their columns
            decrypted_text += key_matrix[position1[0]][position2[1]]
            decrypted_text += key_matrix[position2[0]][position1[1]]
    
    # Remove 'X', spaces, and convert to uppercase
    decrypted_text = ''.join(char.upper() for char in decrypted_text if char.isalpha() and char != 'X' and char != ' ')

    return decrypted_text

def main():
    secret_key = "SUPERSPY"
    cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    key_matrix = generate_key_matrix(secret_key)

    decrypted_text = decryption(cipher_text, key_matrix)
    print(decrypted_text)

if __name__ == "__main__":
    main()
