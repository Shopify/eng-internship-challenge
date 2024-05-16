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
    
    #Convert to uppercase
    unique_characters = [char.upper() for char in unique_characters]
    
    #Replace J with I
    unique_characters = [char.replace('J', 'I') for char in unique_characters]
    
    #Join characters into a single string
    key = ''.join(unique_characters)
    
    #Combine key with alphabet
    used = set(key)
    full_key = key + ''.join([ch for ch in ALPHABET if ch not in used])
    
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




