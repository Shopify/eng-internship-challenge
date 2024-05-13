from typing import List


def construct_cipher_table(key: str, excluded_letter='J') -> List[str]:
    """
    Construct the Playfair Cipher Table given a <key> and <excluded_letter>.
    The cipher table is returns as a 1D array

    Args:
        key (str): 
            Playfair Cipher Key
        excluded_letter (str, optional): 
            Excluded Character from the Cipher. Defaults to 'J'.

    Returns:
        List[List[str]]: Cipher Table
    """
    
    table = [None] * 25
    included_chars = set()

    cur_index = 0 # current position in the cipher table
    
    # fill key into cipher table
    for char in key:
        if char not in included_chars:
            table[cur_index] = char
            included_chars.add(char)
            cur_index+= 1
            
    alphabet = [char for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    alphabet.remove(excluded_letter.upper())
    
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
        message (str): Encrypted message.
        table (List[str]): Cipher table.

    Returns:
        str: Decypted original message.
    """
    decrypted = ""
    
    get_row_col = lambda x: (table.index(x) // 5, table.index(x) % 5)
    get_index = lambda row, col: row * 5 + col
    
    for i in range(0, len(message), 2):
        #
        char1_row, char1_col = get_row_col(message[i])
        char2_row, char2_col = get_row_col(message[i + 1])
        
        if char1_row == char2_row:
            d_char1_row = char1_row
            d_char2_row = char1_row
            
            d_char1_col = (char1_col - 1) % 5
            d_char2_col = (char2_col - 1) % 5
            
        elif char1_col == char2_col:
            d_char1_row = (char1_row - 1) % 5
            d_char2_row = (char2_row - 1) % 5
            
            d_char1_col = char1_col
            d_char2_col = char1_col
        
        else:
            d_char1_row = char1_row
            d_char2_row = char2_row
            
            d_char1_col = char2_col
            d_char2_col = char1_col
        
        next_char1 = table[get_index(d_char1_row, d_char1_col)]
        next_char2 = table[get_index(d_char2_row, d_char2_col)]
        # check if we have 'X' inserted because of a repeated character
        if len(decrypted) >= 2 and (decrypted[-2] == next_char1 and decrypted[-1] == 'X'):
            decrypted = decrypted[:-1] + next_char1 + next_char2
        else:
            decrypted += next_char1 + next_char2
    
    # remove last padding 'X'
    if len(decrypted) >= 1 and decrypted[-1] == 'X':
        decrypted = decrypted[:-1]
    
    return decrypted


def full_decrypt(message: str, key: str) -> str:
    """
    Decrypt a Playfair Cipher <message> given a Cipher key <key>.

    Args:
        message (str): Encrypted message.
        key (str): Cipher Key.

    Returns:
        str: Decypted original message.
    """
    # construct cipher table
    table = construct_cipher_table(key)
    
    return decrypt_given_table(message, table)


if __name__=="__main__":
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    print(full_decrypt(message, key))
    