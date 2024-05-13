def create_matrix(key):
    # Remove duplicate letters, convert to uppercase
    filtered_key = ''.join(sorted(set(key.upper()), key=key.index))
    # Add the remaining letters of the alphabet, excluding 'J'
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    filtered_key += ''.join([char for char in alphabet if char not in filtered_key and char != 'J'])
    # Create the 5x5 matrix
    matrix = [filtered_key[i:i+5] for i in range(0, 25, 5)]
    return matrix

key = "SUPERSPY"
matrix = create_matrix(key)  # Corrected function call
print("Matrix:\n", "\n".join([" ".join(row) for row in matrix]))


