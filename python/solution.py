def generate_playfair_square(passkey):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    passkey = "SUPERY" #Duplicate letters are removed from the passkey (i.e. S and P)

    square = []#creates the square for the playfair cipher
    for char in passkey: 
        if char not in square:
            square.append(char)
    
    for char in alphabet:
        if char not in square:
            square.append(char)
    
    return [square[i * 5:(i + 1) * 5] for i in range(5)]

def find_position(square, char):
    for i, row in enumerate(square):
        if char in row:
            return (i, row.index(char))
    return None

def decrypt_pair(square, a, b):
    row_a, col_a = find_position(square, a)
    row_b, col_b = find_position(square, b)
    
    if row_a == row_b:
        return square[row_a][(col_a - 1) % 5] + square[row_b][(col_b - 1) % 5]
    elif col_a == col_b:
        return square[(row_a - 1) % 5][col_a] + square[(row_b - 1) % 5][col_b]
    else:
        return square[row_a][col_b] + square[row_b][col_a]

def decrypt_playfair(ciphertext, passkey):
    ciphertext = ciphertext.replace("J", "I")
    square = generate_playfair_square(passkey)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i + 1]
        plaintext += decrypt_pair(square, a, b)
    
    return plaintext

# Provided encrypted message and passkey
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
passkey = "SUPERY"

# Decrypt the message
decrypted_message = decrypt_playfair(ciphertext, passkey)
print(decrypted_message)
