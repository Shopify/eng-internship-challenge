# Function to create the 5 x 5 matrix with the key in the first n cells where n = length of the key
# followed by the rest of the alphabet
def create_matrix(key):
    matrix = [] 
    key = key.replace('J', 'I') # Replace 'J' with 'I' since they are interchangable
    used_chars = set() # Track used chars to avoid duplicate letters
    # Fill the matrix with characters from the key
    for char in key:
        if char not in used_chars: # account for case where key may be lowercase but readme instructions want everything in uppercase
            matrix.append(char) 
            used_chars.add(char)
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" # Omit J from the alphabet
    for char in alphabet:
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

# function to decrypt each pair thats passed in
def decrypt_pair(pair, matrix):
    one_dimensional_matrix = sum(matrix, []) # Convert 2d array into 1d so we can use .index to calculate the row and col of each num
    first_pos = one_dimensional_matrix.index(pair[0])
    second_pos = one_dimensional_matrix.index(pair[1])
    first_row, first_col = first_pos // 5, first_pos % 5
    second_row, second_col = second_pos // 5, second_pos % 5

    # Same row (Shift left)
    if first_row == second_row:
        first_col = (first_col - 1) % 5
        second_col = (second_col - 1) % 5
    # Same column (Shift up)
    elif first_col == second_col:
        first_row = (first_row - 1) % 5
        second_row = (second_row - 1) % 5
    # Pair forms a rectangle
    else:
        temp = first_col
        first_col = second_col
        second_col = temp
    return matrix[first_row][first_col] + matrix[second_row][second_col]

# Function that decrypts the cipher using the key provided
def decrypt(cipher, key):
    # Remove spaces and lowercase for both key and cipher
    key = key.upper().replace(' ', '')
    cipher = cipher.upper().replace(' ', '') 
    matrix = create_matrix(key)
    decrypted_text = ""

    i = 0
    while i < len(cipher) - 1:
        # iteratively decrypt each pair
        decrypted_text += decrypt_pair(cipher[i:i+2], matrix)
        i += 2

    return decrypted_text.replace('X', '') # Decrypted text cannot include 'X'

def main():
    cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    print(decrypt(cipher, key))

if __name__ == '__main__':
    main()