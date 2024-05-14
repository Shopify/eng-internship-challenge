def generate_grid(key):
    # Generate the grid
    grid = [['' for _ in range(5)] for _ in range(5)]
    # Remove duplicates from the key
    key = key.upper()
    key = ''.join(dict.fromkeys(key))
    # Remove 'J' from the key
    key = key.replace('J', '')
    # Add the remaining letters to the key. Letters shouldn't repeat
    for i in range(65, 91):
        if chr(i) not in key and chr(i) != 'J':
            key += chr(i)

    # Fill the grid
    k = 0
    for i in range(5):
        for j in range(5):
            grid[i][j] = key[k]
            k += 1

    return grid

def decrypt(encrypted_message, grid):
    decrypted_message = ''

    # Decrypt the message
    for i in range(0, len(encrypted_message), 2):
        # Get the coordinates of the characters
        char1 = encrypted_message[i]
        char2 = encrypted_message[i + 1]
        row1, col1 = -1, -1
        row2, col2 = -1, -1
        for j in range(5):
            for k in range(5):
                if grid[j][k] == char1:
                    row1, col1 = j, k
                if grid[j][k] == char2:
                    row2, col2 = j, k

        # Decrypt the characters
        if row1 == row2:
            decrypted_message += grid[row1][(col1 - 1) % 5]
            decrypted_message += grid[row2][(col2 - 1) % 5]
        elif col1 == col2:
            decrypted_message += grid[(row1 - 1) % 5][col1]
            decrypted_message += grid[(row2 - 1) % 5][col2]
        else:
            decrypted_message += grid[row1][col2]
            decrypted_message += grid[row2][col1]

    return decrypted_message

if __name__ == '__main__':
    # Read the encrypted message
    encrypted_message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERSPY'

    # Decrypt the message
    grid = generate_grid(key)
    print(grid)
    decrypted_message = decrypt(encrypted_message, grid)
    print(decrypted_message)