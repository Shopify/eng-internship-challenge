import sys

def generate_playfair_grid(key):
    # Remove 'J' from the base alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    
    # Remove duplicates from the key while preserving order
    seen = set()
    key = ''.join(char for char in key.upper() if not (char in seen or seen.add(char)))
    
    # Concatenate key and alphabet
    key_alphabet = key + alphabet
    
    # Create the grid string
    grid_string = ''
    for char in key_alphabet:
        if char not in grid_string:
            grid_string += char
    
    # Fill in missing letters if necessary
    for char in alphabet:
        if char not in grid_string:
            grid_string += char
    
    # Convert the grid string to a 5x5 grid
    grid_matrix = [list(grid_string[i:i+5]) for i in range(0, 25, 5)]
    
    return grid_matrix

def decrypt_playfair(ciphertext, key):
    grid = generate_playfair_grid(key)
    plaintext = ""
    ciphertext = ciphertext.upper().replace("J", "I")
    
    # Find positions of letters in the grid
    positions = {}
    for i in range(5):
        for j in range(5):
            positions[grid[i][j]] = (i, j)
    
    # Insert 'X' between consecutive identical letters
    i = 0
    while i < len(ciphertext) - 1:
        if ciphertext[i] == ciphertext[i+1]:
            ciphertext = ciphertext[:i+1] + 'X' + ciphertext[i+1:]
            i += 1  # Increment i to skip the inserted 'X'
        i += 2
    
    # Decrypt pairs of letters
    i = 0
    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]
        
        # Handle characters not found in the grid
        if char1 not in positions or char2 not in positions:
            plaintext += 'X'  # Placeholder for unknown characters
            i += 1
            continue
        
        row1, col1 = positions[char1]
        row2, col2 = positions[char2]
        
        # Decrypt characters based on their positions in the grid
        if row1 == row2:  # Same row
            plaintext += grid[row1][(col1 - 1) % 5]
            plaintext += grid[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column
            plaintext += grid[(row1 - 1) % 5][col1]
            plaintext += grid[(row2 - 1) % 5][col2]
        else:  # Rectangle
            plaintext += grid[row1][col2]
            plaintext += grid[row2][col1]
        
        i += 2
    
    return ''.join(plaintext).replace('X', '')

def main():

    #define encrypted msg:
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    # Define key
    key = "SUPERSPY"

    # Decrypt Playfair ciphertext
    decrypted_message = decrypt_playfair(encrypted_message, key)
    print(decrypted_message)

# Execute main function if script is run directly
if __name__ == "__main__":
    main()