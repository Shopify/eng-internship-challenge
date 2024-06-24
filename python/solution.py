def generate_key_table(keyword):
    # Create a 5x5 key table
    key_table = []
    seen = set()
    
    # Add keyword letters to the key table
    for char in keyword:
        if char not in seen:
            seen.add(char)
            key_table.append(char)
    
    # Add remaining letters of the alphabet to the key table
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':  # I/J are treated as the same letter
        if char not in seen:
            seen.add(char)
            key_table.append(char)
    
    # Convert the key table list into a 5x5 matrix
    return [key_table[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, key_table):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == char:
                return row, col
    return None

def decrypt_pair(pair, key_table):
    r1, c1 = find_position(pair[0], key_table)
    r2, c2 = find_position(pair[1], key_table)
    
    if r1 == r2:
        return key_table[r1][(c1 - 1) % 5] + key_table[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return key_table[(r1 - 1) % 5][c1] + key_table[(r2 - 1) % 5][c2]
    else:
        return key_table[r1][c2] + key_table[r2][c1]

def preprocess_message(message):
    # Prepare message for decryption by splitting into pairs and handling 'X'
    message = message.replace(" ", "").upper()
    pairs = []
    i = 0
    while i < len(message):
        a = message[i]
        b = message[i + 1] if i + 1 < len(message) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def decrypt_message(message, keyword):
    key_table = generate_key_table(keyword)
    pairs = preprocess_message(message)
    decrypted_text = ''.join(decrypt_pair(pair, key_table) for pair in pairs)
    # Remove any 'X's in the string
    decrypted_text = decrypted_text.replace('X', '')
    # Ensure the result is entirely uppercase and doesn't include spaces or special characters
    decrypted_text = ''.join(filter(str.isalpha, decrypted_text))
    return decrypted_text

if __name__ == "__main__":
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    keyword = "SUPERSPY"
    decrypted_message = decrypt_message(encrypted_message, keyword)
    print(decrypted_message)
