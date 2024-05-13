from typing import List


def construct_cipher_table(key: str, excluded_letter='J', replacement_letter='I') -> List[str]:
    """
    Construct the Playfair Cipher Table given a <key>. Playfair cipher has 25
    characters so <excluded_letter> is replaced with <replacement_letter>. The
    cipher table is returns as a 1D array.

    Args:
        key (str): 
            Playfair Cipher Key
        excluded_letter (str, optional): 
            Excluded Character from the Cipher, must be upper case. Defaults 
            to 'J'.
        replacement_letter (str, optional):
            Replacement Character for the excluded character, must be upper 
            case. Defaults to 'I'.

    Returns:
        List[List[str]]: Cipher Table
    """
    table = [None] * 25
    included_chars = set()
    cur_index = 0 # current position in the cipher table
    
    # Replace the excluded_letter with replacement_letter
    key = key.upper()
    key = key.replace(excluded_letter, replacement_letter)
    
    # fill key into cipher table
    for char in key:
        if char not in included_chars:
            table[cur_index] = char
            included_chars.add(char)
            cur_index+= 1
            
    alphabet = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    alphabet.remove(excluded_letter)
    
    # fill in rest of alphabet into cipher table
    for char in alphabet:
        if char not in included_chars:
            table[cur_index] = char
            cur_index += 1
            
    return table
      
      
def decrypt_given_table(message: str, table: List[str]) -> str:
    """
    Decrypt a Playfair Cipher <message> given a Cipher Table <table>.

    Args:
        message (str): 
            Encrypted message, length must be even, must be uppercase.
        table (List[str]): 
            Cipher table.

    Returns:
        str: Decypted original message.
    """
    decrypted = ""
    
    # get the row, col for a character
    get_row_col = lambda x: (table.index(x) // 5, table.index(x) % 5)
    
    # get the index in the table of a character from its row, col
    get_index = lambda row, col: row * 5 + col
    
    for i in range(0, len(message), 2):
        # char[0] is row, char[1] is col
        char1 = get_row_col(message[i]) 
        char2 = get_row_col(message[i + 1])
        
        if char1[0] == char2[0]:
            # Same row of cipher table
            # Move to the left by 1 in the row for each char
            decrypt_char1 = (char1[0], (char1[1] - 1) % 5)
            decrypt_char2 = (char2[0], (char2[1] - 1) % 5)
            
        elif char1[1] == char2[1]:
            # Same column of cipher table
            # Move up by 1 in the same column for each char
            decrypt_char1 = ((char1[0] - 1) % 5, char1[1])
            decrypt_char2 = ((char2[0] - 1) % 5, char2[1])
        
        else:
            # Standard case
            # encoded have swaped columns and same rows
            decrypt_char1 = (char1[0], char2[1])
            decrypt_char2 = (char2[0], char1[1])
        
        next_char1 = table[get_index(decrypt_char1[0], decrypt_char1[1])]
        next_char2 = table[get_index(decrypt_char2[0], decrypt_char2[1])]
        
        # Remove 'X' if inserted because of a repeated character
        if len(decrypted) >= 2 \
            and (decrypted[-2] == next_char1 and decrypted[-1] == 'X'):
            decrypted = decrypted[:-1]
                
        decrypted += next_char1 + next_char2
    
    # Remove last padding 'X'
    if len(decrypted) >= 1 and decrypted[-1] == 'X':
        decrypted = decrypted[:-1]
    
    return decrypted


def full_decrypt(message: str, key: str) -> str:
    """
    Decrypt a Playfair Cipher <message> given a Cipher key <key>.

    Args:
        message (str): 
            Encrypted message.
        key (str): 
            Cipher Key.

    Returns:
        str: Decypted original message.
    """
    # construct cipher table
    table = construct_cipher_table(key)
    
    # Playfair Cipher requires even length message for bigrams
    if len(message) % 2 == 1:
        message += 'X'
    message = message.upper()
        
    return decrypt_given_table(message, table)


if __name__=="__main__":
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    print(full_decrypt(message, key))
    