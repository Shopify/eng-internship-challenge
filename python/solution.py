def generatePlayfairCipherTable(key):
    # Create a 5x5 grid
    key_table = [["" for _ in range(5)] for _ in range(5)]

    # Iterator for key
    key_index = 0

    # Set tracks characters already added to table
    used_characters = set()

    # Start at beginning of alphabet when all key elements are added to table
    fill_table = ord('A')

    # Stores [row,col] index pair for each character in the cipher table
    character_indicies = {}

    # Populate the cipher table
    for i in range(5):
        for j in range(5):
            # Skip repeat characters in the key
            while (key_index < len(key) and key[key_index].upper() in used_characters):
                key_index += 1

            new_character = ''
            if (key_index < len(key)):
                key_table[i][j] = key[key_index].upper()
                new_character = key[key_index].upper()
            else:
                # Skip characters that are already in the table
                while (chr(fill_table) in used_characters):
                    # Increment ASCII value by 1 to move to the next alphabetical character
                    fill_table += 1
                key_table[i][j] = chr(fill_table)
                new_character = chr(fill_table)

            # Insert the new character in the character set to avoid duplicates
            if new_character == 'I' or new_character == 'J':
                # I and J are treated as equals as per playfair rule
                used_characters.add('I')
                used_characters.add('J')
                character_indicies['I'] = (i,j)
                character_indicies['J'] = (i,j)
            else:
                character_indicies[new_character] = (i,j)
                used_characters.add(new_character)  
    return key_table, character_indicies
    
def decryptPlayfairCipher(key, encrypted_string):
    decrypted_characters = []
    # Split encrypted message into bigrams
    encrypted_pairs = [[encrypted_string[i], encrypted_string[i+1]] for i in range(0,len(encrypted_string)-1, 2)]
    key_table, character_indicies = generatePlayfairCipherTable(key)

    # Decrypt each pair
    for pair in encrypted_pairs:
        # Retrieve [row, col] indices of each character in bigram
        char1_index = character_indicies[pair[0]]
        char2_index = character_indicies[pair[1]]

        decrypted_char1_index = [-1, -1] 
        decrypted_char2_index = [-1, -1] 

        if char1_index[1] == char2_index[1]:
            # Check if bigram is in the same column and shift row position one to the left (with wrap around)
            decrypted_char1_index = [char1_index[0]-1, char1_index[1]] 
            decrypted_char2_index = [char2_index[0]-1, char2_index[1]]
        elif char1_index[0] == char2_index[0]:
            # Check if bigram is in the same row and shift column position up by one(with wrap around)
            decrypted_char1_index = [char1_index[0], char1_index[1]-1]
            decrypted_char2_index = [char2_index[0], char2_index[1]-1]
        else:
            # The bigram forms a rectangle so select the table element that is in the opposite corner of the rectangle in the same row
            decrypted_char1_index = [char1_index[0], char2_index[1]] 
            decrypted_char2_index = [char2_index[0], char1_index[1]]
        
        # Append the decrypted pair to the result 
        decrypted_characters.append(key_table[decrypted_char1_index[0]][decrypted_char1_index[1]]) 
        decrypted_characters.append(key_table[decrypted_char2_index[0]][decrypted_char2_index[1]])
    # Remove all occurrences of 'X' and return the result as a string
    return "".join([c for c in decrypted_characters if c != 'X'])

if __name__ == "__main__":
    # Solving the given cipher: 
    key = "SUPERSPY"
    encrypted_string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_string = decryptPlayfairCipher(key, encrypted_string)
    print(decrypted_string) # Solution is: HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA
