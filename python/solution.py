# A program to solve a playfair cipher.

cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
secret = []

# a dictionary for positions of letters in the grid, for faster searching
letter_positions = {}

# a 5x5 grid to be used to decrypt the cipher
decryption_grid = [[0 for _ in range(5)] for _ in range(5)]


# function to construct the grid
def build_decryption_grid():

    remaining_letters = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    # determine which letter to cut out of remaining letters, I or J
    for c in cipher_text:
        if c == "I":
            remaining_letters.remove("J")
            break
        elif c == "J":
            remaining_letters.remove("I")
            break

    # main loop to populate grid
    key_index = 0
    for i in range(5):
        for j in range(5):

            # if there are still characters in the key that haven't been
            # added to the grid, then add them first
            if key_index < len(key):

                # find next available letter:
                while key_index < len(key) and key[key_index] not in remaining_letters:
                    key_index += 1

                if key_index < len(key):
                    decryption_grid[i][j] = key[key_index]
                    letter_positions[key[key_index]] = [i, j]
                    remaining_letters.remove(key[key_index])
                    key_index += 1
                    continue

            # once the key has been added, add from remaining leftover letters:
            next_letter = remaining_letters.pop(0)
            decryption_grid[i][j] = next_letter
            letter_positions[next_letter] = [i, j]


# function to solve the cipher text
def solve_message():
    # helper variables to make code easier to write and debug
    row, column = 0, 1
    c_index_1, c_index_2 = 0, 1

    while c_index_2 < len(cipher_text):
        # get new characters and positions
        c_char_1 = cipher_text[c_index_1]
        c_char_2 = cipher_text[c_index_2]

        c_char_1_position = letter_positions[c_char_1]
        c_char_2_position = letter_positions[c_char_2]

        s_char_1_position = c_char_1_position.copy()
        s_char_2_position = c_char_2_position.copy()

        # case 1: same row, get letters to the left
        if c_char_1_position[row] == c_char_2_position[row]:
            # determine if wrap-around needed by checking if col == 0

            if c_char_1_position[column] == 0:
                s_char_1_position[column] = len(decryption_grid) - 1
            else:
                s_char_1_position[column] = s_char_1_position[column] - 1

            if c_char_2_position[column] == 0:
                s_char_2_position[column] = len(decryption_grid) - 1
            else:
                s_char_2_position[column] = s_char_2_position[column] - 1

        # case 2: same column, get letters above
        elif c_char_1_position[column] == c_char_2_position[column]:
            # determine if wrap-around needed by checking if row == 0
            if c_char_1_position[row] == 0:
                s_char_1_position[row] = len(decryption_grid) - 1
            else:
                s_char_1_position[row] = s_char_1_position[row] - 1

            if c_char_2_position[row] == 0:
                s_char_2_position[row] = len(decryption_grid) - 1
            else:
                s_char_2_position[row] = s_char_2_position[row] - 1

        # case 3: diff row or column, get other end of rectangle by switching columns
        else:
            temp = s_char_1_position[column]
            s_char_1_position[column] = s_char_2_position[column]
            s_char_2_position[column] = temp

        # append new characters in order
        secret.append(
            decryption_grid[s_char_1_position[row]][s_char_1_position[column]]
        )
        secret.append(
            decryption_grid[s_char_2_position[row]][s_char_2_position[column]]
        )

        c_index_1 += 2
        c_index_2 += 2


build_decryption_grid()
solve_message()

# remove X from final result
answer = "".join(secret)
answer_without_x = answer.replace("X", "")

print(answer_without_x)
