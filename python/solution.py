def create_playfair_table(key):
    """
    Constructs a 5x5 Playfair key table using the provided key
        Paramters:
            key (str): Key to the cipher
        Returns:
            table (2d list): 5x5 table made with the key
    """

    # Removing duplicates in the key
    seen = set()
    processed_key = ''
    for c in key:
        if c not in seen:
            seen.add(c)
            processed_key += (c)
    processed_key = processed_key.upper()
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_table = processed_key + ''
    for c in alphabet:
        if c not in processed_key:
            key_table += c

    # Create a 5x5 table
    table = []
    for i in range(0, 25, 5):
        table.append(key_table[i:i+5])
    return table

def get_position(letter, table):
    """
    Gets positon/coordinates of the letter in the 5x5 table
        Paramters:
            letter (str): The letter we are looking for
            table (2d list): 5x5 table made with the key
        Returns:
            tuple[int, int] | None: The row and column indices of the letter if found, otherwise None.
    """

    for row in range(5):
        for col in range(5):
            if table[row][col] == letter:
                return row, col
    return None

def decrypt_playfair(ciphertext, key):
    """
    Decrypts ciphertext with the given key using the Playfair algorithem
        Paramters:
            ciphertext (str): The ciphertext that is being decrypted
            key (str): Key to the cipher
        Returns:
            decrypted_text (str): The decrypted message
    """

    # If there are characters other than the alphabet stop the program
    if not ciphertext.isalpha(): raise Exception("Exception: Ciphertext contains invalid characters. ")

    # Create the Playfair key table
    table = create_playfair_table(key)

    # Check if length of ciphertext is odd and append 'X' if it is odd
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'
    
    # Process ciphertext into pairs of letters
    pairs = []
    for i in range(0, len(ciphertext), 2):
        pairs.append(ciphertext[i:i+2].upper())

    # Decrypting process
    decrypted_text = ""
    for pair in pairs:
        r1, c1 = get_position(pair[0], table)
        r2, c2 = get_position(pair[1], table)

        if r1 == r2:    # same row:     move left
            decrypted_text += table[r1][c1 - 1]
            decrypted_text += table[r2][c2 - 1]
        elif c1 == c2:  # same column:  move up
            decrypted_text += table[r1 - 1][c1]
            decrypted_text += table[r2 - 1][c2]
        else:           # rectangle:    swap column
            decrypted_text += table[r1][c2]
            decrypted_text += table[r2][c1]
    
    decrypted_text = decrypted_text.replace('X', '')

    return decrypted_text

if __name__ == "__main__":
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt_playfair(ciphertext, key))