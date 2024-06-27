def construct_table(keyword):
    """
    This function generates the associated Playfair
    table (2D array) with the given keyword.
    """
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Omitting J
    playfair_set = set()
    playfair_list = []

    # Summing letters, starting w/ keyword and then alphabet
    generation_string = keyword + alphabet
    
    # If letter has appeared already (in set), it's in the table already.
    for letter in generation_string:
        if letter not in playfair_set:
            playfair_set.add(letter)
            playfair_list.append(letter)

    # Transforming playfair_list to 2D list (i.e. a matrix/table)
    playfair_table = []

    for i in range(0, 25, 5):
        row = playfair_list[i:i+5] # Grabbing elements, 5 at a time
        playfair_table.append(row)

    return playfair_table


def create_letter_locations(table):
    """
    This function maps letters to their indices
    and returns it as a dictionary.
    """
    letter_locations = {}

    for i in range(5):
        for j in range(5):
            letter_locations[table[i][j]] = (i,j)

    return letter_locations

def decrypt_playfair(message, table):
    """
    This function decrypts and returns 
    the message, given a Playfair table.
    """

    i = 0
    j = 1
    decrypted_message = ""
    letter_locations = create_letter_locations(table)

    # Stop once we've reached the end of the message
    while i < len(message) and j < len(message):
        letter1 = message[i]
        letter2 = message[j]

        location1 = letter_locations[letter1] # Indices of letter 1
        location2 = letter_locations[letter2] # Indices of letter 2

        # Row and column indices of letter 1 and 2
        l1_row = location1[0]
        l2_row = location2[0]
        l1_col = location1[1]
        l2_col = location2[1]

        # If letters are in the same row
        if l1_row == l2_row:
            """
            Shift 1 letter to the left if there exists one.
            Otherwise, take the rightmost character.
            """ 

            decrypted_message += table[l1_row][l1_col-1] if l1_col-1 >= 0 else table[l1_row][4]
            decrypted_message += table[l2_row][l2_col-1] if l2_col-1 >= 0 else table[l2_row][4]
            i += 2
            j += 2


        # If letters are in the same col
        elif l1_col == l2_col:
            """
            Shift 1 letter upwards if there exists one.
            Otherwise, take the bottommost character.
            """
            decrypted_message += table[l1_row-1][l1_col] if l1_row-1 >= 0 else table[4][l1_col]
            decrypted_message += table[l2_row-1][l2_col] if l2_row-1 >= 0 else table[4][l1_col]
            i += 2
            j += 2


        # Neither (letters form diagonal corners of a rectangle)
        else:
            """
            Letter 1: Take the letter in L1's row but in L2's column
            Letter 2: Take the letter in L2's row but in L1's column
            """

            decrypted_message += table[l1_row][l2_col]
            decrypted_message += table[l2_row][l1_col]
            i += 2
            j += 2
        
    return decrypted_message

if __name__ == '__main__':
    key = "SUPERSPY"
    table = construct_table(key)
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt_playfair(message, table).replace("X", "").replace(" ", ""))