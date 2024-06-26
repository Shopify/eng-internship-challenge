# Normalize the key by removing duplicates, ignore non-alphabet characters, and replacing 'J' with 'I'.
def normalize_key(key):
    seen = set()
    normalized_key = []
    key = key.upper().replace('J', 'I')
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            normalized_key.append(char)
    return normalized_key

# Complete the key by adding the missing alphabet characters to form the cipher grid.
def fill_key_with_alphabet(normalized_key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in normalized_key:
            normalized_key.append(char)
    return normalized_key

# Create a 5x5 grid from the processed key
def create_cipher_grid(key):
    normalized_key = normalize_key(key)
    completed_key = fill_key_with_alphabet(normalized_key)
    return [completed_key[i * 5:(i + 1) * 5] for i in range(5)]

# Find the row and column of the character in the grid
def find_character_position(grid, char):
    for row_index, row in enumerate(grid):
        if char in row:
            return (row_index, row.index(char))
    return None

# Decrypt digraphs according to Playfair cipher rules
def decrypt_digraphs(grid, text):
    decrypted_text = ''
    index = 0
    while index < len(text):
        char1 = text[index]
        char2 = text[index + 1] if index + 1 < len(text) else 'X'
        r1, c1 = find_character_position(grid, char1)
        r2, c2 = find_character_position(grid, char2)
        if r1 == r2:  # Same row
            decrypted_text += grid[r1][(c1 - 1) % 5] + grid[r2][(c2 - 1) % 5]
        elif c1 == c2:  # Same column
            decrypted_text += grid[(r1 - 1) % 5][c1] + grid[(r2 - 1) % 5][c2]
        else:  # Rectangle swap
            decrypted_text += grid[r1][c2] + grid[r2][c1]
        index += 2
    return decrypted_text

# Main function to decrypt ciphertext using the Playfair cipher method
def decrypt_playfair(ciphertext, key):
    grid = create_cipher_grid(key)
    cleaned_text = ''.join([c for c in ciphertext.upper() if c.isalpha()])
    if len(cleaned_text) % 2 != 0:
        cleaned_text += 'X'
    return decrypt_digraphs(grid, cleaned_text).replace('X', '')

# Example usage
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

# Output decrypted message
decrypted_message = decrypt_playfair(ciphertext, key)
print(decrypted_message)
