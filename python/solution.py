key = "SUPERSPY"
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Construct the 5*5 matrix 
def generate_matrix(key):
    alphabet_sequence = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = [[0 for _ in range(5)] for _ in range(5)]
    # Remove Duplicate letters in the key
    key = ''.join(sorted(set(key.upper()), key=key.upper().index))
    index = 0

    # populate the matrix
    for i in range(5):
        for j in range(5):
            if index < len(key):
                matrix[i][j] = key[index]
                index += 1
            else:
                while True:
                    if len(alphabet_sequence) > 0:
                        c = alphabet_sequence[0]
                        alphabet_sequence = alphabet_sequence[1:]
                        if c not in key:
                            matrix[i][j] = c
                            break
                    else:
                        break
    return matrix

# Decipher the text using the 5*5 matrix
def decrypt(key, ciphertext):
    
    matrix = generate_matrix(key)
    plaintext = ""
    i = 0
    # pair two letters at a time and decipher each pair
    while i < len(ciphertext):
        c1 = ciphertext[i]
        if i + 1 < len(ciphertext):
            c2 = ciphertext[i + 1]
        else:
            c2 = 'X'

        c1row, c1col, c2row, c2col = 0, 0, 0, 0
        for row in range(5):
            if c1 in matrix[row]:
                c1row = row
                c1col = matrix[row].index(c1)
            if c2 in matrix[row]:
                c2row = row
                c2col = matrix[row].index(c2)

        # Same row substitution
        if c1row == c2row: 
            plaintext += matrix[c1row][(c1col - 1) % 5] + matrix[c2row][(c2col - 1) % 5]
        # Same column substitution
        elif c1col == c2col:  
            plaintext += matrix[(c1row - 1) % 5][c1col] + matrix[(c2row - 1) % 5][c2col]
        # Rectangle substitution
        else:  
            plaintext += matrix[c1row][c2col] + matrix[c2row][c1col]
        i += 2
    return ''.join(filter(lambda x: x.isalpha() and x != 'X', plaintext))

def main():
    # Decrypt the ciphertext
    plaintext = decrypt(key, ciphertext)
    # Print the decrypted plaintext
    print(plaintext.upper())

if __name__ == "__main__":
    main()