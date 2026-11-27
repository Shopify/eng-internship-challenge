# Name: Fayaz Rafin

def create_key_grid(key):
    # Removing duplicate letters from key string and create a 5x5 matrix to decipher the encrypted text.
    key = key.upper().replace('J', 'I') # J is ignored so we exclude J and replace it with I.
    char_set = set()
    key_matrix = []
    combined_chars = key + 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in combined_chars:
        if char not in char_set and char != 'J': 
            char_set.add(char)
            key_matrix.append(char)
    # A 5x5 matrix is created from the key string and the remaining alphabets. 
    key_grid = []
    for i in range(0, 25, 5):
        key_grid.append(key_matrix[i:i + 5])

    return key_grid
    
def decrypt_message(cipher_text, key_matrix):
    def find_position(letter):
        for row_index, row in enumerate(key_matrix):
            if letter in row:
                return (row_index, row.index(letter))
        return None

    # Decrypt the encrypted message by splitting the letters into pairs
    def decrypt_pair(char1, char2):
        row1, col1 = find_position(char1)
        row2, col2 = find_position(char2)

        if row1 == row2:
            # If the characters are in the same row, we shift each letter to the left by one
            return key_matrix[row1][(col1 - 1) % 5], key_matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            # If the characters are in the same column, we shift each letter up by one
            return key_matrix[(row1 - 1) % 5][col1], key_matrix[(row2 - 1) % 5][col2]
        else:
            # If the characters are in different rows and columns, we swap columns
            return key_matrix[row1][col2], key_matrix[row2][col1]

    # Replaced 'J' with 'I' as we excluded the letter J in our key grid
    formatted_text = cipher_text.replace('J', 'I')
    decrypted_text = []

    i = 0
    while i < len(formatted_text):
        pair = decrypt_pair(formatted_text[i], formatted_text[i + 1])
        decrypted_text.extend(pair)
        i += 2

    return ''.join(decrypted_text).replace('X', '')


if __name__ == "__main__":
    key = "SUPERSPY"
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key_matrix = create_key_grid(key)
    decrypted_message = decrypt_message(message, key_matrix)
    print(decrypted_message)

