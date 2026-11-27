def decrypt(key: str, ciphertext: str) -> str:
    """
    Decrypts a ciphertext using the Playfair cipher.

    Arguments:
        key: The key used to encrypt the plaintext.
        ciphertext: The ciphertext to decrypt.

    Raises:
        ValueError: If the ciphertext has an odd number of characters.

    Returns:
        The decrypted plaintext.
    """

    if len(ciphertext) % 2 != 0:
        raise ValueError("The ciphertext must have an even number of characters.")
    
    # Normalize the inputs in case they contains lowercase letters or spaces
    key = key.upper()
    key = key.replace(" ", "")
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace(" ", "")

    # Create the Playfair square

    used_letters: set[str] = set()
    key_idx: int = 0
    alpha_char_unicode: int = ord("A")
    square: list[list[str]] = []

    for i in range(5):
        square.append([])
        for _ in range(5):
            # Make sure we use all the key letters first but don't repeat any
            while key_idx < len(key) and key[key_idx] in used_letters:
                key_idx += 1

            if key_idx < len(key):
                char = key[key_idx]
                square[i].append(char)
                used_letters.add(char)

                # We treat I and J as the same letter to fit the alphabet in the square
                if char == "I" or char == "J":
                    used_letters.add("J")
                    used_letters.add("I")
            else:
                # Fill the rest of the square with the remaining unused alphabet letters
                while chr(alpha_char_unicode) in used_letters:
                    alpha_char_unicode += 1
                
                square[i].append(chr(alpha_char_unicode))
                used_letters.add(chr(alpha_char_unicode))

                # We treat I and J as the same letter to fit the alphabet in the square
                if chr(alpha_char_unicode) == "I" or chr(alpha_char_unicode) == "J":
                    used_letters.add("J")
                    used_letters.add("I")

    # Decrypt the ciphertext

    decrypted_text: str = ""

    for i in range(0, len(ciphertext), 2):
        char1: str = ciphertext[i]
        char2: str = ciphertext[i + 1]

        # Find the positions of the characters in the square
        char1_pos: tuple[int, int] = (-1, -1)
        char2_pos: tuple[int, int] = (-1, -1)

        for row_idx, row in enumerate(square):
            if char1 in row:
                char1_pos = (row_idx, row.index(char1))
            if char2 in row:
                char2_pos = (row_idx, row.index(char2))

        # Decrypt the characters
        if char1_pos[0] == char2_pos[0]:
            # Same row
            decrypted_text += square[char1_pos[0]][(char1_pos[1] - 1) % 5]
            decrypted_text += square[char2_pos[0]][(char2_pos[1] - 1) % 5]
        elif char1_pos[1] == char2_pos[1]:
            # Same column
            decrypted_text += square[(char1_pos[0] - 1) % 5][char1_pos[1]]
            decrypted_text += square[(char2_pos[0] - 1) % 5][char2_pos[1]]
        else:
            decrypted_text += square[char1_pos[0]][char2_pos[1]]
            decrypted_text += square[char2_pos[0]][char1_pos[1]]

    # Remove any "X" characters that were added to make the ciphertext have an even length or to separate repeated characters
    return decrypted_text.replace("X", "")


if __name__ == '__main__':
    KEY = "SUPERSPY"
    CIPHERTEXT = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    print(decrypt(KEY, CIPHERTEXT))