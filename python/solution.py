# This program solves a Playfair Cipher using matrix-based logic and a hashmap to represent the board.
import numpy as np

message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
key = 'SUPERYABCDFGHIKLMNOQTVWXZ'



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

def board_search(board_map, board_array, letters):
    global output
    char1, char2 = letters
    if column_search(board_map, char1, char2) == True:
        output = output + board_array[(board_map[char1][0] + 1) % 5][board_map[char1][1]] + board_array[(board_map[char2][0] + 1) % 5][board_map[char2][1]]
    elif row_search(board_map, char1, char2) == True:
        output = output + board_array[board_map[char1][0]][(board_map[char1][1] - 1) % 5] + board_array[board_map[char2][0]][(board_map[char2][1] - 1) % 5]
    else:
        output = output + board_array[board_map[char1][0]][board_map[char2][1]] + board_array[board_map[char2][0]][board_map[char1][1]]
    return output

def column_search(board, char1, char2):
    if board[char1][1] == board[char2][1]:
        return True
    else:
        return False

def row_search(board, char1, char2):
    if board[char1][0] == board[char2][0]:
        return True
    else:
        return False
    


split_msg = digraph(message)
board_map = create_map(key)
board_array = create_array(key)

output = ''
for i in range(len(split_msg)):

    board_search(board_map, board_array, split_msg[i])

output = output.replace('X', '')
print(output)




