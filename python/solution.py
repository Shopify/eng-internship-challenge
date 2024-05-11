def create_cipher_table(keyword):
    """
    Generates a 5x5 cipher table for the Playfair cipher based on a provided keyword.
    
    The function first normalizes the keyword by converting it to uppercase and removing duplicate letters.
    It then creates a list of characters from the normalized keyword, followed by the remaining letters of the
    alphabet, excluding 'J' (which is traditionally omitted in the Playfair cipher to fit the 25-cell table).
    
    Parameters:
    keyword (str): The keyword used to generate the initial part of the cipher table.
    
    Returns:
    list of list of str: A 5x5 matrix representing the cipher table.
    """
    # Normalize the keyword: uppercase and remove duplicates
    formatted_keyword = ''.join(sorted(set(keyword.upper()), key=keyword.index))
    
    # Remove 'J' from the alphabet and prepare the rest of the letters
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    
    # Create the cipher table starting with the keyword
    used_letters = set(formatted_keyword)
    table = [char for char in formatted_keyword]
    
    # Fill the table with the remaining letters
    for char in alphabet:
        if char not in used_letters:
            table.append(char)
    
    # Group the letters into a 5x5 matrix
    cipher_table = [table[i:i+5] for i in range(0, 25, 5)]
    return cipher_table


def find_position(letter, cipher_table):
    """
    Find the position (row, col) of a letter in the cipher table.
    """
    for row_index, row in enumerate(cipher_table):
        if letter in row:
            return (row_index, row.index(letter))
    return None

def decrypt_digram(digram, cipher_table):
    """
    Decrypt a single digram according to Playfair cipher rules.
    """
    row1, col1 = find_position(digram[0], cipher_table)
    row2, col2 = find_position(digram[1], cipher_table)

    if row1 == row2:
        # Same row: shift letters left
        decrypted = cipher_table[row1][(col1 - 1) % 5] + cipher_table[row2][(col2 - 1) % 5]
    elif col1 == col2:
        # Same column: shift letters up
        decrypted = cipher_table[(row1 - 1) % 5][col1] + cipher_table[(row2 - 1) % 5][col2]
    else:
        # Rectangle: swap columns
        decrypted = cipher_table[row1][col2] + cipher_table[row2][col1]

    return decrypted

def clean_decrypted_message(decrypted_message):
    """
    Clean up the decrypted message by handling 
    padding and special cases, including 'X' characters.
    """
    # First pass to remove 'X' that are clearly padding or inserted for repeated letters
    cleaned_message = ""
    i = 0
    while i < len(decrypted_message):
        if i + 2 < len(decrypted_message) and decrypted_message[i] == decrypted_message[i + 2]:
            # Check if 'X' is between two same letters
            if decrypted_message[i + 1] == 'X':
                cleaned_message += decrypted_message[i]
                i += 2  # Skip the 'X' and the next repeated letter
            else:
                cleaned_message += decrypted_message[i]
                i += 1
        else:
            cleaned_message += decrypted_message[i]
            i += 1

    # Second pass to remove trailing 'X', if exists
    if cleaned_message.endswith('X'):
        cleaned_message = cleaned_message[:-1]

    return cleaned_message

def decrypt_message(encrypted_message, cipher_table):
    """
    Decrypt an entire message using the Playfair cipher.
    """
    encrypted_message = encrypted_message.replace(" ", "").upper()
    decrypted_message = ""

    # Process the message in digrams
    for i in range(0, len(encrypted_message), 2):
        digram = encrypted_message[i:i+2]
        decrypted_digram = decrypt_digram(digram, cipher_table)
        decrypted_message += decrypted_digram

    # Handle potential padding 'X' and clean the decrypted message
    return clean_decrypted_message(decrypted_message)

if __name__ == "__main__":
    cipher_table = create_cipher_table("SUPERSPY")
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_message = decrypt_message(encrypted_message, cipher_table)
    print(decrypted_message)
