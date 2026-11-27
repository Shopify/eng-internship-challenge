import re

def createTable(key):
    # Removed J from alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Create a string with all letters available
    letters = key + alphabet

    # Create array to hold 5 x 5 table
    table = []

    # Create array of letters that will be selected
    valid_letters = []

    # Add 25 letters that are not duplicates to valid_letters
    for i in letters:
        if i not in valid_letters and len(valid_letters) != 25:
            valid_letters.append(i)
    
    # Create a 5 x 5 table containing the valid letters
    for i in range(5):
        table.append(valid_letters[:5])
        valid_letters = valid_letters[5:]
    
    return table

# Iterate through each element in table and check if element is found
def findPos(table, char):
    for i, row in enumerate(table):
        for j, cell in enumerate(row):
            if cell == char:
                return i, j
    return None

def decode(encrypted, key):
    # Create table used for playfair decoding
    table = createTable(key)

    # Remove all not alphabetical character from encrypted text and replaced all instance of J with I in string
    encrypted = re.sub(r'[^A-Z]', '', encrypted.upper().replace('J', 'I'))
    plaintext = []

    # Iterate through each pair of letters in encrypted text
    for i in range(0, len(encrypted), 2):
        # Check to ensure iterator doesn't go out of bounds
        if i + 1 < len(encrypted):
            # Grab two letters
            a = encrypted[i] 
            b = encrypted[i + 1]

            # Find their respective column and row
            row_a, col_a = findPos(table, a)
            row_b, col_b = findPos(table, b)
            
            # Same row: add the letters to their direct left
            if row_a == row_b:
                plaintext.append(table[row_a][(col_a - 1) % 5])
                plaintext.append(table[row_b][(col_b - 1) % 5])

             # Same column: add the letters directly above them
            elif col_a == col_b:
                plaintext.append(table[(row_a - 1) % 5][col_a])
                plaintext.append(table[(row_b - 1) % 5][col_b])

            # Unique rows and columns: add the letters that are in A's/B's row and B's/A's column respectively
            else:
                plaintext.append(table[row_a][col_b])
                plaintext.append(table[row_b][col_a])
    
    # Make string out of array
    text = ''.join(plaintext)

    # Remove X as per output specification
    return text.replace('X', '')



if __name__ == "__main__":
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decode(encrypted, key))
        


