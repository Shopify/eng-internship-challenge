def generate_playfair_square(key):
    """Generate the Playfair cipher square as a dictionary mapping characters to their positions (row, col).

    Args:
        key (str): The key used for generating the Playfair cipher square.

    Returns:
        dict: A dictionary where keys are characters and values are tuples (row, col) representing positions in the square.
    """
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Ignoring 'J' as per Playfair Cipher rules
    key = key.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    
    playfair_square = {}
    key_set = set()
    
    # Build the Playfair square dictionary
    row, col = 0, 0
    for char in key + alphabet:
        if char not in key_set:
            # Assign the current character to the current position (row, col)
            playfair_square[char] = (row, col)
            key_set.add(char)  # Add the character to the set of seen characters
            col += 1  # Move to the next column
            
            # If we have filled a row (5 columns), move to the next row
            if col == 5:
                col = 0  # Reset column to start a new row
                row += 1  # Move to the next row
                
                # Stop filling the square if we have completed 5 rows
                if row == 5:
                    break
    
    return playfair_square

def decrypt_message(playfair_square, encrypted_message):
    """Decrypt an encrypted message using the provided Playfair cipher square.

    Args:
        playfair_square (dict): A dictionary representing the Playfair cipher square.
        encrypted_message (str): The encrypted message to decrypt.

    Returns:
        str: The decrypted message.
    """
    decrypted_message = []
    length = len(encrypted_message)
    i = 0
    
    # Process the encrypted message in pairs of characters
    while i < length:
        char1 = encrypted_message[i]
        char2 = encrypted_message[i + 1]

        # Get positions of the characters from the Playfair square dictionary
        char1_row, char1_col = playfair_square[char1]
        char2_row, char2_col = playfair_square[char2]

        if char1_row == char2_row:  # Characters are in the same row
            # Decrypt characters based on the same-row rule
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index((char1_row, (char1_col - 1) % 5))])
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index((char2_row, (char2_col - 1) % 5))])
        elif char1_col == char2_col:  # Characters are in the same column
            # Decrypt characters based on the same-column rule
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index(((char1_row - 1) % 5, char1_col))])
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index(((char2_row - 1) % 5, char2_col))])
        else:  # Characters form a rectangle in the square
            # Decrypt characters based on the rectangle rule
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index((char1_row, char2_col if char2_col < 5 else 0))])
            decrypted_message.append(list(playfair_square.keys())[list(playfair_square.values()).index((char2_row, char1_col if char1_col < 5 else 0))])

        i += 2  # Move to the next pair of characters in the encrypted message
    
    return "".join(decrypted_message)

def main():
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    # Generate the Playfair cipher square
    playfair_square = generate_playfair_square(key)

    # Decrypt the encrypted message
    decrypted_message = decrypt_message(playfair_square, encrypted_message)

    # Further processing: keep uppercase letters only, remove 'X' and spaces
    decrypted_message = "".join(filter(str.isupper, decrypted_message))  # Keep uppercase letters only
    decrypted_message = decrypted_message.replace("X", "")  # Remove 'X'
    decrypted_message = decrypted_message.replace(" ", "")  # Remove spaces

    # Output the decrypted message
    print(decrypted_message)

if __name__ == "__main__":
    main()