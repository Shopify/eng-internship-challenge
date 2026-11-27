def modify_key(key):
    """
    This function modifies a key (string) to be used for creating
    a Playfair cipher key matrix. The modifications include removing duplicates, 
    replacing Js with Is and appending the remaining letters of the alphabet (excluding 'J')

    Parameters:
        key (str): The initial key string that will be modified for the cipher matrix
    
    Returns:
        key_square (str): The modified key string 

    """

    # All alphabets excluding J 
    alphabets = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    
    # Replacing all Js with Is and converting all letters to uppercase
    key = key.replace("J", "I").upper() 
    
    # Removing duplicates from the key
    key_square = ""
    for letter in key: 
        if letter not in key_square:
            key_square += letter
    
    # Appending the rest of the alphabets to the end of the key_square
    for char in alphabets: 
        if char not in key_square:
            key_square += char

    return key_square

def create_playfair_matrix(key):
    """
    This function creates a 5x5 Playfair cipher matrix from a given key

    This function first modifies the provided key using the `modify_key` and then constructs a 5x5 matrix,
    filling it row by row with characters from the modified key

    Parameters:
        key (str): The initial string used to generate the Playfair cipher matrix

    Returns:
        matrix (list of lists): A 5x5 matrix  where each sublist represents a row in the matrix, 
            with characters from the modified key

    """
    # Modify the key to remove duplicates and exclude 'J'.
    key_square = modify_key(key)

    # Creating a matrix by segmenting the modified key into rows of five characters each
    matrix = []
    for i in range(0, 25, 5):
        row = key_square[i:i+5]
        matrix.append(row)        

    return matrix


def find_position_matrix(char, matrix):
    """
    Finds and returns the position of a character in a 5x5 Playfair cipher matrix

    Parameters:
        char (str): The character to find within the matrix
        matrix (list of lists): The 5x5 matrix where characters are stored

    Returns:
        tuple: The (row, column) indices of the character in the matrix
    """
        
    # Iterating over the rows of the matrix
    for x, row in enumerate(matrix): 
        if char in row:
            # Returning the row and the column index of the character
            return x, row.index(char) 
        
def decrypt_playfair_message(message, matrix):
    """
    Decrypts a message using the Playfair cipher process given a 5x5 cipher matrix
    
    The message undergoes pre-processing to replace 'J' with 'I' and convert to uppercase, 
    ensuring compatibility with the cipher matrix. The decryption process adjusts pairs of 
    characters from the message based on their positions within the matrix

    Parameters:
        message (str): The encrypted message to be decrypted
        matrix (list of lists): The 5x5 cipher matrix used for the decryption process

    Returns:
        str: The decrypted text
    """

    message = message.replace("J", "I").upper()

    decrypted_output = []

    for i in range(0, len(message), 2):
        # Getting a pair of characters
        pair = message[i:i+2]
        
        # Finding the matrix positions of both characters in the pair
        first_letter_position = find_position_matrix(pair[0], matrix)
        second_letter_position = find_position_matrix(pair[1], matrix)

        # If characters are in the same row, they are replaced by the letter immediately to their left, shifting each left by one position 
        # Wrapping around to the end of the row if necessary using modulo operation
        if first_letter_position[0] == second_letter_position[0]:  
            decrypted_pair = matrix[first_letter_position[0]][(first_letter_position[1]-1)%5] + matrix[second_letter_position[0]][(second_letter_position[1]-1)%5]
        
        # If characters are in the same column, they are replaced by the letter immediately above them, shifting each up by one position
        # This also wraps around to the bottom of the column if moving above the first row.
        elif first_letter_position[1] == second_letter_position[1]:  
            decrypted_pair = matrix[(first_letter_position[0]-1)%5][first_letter_position[1]] + matrix[(second_letter_position[0]-1)%5][second_letter_position[1]]
        

        # If characters are not in the same row or column, they are swapped diagonally within the rectangle
        # formed by their positions. Each character is moved to the column of its counterpart while remaining in
        # its original row,  swapping their positions in a crisscross way.
        else:  
            decrypted_pair = matrix[first_letter_position[0]][second_letter_position[1]] + matrix[second_letter_position[0]][first_letter_position[1]]
        
        decrypted_output.append(decrypted_pair)

    # Joining all pairs to generate the decrypted text
    return ''.join(decrypted_output)

def format_decrypted_output(decrypted_message):
    """
    This function formats the decrypted message by removing non-alphabetical characters,
    any occurrences of the letter 'X', and ensuring only  uppercase 
    alphabetical characters

    Parameters:
        decrypted_message (str): The decrypted message 

    Returns:
        str: The cleaned decrypted message with all characters in uppercase
    """

    # Ensuring only alphabetical characters are in the final output
    formatted_output = ''
    for char in decrypted_message:
        if char.isalpha():
            formatted_output += char
            
    # Removing any 'X' from the final output 
    formatted_output = formatted_output.replace('X', '').upper()

    return formatted_output

# testing
key = "SUPERSPY"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# creating a matrix 
matrix = create_playfair_matrix(key)

# decrypting the message
decrypted_message = decrypt_playfair_message(message, matrix)

# formatting (removing X and non alpha chars)
final_output = format_decrypted_output(decrypted_message)
print(final_output)