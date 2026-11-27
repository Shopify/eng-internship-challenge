LETTERS = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # excluding J by cipher table convention

### HELPER FUNCTIONS

def build_table(key_phrase):
    """
    build_table returns table and letter_to_position
    
    table: a 5x5 matrix of letters by appending all "unconsidered" letters in key_phrase, then doing the same for LETTERS (alphabet without 'J').
    letter_to_position: a map between a letter and it's position in table
    """
    seen_letters = set()
    table = [['' for _ in range(5)] for _ in range(5)]
    letter_to_position = {}
    row, col = 0, 0

    for letter in key_phrase + LETTERS:
        if letter == 'J':
            letter = 'I' # J and I are equivalent (Playfair standard)
        if letter not in seen_letters: # add letter to table and record it's position
            table[row][col] = letter
            seen_letters.add(letter)
            letter_to_position[letter] = (row, col)
            col = (col + 1) % 5
            if col == 0:
                row += 1
    
    return table, letter_to_position

def make_digrams(message):
    """
    make_digrams returns a list of 2-letter partitions of message, in order from left to right.
    """
    return [message[i: i+2] for i in range(0, len(message), 2)]

def decrypt_digrams(digrams, table, letter_to_position):
    """
    decrypt_digrams decrypts each digram from digrams and returns a list of the resulting 2-letter chunks
    """
    decrypted_digrams = ['' for _ in range(len(digrams))]
    for i, digram in enumerate(digrams):
        ch1, ch2 = digram[0], digram[1]
        row1, col1 = letter_to_position[ch1]
        row2, col2 = letter_to_position[ch2]
        if row1 == row2: # construct by moving left, wrapping if necessary
            decrypted_digrams[i] = table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
        elif col1 == col2: # construct by moving upwards, wrapping if necessary
            decrypted_digrams[i] = table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
        else: # rectangle case - use opposite corners
            decrypted_digrams[i] = table[row1][col2] + table[row2][col1]
    
    return decrypted_digrams

### DECRYPT FUNCTION

def decrypt(encrypted_message, key_phrase):
    """
    decrypt decrypts an encrypted_message using key_phrase, and assumes that encrypted_message was encrypted using the Playfair cipher encryption algorithm.
    """

    # format the message and key (uppercase, no spaces)
    encrypted_message, key_phrase = encrypted_message.upper().replace(' ', ''), key_phrase.upper().replace(' ', '')

    # build a 5x5 matrix according to playfair algorithm
    table, letter_to_position = build_table(key_phrase)

    # split message into length-2 chunks
    digrams = make_digrams(encrypted_message)

    # decrypt each chunk
    decrypted_digrams = decrypt_digrams(digrams, table, letter_to_position)

    # create word from decrypted chunks with requested format
    return ''.join(decrypted_digrams).replace('X', '')

def main():
    print(decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))

if __name__ == "__main__":
    main()