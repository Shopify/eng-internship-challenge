def generate_playfair_key(key):
    # Create a list from the key, removing duplicates and ignoring 'J'
    filtered_key = []
    for char in key.upper():
        if char not in filtered_key and char != 'J':
            filtered_key.append(char)

    # Complete the set with the rest of the alphabet (excluding 'J')
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    full_key = filtered_key + [char for char in alphabet if char not in filtered_key]

    # Create a 5x5 matrix
    matrix = [full_key[i*5:(i+1)*5] for i in range(5)]
    return matrix

def decrypt_playfair(ciphertext, key):
    # Generate the Playfair cipher matrix
    matrix = generate_playfair_key(key)
    
    # Helper function to find the position of a letter in the matrix
    def find_position(letter):
        for row in range(5):
            for column in range(5):
                if matrix[row][column] == letter:
                    return row, column

    # Decrypt the ciphertext by pairs of letters
    plaintext = ''
    i = 0
    while i < len(ciphertext):
        row1, col1 = find_position(ciphertext[i])
        row2, col2 = find_position(ciphertext[i + 1])

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    # Remove 'X', spaces, and special characters, ensure all are uppercase
    final_output = ''.join([char for char in plaintext if char.isalpha() and char != 'X']).upper()
    return final_output

if __name__ == '__main__':
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_playfair(ciphertext, key)
    print(decrypted_message, end='')