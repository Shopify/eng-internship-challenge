def remove_duplicates_from_keyword(keyword):
    """remove duplicates from given keyword

    Args:
        keyword (string): the keyword string which we are trying to remove the duplicate characters

    Returns:
        string: The keyword argument without duplicate characters, in uppercase
    """
    
    # set variable to prevent and check for duplicated characters
    single_chr = set()
    sanitized_word = ""

    keyword = keyword.replace(" ", '').upper()

    for chr in keyword:
        if chr not in single_chr:
            sanitized_word += chr
            single_chr.add(chr)
            
    return sanitized_word
            
def create_table(keyword):
    """Creates a 5x5 2d-list containing the keyword argument and letters of the alphabet without the letter J

    Args:
        keyword (str): The sanitized keyword(no duplicates, uppercase) to be used in building the table 

    Returns:
        list: The 2d-list which will represent the playfair cipher table
    """
    
    # alphabet letters without the letter "J"
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    for char in keyword:
        if char in alphabet:
            alphabet = alphabet.replace(char, '')

    size = 5
    
    # Create an empty table with 2D array 
    table = [[None for _ in range(size)] for _ in range(size)]
    
    key_index = 0  
    for i in range(size):
        for j in range(size):
            if key_index < len(keyword):
                table[i][j] = keyword[key_index]
                key_index += 1
            else:
                table[i][j] = alphabet[key_index - len(keyword)]
                key_index += 1
                
    return table

def get_position(char, table): 
    """Obtains the position for a single character in the table provided

    Args:
        char (str): The single string character which we are trying to get the position.
        table (list): The playfair cipher table to get the position for the character argument 

    Returns:
        tuple: The row and column positions for the single string charcter argument
    """
    
    for i, row in enumerate(table):
        for j, value in enumerate(row):
            if  value == char:
                return (i, j)
            
def decrypt_playfair_cipher(message, table):
    """Decrypts the playfair cipher message using the provided table

    Args:
        message (string): The encrypted message to be decrypted
        table (string): The Playfair table to be used for decryption

    Returns:
        str: The decrypted message without special characters, spaces, letter X in upper case
        
    Raises:
        ValueError: If the encrypted message is not a multiple of 2
    """
    
    if len(message) % 2 != 0 :
        raise ValueError("Invalid length. Encrypted message must be a multiple of 2")
    
    decrypted_message = ""
    
    # preprocess encrypted message
    message = message.replace(" ", '').upper()
    message = "".join(e for e in message if e.isalpha())
        
    for i in range(0, len(message), 2):
        pair = message[i: i+2]
        
        pos1 = get_position(pair[0], table)
        pos2 = get_position(pair[1], table)
        
        if pos1[0] == pos2[0]:
            decrypted_message += table[pos1[0]][(pos1[1] - 1) % 5]
            decrypted_message += table[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:
            decrypted_message += table[(pos1[0] - 1) % 5][pos1[1]]
            decrypted_message += table[(pos2[0] - 1) % 5][pos2[1]]
        else:
            decrypted_message += table[pos1[0]][pos2[1]]
            decrypted_message += table[pos2[0]][pos1[1]]
             
    decrypted_message = decrypted_message.replace("X", "")
            
    return decrypted_message

def main():
    keyword = 'SUPERSPY'
    message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINChcv'
    
    sanitized_word = remove_duplicates_from_keyword(keyword)
    table = create_table(sanitized_word)
    
    output = decrypt_playfair_cipher(message, table)
    print(output)

if __name__ == '__main__':
    main()