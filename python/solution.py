def create_playfair_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = []
    # Remove duplicates and prepare key
    seen = set()
    # Convert J to I in the key first, then remove duplicates
    key = key.replace('J', 'I')
    key = ''.join([c for c in key if not (c in seen or seen.add(c))])
    
    # Fill table
    for char in key:
        if char not in table:
            table.append(char)
    
    for char in alphabet:
        if char not in table:
            table.append(char)
    
    # Convert list to 5x5 matrix
    return [table[i*5:(i+1)*5] for i in range(5)]

def decrypt_playfair(ciphertext, key):
    table = create_playfair_table(key)
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        digraph = ciphertext[i:i+2]
        row1, col1, row2, col2 = [None]*4
        # Locate letters in the table
        for r in range(5):
            for c in range(5):
                if table[r][c] == digraph[0]:
                    row1, col1 = r, c
                elif table[r][c] == digraph[1]:
                    row2, col2 = r, c

        # Decrypt each pair
        if row1 == row2:
            decrypted_chars = table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_chars = table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else:
            decrypted_chars = table[row1][col2] + table[row2][col1]

        # remove the x from plaintext
        for char in decrypted_chars:
            if char != 'X':
                plaintext += char
            
    return plaintext

# Example usage
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
plaintext = decrypt_playfair(encrypted_message, key)
print(f'{plaintext}')



