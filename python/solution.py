def create_matrix_and_position_map(key):
    """Creates a 5x5 matrix from the keyword and maps each letter's position."""
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    position_map = {}
    seen = set()

    # Fill matrix with unique letters from the keyword
    for char in key:
        if char not in seen and char in alphabet:
            matrix.append(char)
            seen.add(char)

    # Add remaining letters of the alphabet
    for char in alphabet:
        if char not in seen:
            matrix.append(char)

    # Generate 5x5 matrix and map positions
    for index, char in enumerate(matrix):
        row, col = divmod(index, 5)
        position_map[char] = (row, col)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)], position_map

def decrypt_pair(pair, matrix, position_map):
    """Decrypts a pair of letters using the Playfair cipher rules."""
    row1, col1 = position_map[pair[0]]
    row2, col2 = position_map[pair[1]]

    # Apply decryption rules based on the letters' positions
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_message(message, key):
    """Decrypts an entire message encrypted with the Playfair cipher."""
    if len(message) % 2 != 0:
        raise ValueError("Encrypted message must be in even length digraphs.")

    matrix, position_map = create_matrix_and_position_map(key)
    decrypted = []

    # Process each digraph
    for i in range(0, len(message), 2):
        decrypted.append(decrypt_pair(message[i:i+2], matrix, position_map))
    
    # Join all decrypted pairs and remove non-alphabet characters
    return ''.join(decrypted).replace('X', '')

# Main execution
if __name__ == "__main__":
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    try:
        decrypted_message = decrypt_message(encrypted_message, key)
        print(decrypted_message)
    except ValueError as e:
        print(f"Error: {str(e)}")
