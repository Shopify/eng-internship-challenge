# Helper function
def find_char_index(char, array):
    for r, row in enumerate(array):
        for c, item in enumerate(row):
            if item==char:
                return r, c
    
    print("Error: character not found")
    quit()

def generate_table(keyword):

    # Initializing 5x5 empty array (Playfair table)
    playfair_table = [[None]*5 for i in range(5)]
    
    # Cleaning up the keyword: no duplicate letters, and J will be ommitted
    newStr = ""
    for char in keyword:
        if char not in newStr and char.lower() != 'j':
            newStr += char.upper()
    keyword = newStr

    # Checks if keyword is bigger than the table. In that case, in order to prevent IndexError, it slices the string
    if len(keyword) > 25:
        keyword = keyword[:25]

    # Populates empty table with the letters from the keyword
    for i in range(len(keyword)):
        playfair_table[i//5][i%5] = keyword[i]

    # Continues to populate the table with letters from the alphabet, starting after the keyword
    # Makes sure to skip letters from the alphabet that were already included in the keyword, and 'j'
    j=0
    for i in range(25):
        if playfair_table[i//5][i%5] != None:
            continue
        while chr(ord('A')+j) in keyword or chr(ord('A')+j) == 'J':
            j+=1
        playfair_table[i//5][i%5] = chr(ord('A')+j)
        j+=1
    
    return playfair_table


def decrypt_message(encrypted_message, table):

    encrypted_message = encrypted_message.upper()
    decrypted_message = ""

    for i in range(0, len(encrypted_message), 2):
        
        # Uses helper function to get the position of character in the table
        r1, c1 = find_char_index(encrypted_message[i], table)
        r2, c2 = find_char_index(encrypted_message[i+1], table)

        # In the statements below, there is no risk of overlow. Since the expected behavior for the
        # decryption algorithm is to "wrap around" after going further than the beginning of the array,
        # which would happen at index 0, Python automatically handles it (index -1 represents last index)

        # If they are in the same row, shift one element over to the left
        if r1==r2:
            decrypted_message += table[r1][(c1-1)]
            decrypted_message += table[r1][(c2-1)]

        # If they are in the same column, shift one element over up
        elif c1 == c2:
            decrypted_message += table[r1-1][c1]
            decrypted_message += table[r1-1][c2]
        
        # If they aren't, swap the elements in the rectangle shape
        else:
            decrypted_message += table[r1][c2]
            decrypted_message += table[r2][c1]

    # Cleaning up decrypted message (getting rid of spaces | 'X' | special characters)
    newStr = ""

    for char in decrypted_message:
        if not char.isalpha() or char=="X":
            continue
        newStr += char
    
    decrypted_message = newStr

    return decrypted_message
    

keyword = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

print(decrypt_message(encrypted_message, generate_table(keyword)))