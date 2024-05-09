def get_cypher(key):
    # Initialize a dictionary to track which letters have been used
    used_letters = {}
    # Initialize an empty string for the new key without duplicates
    new_key = ''
    # Replace 'J' with 'I' to handle the Playfair cipher rule that merges I and J
    key = key.replace('J', 'I')
    # Iterate through the key, adding unique letters to the new_key
    for i in range(0, len(key)):
        if key[i] not in used_letters and ord(key[i])>=65 and ord(key[i])<=90:
            new_key += key[i]
            used_letters[key[i]] = 1
    # Complete the key by adding unused letters of the alphabet, excluding 'J'
    complete_key = new_key + ''.join(chr(i) for i in range(65, 91) if chr(i) not in used_letters and i != 74)
    # Create a 5x5 matrix to represent the cipher key
    key_matrix = [[] for _ in range(0, 5)]
    for i in range(0, 25):
        key_matrix[i // 5].append(complete_key[i])
    # Map each character to its position in the matrix for quick access
    key_map = {}
    for row in range(0, 5):
        for col in range(0, 5):
            key_map[key_matrix[row][col]] = (row, col)
    return key_map, key_matrix

def decrypt_two_characters(two_characters, key_map, key_matrix):
    # Fetch positions of the two characters from the key map
    first_character = key_map[two_characters[0]]
    second_character = key_map[two_characters[1]]
    # Decrypt based on their positions in the matrix
    if first_character[0] == second_character[0]:
        # Same row: Shift both characters one position to the left (wrap around if necessary)
        return key_matrix[first_character[0]][first_character[1]-1 if first_character[1]!=0 else 4] + \
               key_matrix[second_character[0]][second_character[1]-1 if second_character[1]!=0 else 4]
    elif first_character[1] == second_character[1]:
        # Same column: Shift both characters one position up (wrap around if necessary)
        return key_matrix[first_character[0]-1 if first_character[0]!=0 else 4][first_character[1]] + \
               key_matrix[second_character[0]-1 if second_character[0]!=0 else 4][second_character[1]]
    else:
        # Rectangle rule: Swap the characters' columns
        return key_matrix[first_character[0]][second_character[1]] + \
               key_matrix[second_character[0]][first_character[1]]

def decrypt_message(encrypted_message, key):
    # Generate the cipher key matrix and map
    key_map, key_matrix = get_cypher(key)
    # Handle odd-length encrypted messages by appending 'X' if necessary
    if len(encrypted_message) % 2 != 0:
        encrypted_message += 'X'
    # Initialize the decrypted message
    decrypted_message = ''
    # Decrypt two characters at a time
    for i in range(0, len(encrypted_message), 2):
        decrypted_message += decrypt_two_characters(encrypted_message[i:i + 2], key_map, key_matrix)
    # Remove any 'X' used for padding during decryption
    return decrypted_message.replace('X', '')

# Example usage
key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted_message = decrypt_message(encrypted_message, key)
print(decrypted_message)