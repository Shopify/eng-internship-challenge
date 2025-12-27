def generate_playfair_square(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Ignoring 'J' as per Playfair Cipher rules
    key = key.upper().replace("J", "I")  # Convert to uppercase and replace 'J' with 'I'
    key_set = set()
    playfair_square = []

    row = []  # Initialize an empty row
    for char in key + alphabet:
        if char not in key_set:
            row.append(char)  # Add character to the current row
            key_set.add(char)
            if len(row) == 5:   # Check if the row is full
                playfair_square.append(row)  # Add the row to the Playfair square
                row = []  # Reset the row for the next iteration

    return playfair_square

def find_char_positions(matrix, char):
    positions = []
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            if val == char:
                positions.append((i, j))
    return positions

def decrypt_message(playfair_square, encrypted_message):
    decrypted_message = ""
    for i in range(0, len(encrypted_message), 2):
        char1 = encrypted_message[i]
        char2 = encrypted_message[i + 1]

        char1_positions = find_char_positions(playfair_square, char1)
        char2_positions = find_char_positions(playfair_square, char2)

        if char1_positions and char2_positions:  # Ensure positions are found
            char1_row, char1_col = char1_positions[0]
            char2_row, char2_col = char2_positions[0]

            if char1_row == char2_row:  # Same row
                decrypted_message += playfair_square[char1_row][(char1_col - 1) % 5]
                decrypted_message += playfair_square[char2_row][(char2_col - 1) % 5]
            elif char1_col == char2_col:  # Same column
                decrypted_message += playfair_square[(char1_row - 1) % 5][char1_col]
                decrypted_message += playfair_square[(char2_row - 1) % 5][char2_col]
            else:  # Forming rectangle
                decrypted_message += playfair_square[char1_row][char2_col] if char2_col < 5 else playfair_square[char1_row][0]
                decrypted_message += playfair_square[char2_row][char1_col] if char1_col < 5 else playfair_square[char2_row][0]

    return decrypted_message

def main():
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    playfair_square = generate_playfair_square(key)
    decrypted_message = decrypt_message(playfair_square, encrypted_message)

    decrypted_message = "".join(filter(str.isupper, decrypted_message))  # Keep uppercase letters only
    decrypted_message = decrypted_message.replace("X", "")  # Remove 'X'
    decrypted_message = decrypted_message.replace(" ", "")  # Remove spaces

    print(decrypted_message)

if __name__ == "__main__":
    main()
