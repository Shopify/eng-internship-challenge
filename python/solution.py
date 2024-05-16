"""
**********************************************
Jian Li (j438li@uwaterloo.ca)
Technical Challenges
Python
Decrypts messages encrypted using a Playfair cipher
in order to access SpyCity.
**********************************************
"""



def create_playfair_key_square(key):
    """
    create_playfair_key_square creates a 5x5 Playfair cipher key square based on the key.
    Requires: key (str): Must be a sequence of alphabet characters.
    
    Returns:
    list: A list of lists representing the 5x5 2D matrix.
 
    Example:
    >>> create_playfair_key_square("KEYWORD")
    [['K', 'E', 'Y', 'W', 'O'], ['R', 'D', 'A', 'B', 'C'], ...]
    """
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

   #Remove duplicates
    unique_characters = []
    seen = set()
    for char in key:
        if char not in seen:
            seen.add(char)
            unique_characters.append(char)
    
    unique_characters = [char.upper() for char in unique_characters]
    
    unique_characters = [char.replace('J', 'I') for char in unique_characters]
    
    key = ''.join(unique_characters)
    
    #Combine key with alphabet
    used = set(key)
    full_key = key + ''.join([ch for ch in alphabet if ch not in used])
    
    matrix = []
    # Iterate the full key
    for i in range(0, 25, 5): 
        row = list(full_key[i:i+5]) 
        matrix.append(row)  

    return matrix



def find_position(letter, key_square):
    """
    find_position finds the index row and column in maxtrix.
    
    Requires:
    letter (str): Must be a sequence of alphabet characters.
    key_square (list of list of str): The 5x5 matrix contains the keyword.
    
    Returns:
    tuple: A tuple containing two integers (row_index, column_index)
    
    Example:
    >>> key_square = [['P', 'L', 'A', 'Y', 'F'], ['I', 'R', 'E', 'X', 'M'], ['B', 'C', 'D', 'G', 'H'], ['K', 'N', 'O', 'Q', 'S'], ['T', 'U', 'V', 'W', 'Z']]
    >>> find_position('Y', key_square)
    (0, 3)
    """
    for row_index, row in enumerate(key_square):
        if letter in row:
            column_index = row.index(letter)
            return (row_index, column_index)
    return None


def decrypt_pair(pair, key_square):
    """
    decrypt_pair decrypts a pair of letters using the Playfair cipher rules.
    
    Requires:
    pair (str): A string of two characters(Must be alphabet characters).
    key_square (list of list of str): The 5x5 matrix contains the keyword.
    
    Returns:
    str: The decrypted pair of letters as a string.
    
    Example:
    >>> key_square = [['P', 'L', 'A', 'Y', 'F'], ['I', 'R', 'E', 'X', 'M'], ['B', 'C', 'D', 'G', 'H'], ['K', 'N', 'O', 'Q', 'S'], ['T', 'U', 'V', 'W', 'Z']]
    >>> decrypt_pair('PM', key_square)
    'AY'
    """

    # Find positions
    pos1 = find_position(pair[0], key_square)
    pos2 = find_position(pair[1], key_square)
    
    row1, col1 = pos1
    row2, col2 = pos2
    
    if row1 == row2:
        # Same row, shift left
        new_col1 = (col1 - 1) % 5
        new_col2 = (col2 - 1) % 5
        decrypted_pair = key_square[row1][new_col1] + key_square[row2][new_col2]
    elif col1 == col2:
        # Same column, shift up
        new_row1 = (row1 - 1) % 5
        new_row2 = (row2 - 1) % 5
        decrypted_pair = key_square[new_row1][col1] + key_square[new_row2][col2]
    else:
        # Rectangle rule
        decrypted_pair = key_square[row1][col2] + key_square[row2][col1]

    return decrypted_pair


def decrypt_message(message, key):
    """
    decrypt_message decrypts all the messages.
    
    Requires:
    - message (str): The message should be formatted as pairs of letters.
    - key (str): The keyword must be a sequence of alphabet characters without any duplicates.
    
    Returns:
    - str: The decrypted message as a string.
    
    Example:
    >>> key = "PLAYFAIREXAMPLE"
    >>> message = "BMODZBXDNABEKUDMUIXMMOUVIF"
    >>> decrypt_message(message, key)
    'HIDETHEGOLDINTHETREXESTUMP'
    """
    # Generate the key square from the key
    key_square = create_playfair_key_square(key)
    
    message = message.replace('J', 'I')
    
    decrypted_message = ""
    for i in range(0, len(message), 2):
        pair = message[i:i+2]
        decrypted_pair = decrypt_pair(pair, key_square)
        decrypted_message += decrypted_pair

    return decrypted_message




def clean_decrypted_message(decrypted_message):
    """
    clean_decrypted_message refines the decrypted message by removing 'X' characters that are used to separate double letters or as 
    placeholders at the end of the message. The output is also converted to uppercase and cleansed of any non-alphabetic characters.
    
    Requires:
    - decrypted_message (str): The initially decrypted message which may contain placeholder or separator 'X' characters.
    
    Returns:
    - str: A cleaned and formatted version of the decrypted message, in uppercase without unnecessary 'X' characters or non-alphabetic symbols.
    
    Example:
    >>> clean_decrypted_message('HIxDETHEGOLDINTHEXTREXESTUMPX')
    'HIDETHEGOLDINTHETREESTUMP'
    """

    decrypted_message = decrypted_message.upper()
    filtered_message = ''.join([char for char in decrypted_message if char.isalpha()])

    # Remove 'X' at the end
    while len(filtered_message) > 0 and filtered_message[-1] == 'X':
        filtered_message = filtered_message[:-1]

    # Remove 'X' used for double letters
    cleaned_message = ""
    i = 0
    while i < len(filtered_message):
        if i + 2 < len(filtered_message) and filtered_message[i] == filtered_message[i + 2] and filtered_message[i + 1] == 'X':
            cleaned_message += filtered_message[i]
            i += 2  # Skip the 'X' and move to the next valid character
        else:
            cleaned_message += filtered_message[i]
            i += 1

    return cleaned_message

#Test
key = "SUPERSPY"
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

decrypted_message = clean_decrypted_message(decrypt_message(encrypted_message, key))
print(decrypted_message)



