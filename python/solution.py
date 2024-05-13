from typing import List


def construct_cipher_table(key: str, excluded_letter='j') -> List[str]:
    """
    Construct the Playfair Cipher Table given a <key> and <excluded_letter>.
    The cipher table is returns as a 1D array

    Args:
        key (str): Playfair Cipher Key
        excluded_letter (str, optional): Excluded Character from the Cipher. Defaults to 'j'.

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
            
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet.remove(excluded_letter)
    
    # fill in rest of alphabet into cipher table
    for char in alphabet:
        if char not in included_chars:
            table[cur_index] = char
            cur_index += 1
            
    return table
      

def full_decrypt(message: str, key: str) -> str:
    """
    Decrypt a Playfair Cipher <message> and given a Cipher key <key>.

    Args:
        message (str): Encrypted message.
        key (str): Cipher Key.

    Returns:
        str: Decypted original message.
    """
    # construct cipher table
    table = construct_cipher_table(key)
    
    return ""


if __name__=="__main__":
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    print(full_decrypt(message, key))
    