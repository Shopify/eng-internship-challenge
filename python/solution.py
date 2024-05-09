import sys

def generate_playfair_grid(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key = key.upper().replace("J", "I")
    key_set = set(key)
    grid = []
    for char in key + alphabet:
        if char not in key_set:
            key_set.add(char)
            grid.append(char)
    return [grid[i:i+5] for i in range(0, len(grid), 5)]

def decrypt_playfair(ciphertext, key):
    grid = generate_playfair_grid(key)
    plaintext = ""
    ciphertext = ciphertext.upper().replace("J", "I")
    
    # Find positions of letters in the grid
    positions = {}
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            positions[grid[i][j]] = (i, j)
    
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
        
        # Same row
        if row1 == row2:
            plaintext += grid[row1][(col1 - 1) % 5]
            plaintext += grid[row2][(col2 - 1) % 5]
        # Same column
        elif col1 == col2:
            plaintext += grid[(row1 - 1) % 5][col1]
            plaintext += grid[(row2 - 1) % 5][col2]
        # Rectangle
        else:
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