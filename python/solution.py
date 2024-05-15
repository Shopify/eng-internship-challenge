cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"
# Construct the 5x5 grid


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
                    remaining_letters.remove(key[key_index])
                    key_index += 1
                    continue

            # otherwise, add from remaining letters:
            decryption_grid[i][j] = remaining_letters.pop(0)
    print(decryption_grid)
