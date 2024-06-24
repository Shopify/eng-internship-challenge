from collections import deque
from string import ascii_uppercase

def generate_key_table(key):
    # The 5x5 table of letters
    key_table = [[None] * 5 for i in range(5)]

    # Used to quickly look up the row and column of a letter
    letter_locations = {}

    # Queue up the letters in the key followed by the letters of the alphabet (not including J)
    queue = deque(key + ascii_uppercase.replace('J', ''))
    for row in range(0, 5):
        for col in range(0, 5):
            # Get the next letter that has not yet been placed in the table
            letter = queue.popleft()
            while letter in letter_locations:
                letter = queue.popleft()
            
            key_table[row][col] = letter
            letter_locations[letter] = (row, col)
    return key_table, letter_locations

def decrypt_playfair(ciphertext, key):
    key_table, letter_locations = generate_key_table(key)

    # Reverse the encryption process for every pair of letters in the ciphertext
    plaintext = []
    for i in range(0, len(ciphertext), 2):
        row1, col1 = letter_locations[ciphertext[i]]
        row2, col2 = letter_locations[ciphertext[i + 1]]

        if row1 == row2:
            first_letter = key_table[row1][(col1 - 1) % 5]
            second_letter = key_table[row2][(col2 - 1) % 5]
        elif col1 == col2:
            first_letter = key_table[(row1 - 1) % 5][col1]
            second_letter = key_table[(row2 - 1) % 5][col2]
        else:
            first_letter = key_table[row1][col2]
            second_letter = key_table[row2][col1]
        
        plaintext.append(first_letter)
        # Ignore X's used for separation
        if second_letter != 'X':
            plaintext.append(second_letter)
    return ''.join(plaintext)

def main():
    ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERSPY'
    print(decrypt_playfair(ciphertext, key))

if __name__ == '__main__':
    main()