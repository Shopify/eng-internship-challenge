def create_key_square(key):
    # Cleans and prepare the key by removing duplicates and excluding "J" from the alphabet
    # Merges J with I
    key = key.upper().replace("J", "I")
    # unique_letters = []
    seen_char = set()
    key_square = []
    for char in key:
        if char not in seen_char and char.isalpha():
            seen_char.add(char)
            key_square.append(char)
            # unique_letters.append(char)

    # Fills key square with remaining letters that weren't in the key.
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ".replace("J", "")
    for char in alphabet:
        if char not in seen_char:
            # unique_letters.append(char)
            key_square.append(char)

    # return unique_letters
    return key_square


def decrypt_playfair(ciphertext, key):

    key_square = create_key_square(key)
    empty_text = ""
    size = 5  # Size is 5 as our playfair uses 5x5 matrix

    # Decrypt each pair of the characters
    for index in range(0, len(ciphertext), 2):
        first_char = ciphertext[index]
        second_char = ciphertext[index+1]
        # Find the indices of the characters in the key square
        index_first_char = key_square.index(first_char)
        index_second_char = key_square.index(second_char)

        # Calculate the row and column
        row1 = index_first_char // size  # Integer division to find the row
        col1 = index_first_char % size   # modulus to find the column

        row2 = index_second_char // size
        col2 = index_second_char % size

        # Apply decryption rules based on the positions
        if row1 == row2:
            # It's the same row, so shift left
            decrypted_pair = key_square[row1 * size + (
                col1 - 1) % size] + key_square[row2 * size + (col2 - 1) % size]
        elif col1 == col2:
            # It's the same column, so shift up
            decrypted_pair = key_square[(
                (row1 - 1) % size) * size + col1] + key_square[((row2 - 1) % size) * size + col2]
        else:
            # Rectangle swap, it's the same row and opposite column
            decrypted_pair = key_square[row1 * size +
                                        col2] + key_square[row2 * size + col1]

        empty_text += decrypted_pair

    # Remove "X" from the text
    new_text = empty_text.replace("X", "")
    return new_text


def main():
    key = "SUPERSPY"
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decrypted_text = decrypt_playfair(ciphertext, key)
    print(decrypted_text)


if __name__ == "__main__":
    main()
