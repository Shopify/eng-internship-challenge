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
    # Replace all J's with I if needed
    processed_key = processed_key.replace('J', 'I').upper()
    
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

def get_positions_map(table):
    """
    Maps all letters with its corresponding location on the table
        Paramters:
            table (2d list): 5x5 table made with the key
        Returns:
            positions (dict): Dictionary with Key's being the letter and Values being location as a tuple (int, int)
    """
    positions = {}
    for row in range(5):
        for col in range(5):
            positions[table[row][col]] = row, col
    
    return positions

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

    # Replace all J's with I if needed
    ciphertext = ciphertext.upper().replace('J', 'I')
    # Check if length of ciphertext is odd and append 'X' if it is odd
    if len(ciphertext) % 2 != 0:
        ciphertext += 'X'

    # Process ciphertext into pairs of letters
    pairs = []
    for i in range(0, len(ciphertext), 2):
        pairs.append(ciphertext[i:i+2].upper())

    # Decrypting process
    positions = get_positions_map(table)
    decrypted_text = ""
    for pair in pairs:
        r1, c1 = positions[pair[0]]
        r2, c2 = positions[pair[1]]

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