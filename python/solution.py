import string

# Define the key and the encrypted message
key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

def create_matrix(key):
    # J ommitted because there can only be 25 letters in the matrix
    used_letters = set("J")
    cipher_letters = [letter for letter in key + string.ascii_uppercase if letter not in used_letters and not used_letters.add(letter)]
    return [cipher_letters[i:i+5] for i in range(0, 25, 5)]

def decrypt_message(digraphs, matrix):
    location_index = {matrix[row][col]: (row, col) for row in range(5) for col in range(5)}

    def decrypt_pair(pair):
        row1, col1 = location_index[pair[0]]
        row2, col2 = location_index[pair[1]]

        if row1 == row2:
            return matrix[row1][(col1-1) % 5] + matrix[row2][(col2-1) % 5]
        elif col1 == col2:
            return matrix[(row1-1) % 5][col1] + matrix[(row2-1) % 5][col2]
        else:
            return matrix[row1][col2] + matrix[row2][col1]
    
    return ''.join(decrypt_pair(pair) for pair in digraphs)

def get_digraphs(message):
    return [message[i:i+2] for i in range(0, len(message), 2)]

matrix = create_matrix(key)
digraphs = get_digraphs(encrypted_message)
decrypted_message = decrypt_message(digraphs, matrix).replace('X', '')

print(decrypted_message)
