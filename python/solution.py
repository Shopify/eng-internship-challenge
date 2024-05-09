# --- Defining the key, encrypted string and alphabet being used to decrypt ---
ENCRYPTED = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
KEY = "SUPERSPY"

# Not including 'J' since 'I' and 'J' can be interchanged
ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def create_table():
    """
    This function creates a 5x5 table using the key.

    Paramaters: None - Uses global values
    - It takes in the key and alphabet used and returns a 2D array
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

    
def decrypt_string(table):
    pass


if __name__ == '__main__':
    table, char_indices = create_table()
    decrypt_string(table)