# This program solves a Playfair Cipher using matrix-based logic and a hashmap to represent the board.
import numpy as np

# Creates a 2D array where each letter is at its coordinate [i, j] so we can search for letters from an index in O(1) time.
# Could have made a two-way hashmap, but an array is more memory-efficient.
def create_array(letters):
    board_array = np.array(list(letters)).reshape(5, 5)
    return board_array

# Creating a hashmap that represents the board where each letter is mapped to its coordinate [i, j].
# This allows for us to search for a letter's index in O(1) time.
def create_map(letters):
    board_map = {}
    for i, char in enumerate(letters):
        row = i // 5
        col = i % 5
        board_map[char] = (row, col)
    return (board_map)

# Method that receives an encrypted message and splits it into two-letter pairs.
def digraph(encrypted_msg):
    return [encrypted_msg[i:i+2] for i in range(0, len(encrypted_msg), 2)]

# Method that searches for the two letters in the board and returns the decrypted pair. Calls column_search and row_search.
def board_search(board_map, board_array, letters):
    global output
    char1, char2 = letters
    
    row1, col1 = board_map[char1]
    row2, col2 = board_map[char2]
    
    # Works by checking if the two letters are in the same row or column and then adding the correct corresponding letters to the output string.
    # This is done by calling the decrypted letter from the board array using indices from the board hashmap.
    if column_search(board_map, char1, char2):
        return (
            board_array[(row1 + 1) % 5][col1] +
            board_array[(row2 + 1) % 5][col2])
    elif row_search(board_map, char1, char2):
        return (
            board_array[row1][(col1 - 1) % 5] +
            board_array[row2][(col2 - 1) % 5]
        )
    else:
        return (
            board_array[row1][col2] +
            board_array[row2][col1]
        )

# Method that checks if two letters are in the same column and returns True if they are.
def column_search(board, char1, char2):
    if board[char1][1] == board[char2][1]:
        return True
    else:
        return False

# Method that checks if two letters are in the same row and returns True if they are.
def row_search(board, char1, char2):
    if board[char1][0] == board[char2][0]:
        return True
    else:
        return False
    

if __name__ == '__main__':
    # The message and key for the Playfair Cipher. 'key' refers to the 25-letter matrix order after including the key at the beginning.
    message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    key = 'SUPERYABCDFGHIKLMNOQTVWXZ'

    # Splitting the message into two-letter pairs.
    split_msg = digraph(message)

    # Creating the associated board map and array.
    board_map = create_map(key)
    board_array = create_array(key)

    # Initializing the output string to a blank string
    output = ''

    # Iterating through the split message and decrypting each pair, then appending it to the 'output' string.
    for i in range(len(split_msg)):
        output += board_search(board_map, board_array, split_msg[i])

    # Removing any 'X' characters from the output string.
    output = output.replace('X', '')

    # Printing the output string.
    print(output)



