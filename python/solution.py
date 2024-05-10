"""
Defining the global variables to easily access them

They do not change within the program, so I declare them as constant variables
"""
ENCRYPTED = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
KEY = "SUPERSPY"

# Not including 'J' since 'I' and 'J' can be interchanged
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def create_table():
    """
    This function creates a 5x5 table using the key.

    Paramaters: None - Uses global constant values
    - It takes in the key and alphabet used and returns a 2D array

    Returns:
    table - Playfair cipher table made with key
    char_indices - indices of each character
    """

    # Creating a 5x5 table
    table = [["" for i in range(5)] for j in range(5)]
    
    # Combining the key and alphabet to be used for the table
    all_letters = KEY + ALPHABET

    # A set to keep track of the used letters thus far
    used_letters = set()

    # Dictionary to keep track of character locations
    # Faster than looking up the locations later
    char_indices = {}

    # Integer value used to index the location in the table to place a character
    # For loop goes through all characters until table is filled
    char_loc = 0
    for char in all_letters:

        # Break when table filled
        if char_loc >= 25:
            break

        # Add character to table if letter not already used
        # Also add the character's location to the dictionary
        if char not in used_letters:
            used_letters.add(char)
            
            char_row = char_loc // 5
            char_col = char_loc % 5

            table[char_row][char_col] = char

            char_indices[char] = (char_row, char_col)

            char_loc += 1

    return table, char_indices

    
def decrypt_string(table, char_indices):
    """
    Function that decrypts the encrypted string using the Playfair cipher and table

    Parameters:
    table - the table created using the key and remaining alphabet letters
    char_indices - the indices of each character in the table

    Returns:
    original_string - the decrypted string
    """

    # Declaring a string to return the deciphered result
    original_string = ""

    # Looping through every two characters
    for i in range(0, len(ENCRYPTED), 2):

        # Getting each two characters
        char1 = ENCRYPTED[i]
        char2 = ENCRYPTED[i+1]

        # Also getting character rows and columns
        r1, c1 = char_indices[char1]
        r2, c2 = char_indices[char2]

        # If the rows match, get the element to the left with wraparound
        if r1 == r2:
            c1 = (c1 - 1) % 5
            c2 = (c2 - 1) % 5
            
            original_string += table[r1][c1]
            original_string += table[r2][c2]

        # If the columns match, get the element above with wraparound
        elif c1 == c2:
            r1 = (r1 - 1) % 5
            r2 = (r2 - 1) % 5
            
            original_string += table[r1][c1]
            original_string += table[r2][c2]

        # Otherwise (a square is made) swap the columns but keep the rows when adding to the string
        else:
            original_string += table[r1][c2]
            original_string += table[r2][c1]

    # Remove any 'X's or spaces from the result
    original_string = original_string.replace("X", "").replace(" ", "")

    return original_string


if __name__ == '__main__':
    table, char_indices = create_table()
    print(decrypt_string(table, char_indices))