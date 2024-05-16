'''
Name: Jason Lu (j388lu@uwaterloo.ca)
Shopify Engineering Internship Challenge
'''

def generate_cipher_table(key: str) -> dict:
    # Hashmap that maps letter to its row, column position in the cipher table
    table = {}
    used_letters = set()
    position_counter = 0

    # Adding the unique letters of the key to the table
    key = key.upper()
    for char in key:
        if char not in used_letters:
            # Convert position_counter to its row, column position in the table
            table[char] = (position_counter // 5, position_counter % 5)
            position_counter += 1
            used_letters.add(char)
    
    # Add the remaining letters of the alphabet to the table, excluding 'J'
    for ascii_codes in range(65, 91):  # ASCII values for A-Z
        char = chr(ascii_codes)
        if char == 'J':  # Skip J
            continue
        if char not in used_letters:
            table[char] = (position_counter // 5, position_counter % 5)
            position_counter += 1
            used_letters.add(char)

    return table

def decrypt_playfair(ciphertext: str, key: str) -> str:
    table = generate_cipher_table(key)
    # We reverse the table to allow for efficient decryption lookup, and we're allowed to do so because row, col positions are unique
    reverse_table = {v: k for k, v in table.items()}  
    decrypted_text = ""

    # We decrypt 2 letters at a time
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        row1, col1 = table[char1]
        row2, col2 = table[char2]
        # We mod 5 to account for overflow in the table, where we will need to wrap around
        # We apply the reverse of each encryption rule for decryption (ie. shift right -> shift left for equal row)
        if row1 == row2:  # Same row
            decrypted_text += reverse_table[(row1, (col1 - 1) % 5)]
            decrypted_text += reverse_table[(row2, (col2 - 1) % 5)]
        elif col1 == col2:  # Same column
            decrypted_text += reverse_table[((row1 - 1) % 5, col1)]
            decrypted_text += reverse_table[((row2 - 1) % 5, col2)]
        else:  # Rectangle rule
            decrypted_text += reverse_table[(row1, col2)]
            decrypted_text += reverse_table[(row2, col1)]

    decrypted_text = decrypted_text.replace('X', '')
    return decrypted_text

if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    decrypted_message = decrypt_playfair(ciphertext, key)
    print(decrypted_message)