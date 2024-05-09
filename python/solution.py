# Alphabets excluding 'J' as the Playfair cipher rules
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def create_key_square(key: str)-> list[list[str]]: 
    """
    Creates a key square for a Playfair cipher based on the given key.

    The key square is a 5x5 grid of characters used in the Playfair cipher.
    It is created by removing duplicate letters, "J", and non-alphabet characters from the key,
    and then filling the remaining spaces with the remaining alphabet characters.

    Args:
        key (str): The key used to create the key square.

    Returns:
        list: A 5x5 grid of characters representing the key square.

    Example:
        >>> create_key_square("playfair")
            [['P', 'L', 'A', 'Y', 'F'], 
            ['I', 'R', 'B', 'C', 'D'], 
            ['E', 'G', 'H', 'K', 'M'], 
            ['N', 'O', 'Q', 'S', 'T'], 
            ['U', 'V', 'W', 'X', 'Z']]
    """
    # Remove duplicate & non-alphabet characters from key
    key = key.upper()
    filtered_key = "".join(sorted(set(key), key=key.index))
    # Create the key square
    key_square = []
    
    for c in filtered_key:
        if c not in key_square:
            key_square.append(c)
    for c in alphabet:
        if c not in key_square:
            key_square.append(c)
            
    # Generate a 5x5 grid from the key square
    return [key_square[i:i+5] for i in range(0, 25, 5)]

def decrypt_pair(pair: str, key_square: list[list[str]]) -> str:
    """
    Decrypts a pair of letters using a key square.

    Args:
        pair (str): The pair of letters to decrypt.
        key_square (list): The key square used for decryption.

    Returns:
        str: The decrypted pair of letters.
    """
    # Locate both letters in the key square
    pos1, pos2 = (None, None), (None, None)
    for r in range(5):
        for c in range(5):
            if key_square[r][c] == pair[0]:
                pos1 = (r, c)
            if key_square[r][c] == pair[1]:
                pos2 = (r, c)
    r1, c1 = pos1
    r2, c2 = pos2
    # Apply decryption rules from the Playfair cipher
    if r1 == r2:
        return key_square[r1][(c1-1) % 5] + key_square[r2][(c2-1) % 5]
    elif c1 == c2:
        return key_square[(r1-1) % 5][c1] + key_square[(r2-1) % 5][c2]
    else:
        return key_square[r1][c2] + key_square[r2][c1]

def decrypt_playfair(ciphertext: str, key: str) -> str:
    """
    Decrypts a Playfair cipher given a ciphertext and a key.

    Parameters:
    ciphertext (str): The encrypted text to be decrypted.
    key (str): The key used for encryption.

    Returns:
    str: The decrypted plaintext.

    """
    key_square = create_key_square(key.upper())
    ciphertext = ciphertext.replace(" ", "").upper()
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(ciphertext[i:i+2], key_square)
    # Remove padding if necessary (commonly 'X')
    if plaintext[-1] == 'X':
        plaintext = plaintext[:-1]
    return plaintext.replace('X', '')

if __name__ == "__main__":
    # print(create_key_square("playfair"))
    
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    
    # key = "monarchy"
    # ciphertext = "gatlmzclrqtx"
    
    # key = "Shaco"
    # ciphertext = "ASXHGSPUCLOEMSUTMSLKVKRAMNHLFXGZBKHCRVRBEX"
    
    decrypted_text = decrypt_playfair(ciphertext, key)
    print(decrypted_text)