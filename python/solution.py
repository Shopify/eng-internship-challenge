def create_playfair_grid(key):
    # Initialize the grid with the key
    key = key.replace('J', 'I')  # Replace 'J' with 'I'
    key = ''.join(dict.fromkeys(key))  # Remove duplicates
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'  # Playfair grid excludes 'J'
    
    # Create the initial grid with the key
    grid = []
    for char in key:
        if char not in grid:
            grid.append(char)
    
    # Fill the rest of the grid with remaining alphabet letters
    for char in alphabet:
        if char not in grid:
            grid.append(char)
    
    # Reshape into 5x5 grid
    playfair_grid = [grid[i:i+5] for i in range(0, 25, 5)]
    
    return playfair_grid

def find_char_position(char, grid):
    # Find position of character in the grid
    for i in range(5):
        for j in range(5):
            if grid[i][j] == char:
                return (i, j)
    return None

def decrypt_message(message, key):
    playfair_grid = create_playfair_grid(key)
    decrypted_message = []
    
    # Prepare message for decryption (convert to digraphs)
    message = message.replace('J', 'I')  # Replace 'J' with 'I'
    message = message.upper().replace(" ", "")  # Convert to uppercase and remove spaces
    message = [message[i:i+2] for i in range(0, len(message), 2)]
    
    for digraph in message:
        # Get positions of both letters in the digraph
        pos1 = find_char_position(digraph[0], playfair_grid)
        pos2 = find_char_position(digraph[1], playfair_grid)
        
        # Decrypt based on Playfair Cipher rules
        if pos1[0] == pos2[0]:  # Same row
            decrypted_message.append(playfair_grid[pos1[0]][(pos1[1] - 1) % 5] + playfair_grid[pos2[0]][(pos2[1] - 1) % 5])
        elif pos1[1] == pos2[1]:  # Same column
            decrypted_message.append(playfair_grid[(pos1[0] - 1) % 5][pos1[1]] + playfair_grid[(pos2[0] - 1) % 5][pos2[1]])
        else:  # Form rectangle
            decrypted_message.append(playfair_grid[pos1[0]][pos2[1]] + playfair_grid[pos2[0]][pos1[1]])
    
    return ''.join(decrypted_message)

# Encrypted message received
encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
# Key for the Playfair Cipher
key = "SUPERSPY"

# Decrypt the message
decrypted_password = decrypt_message(encrypted_message, key)

print(decrypted_password)
