# Written By Kevin Lin on May 11th, 2024 for shopify OA

def generate_cipher_key(key):
    # Define the alphabet, excluding 'J' and keeping 'X' for padding and separation
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = ''.join(sorted(set(key), key=key.index))
    key_matrix = [c for c in key.upper() if c in alphabet] + [c for c in alphabet if c not in key]
    return [key_matrix[i:i+5] for i in range(0, 25, 5)]

def playfair_decrypt(key, text):
    key_matrix = generate_cipher_key(key)
    location = {char: (row, col) for row, line in enumerate(key_matrix) for col, char in enumerate(line)}
    decrypted = []
    
    i = 0
    while i < len(text) - 1:
        a, b = text[i], text[i+1]
        row1, col1 = location[a]
        row2, col2 = location[b]

        if row1 == row2:
            decrypted.append(key_matrix[row1][(col1 - 1) % 5])
            decrypted.append(key_matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted.append(key_matrix[(row1 - 1) % 5][col1])
            decrypted.append(key_matrix[(row2 - 1) % 5][col2])
        else:
            decrypted.append(key_matrix[row1][col2])
            decrypted.append(key_matrix[row2][col1])

        i += 2

    # Convert decrypted list to string
    final_message = ''.join(decrypted)

    # Remove 'X' between identical letters
    clean_message = []
    i = 0
    while i < len(final_message):
        if i < len(final_message) - 2 and final_message[i] == final_message[i+2]:
            # If the current character and next are the same, skip the next if it's 'X'
            clean_message.append(final_message[i])
            if final_message[i+1] == 'X':
                i += 2  # Skip the 'X'
            else:
                i += 1
        else:
            clean_message.append(final_message[i])
            i += 1

    # Remove any trailing 'X' as it is likely padding
    if clean_message[-1] == 'X':
        clean_message.pop()

    return ''.join(clean_message)

if __name__ == "__main__":
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY" #make this modular for other potentially used keys
    decrypted_message = playfair_decrypt(key, encrypted_message)
    print(decrypted_message)
