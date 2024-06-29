import string

def prepare_key(key):
    key = key.upper().replace('J', 'I')
    return ''.join(dict.fromkeys(key + string.ascii_uppercase.replace('J', '')))

def create_matrix(key):
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    for i, row in enumerate(matrix):
        if letter in row:
            return i, row.index(letter)
    return None

def decrypt_playfair(ciphertext, key):
    prepared_key = prepare_key(key)
    matrix = create_matrix(prepared_key)
    ciphertext = ciphertext.upper().replace('J', 'I')
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
        elif col1 == col2:
            plaintext += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]

    return plaintext.replace('X','')

def process_cipher(key, ciphertext):
    decrypted_text = decrypt_playfair(ciphertext, key)
    return decrypted_text

if __name__ == "__main__":
    secret_key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    
    result = process_cipher(secret_key, encrypted_message)
    print(result, end='')
