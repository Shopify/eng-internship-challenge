def generate_key_table(key):
    """
    Generates a key table and a dictionary of letter locations in the key table.

    Args:
        key (str): The key to generate the key table and letter locations from.

    Returns:
        tuple: A tuple containing the key table (a 2D list) and the letter locations (a dictionary).
    """
    key_table = [[0 for i in range(5)] for j in range(5)]

    #Encrypted Text uses I, assume I is used in place of J for this implementation
    alphabet = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")

    # Keeps track of the location each letter is placed within the table
    letter_locations = {}

    # Create a new key without duplicated letters
    new_key = ''
    for letter in key:
        if letter not in new_key:
            new_key += letter

    # Fill the key_table with the letters of the new_key
    count = 0
    for i in range(5):
        for j in range(5):
            if count == len(new_key):
                break
            key_table[i][j] = new_key[count]
            letter_locations[new_key[count]] = (i, j)
            alphabet.remove(new_key[count])
            count += 1

    # Fill remaining slots with the unused letters of the alphabet in order
    for i in range(5):
        for j in range(5):
            if key_table[i][j] == 0:
                key_table[i][j] = alphabet[0] # Always valid as the key table only holds 25 letters, loop only runs 25 times
                letter_locations[alphabet[0]] = (i, j)
                alphabet.pop(0)
    
    return key_table, letter_locations

def decrypt(encrypted_text, key):
    """
    Decrypts the given encrypted text using the Playfair cipher and the given key.

    Args:
        encrypted_text (str): The text to decrypt.
        key (str): The key to use for decryption.

    Returns:
        str: The decrypted text.
    """
    key_table, letter_locations = generate_key_table(key)

    letter_pairs = [encrypted_text[i:i+2] for i in range(0, len(encrypted_text), 2)]
    output = ""

    for pair in letter_pairs:
        first, second = letter_locations[pair[0]], letter_locations[pair[1]]
        
        # Letters in the same row are replaced by the letters immediately to the left each of them
        if first[0] == second[0]:
            if first[1] == 0:
                output += key_table[first[0]][4]
            else:
                output += key_table[first[0]][first[1] - 1]
            
            if second[1] == 0:
                output += key_table[second[0]][4]
            else:
                output += key_table[second[0]][second[1] - 1]
        # Letters in the same column are replaced by the letters immediately above each of them
        elif (first[1] == second[1]):
            if first[0] == 0:
                output += key_table[4][first[1]]
            else:
                output += key_table[first[0] - 1][first[1]]
        
            if second[0] == 0:
                output += key_table[4][second[1]]
            else:
                output += key_table[second[0] - 1][second[1]]
        # Letters that create a rectangle are replaced with the letter in the same row but in the opposite corner of the rectangle
        else:
            output += key_table[first[0]][second[1]] + key_table[second[0]][first[1]]

    # Ensure there are no "X" and no whitespace. Special Characters can not exist
    return output.replace("X", "").replace(" ", "")

if __name__ == '__main__':
    encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decrypt(encrypted_text, key))