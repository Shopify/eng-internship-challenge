cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
# Construct the 5x5 grid
letter_positions = {}


def build_decryption_grid():
    decryption_grid = [[0 for _ in range(5)] for _ in range(5)]

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
    # determine which letter to cut out of remaining letters
    for c in cipher_text:
        if c == "I":
            remaining_letters.remove("J")
            break
        elif c == "J":
            remaining_letters.remove("I")
            break

    key_index = 0
    for i in range(5):
        for j in range(5):
            # print(decryption_grid)
            # print(i, j, key_index)
            # if there are still characters remaining in key, then add them first
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

            # otherwise, add from remaining letters:
            next_letter = remaining_letters.pop(0)
            decryption_grid[i][j] = next_letter
            letter_positions[next_letter] = [i, j]

    print(decryption_grid)
    print(letter_positions)


build_decryption_grid()
# def solve_message():
#     index_1, index_2 = 0, 0
#     while index_2 < len(cipher_text):
#         # get new characters
#         char_1 = cipher_text[index_1]
#         char_2 = cipher_text[index_2]

#         # determine which 3 cases

#         # same row, get letters to the left
#         if letter_positions[char_1][0] == letter_positions[char_2][0]:
#             # determine if wrap-around needed
#             asdf

#         # same column, get letters above
#         elif letter_positions[char_1][1] == letter_positions[char_2][1]:
#             # determine if wrap-around needed
#             asdf

#         # diff row or column, need to get rectangle
#         else:
#             asdf

#         index_1 += 1
#         index_2 += 1
