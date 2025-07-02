from collections import OrderedDict


def get_playfair_matrix(key):
    # processing key (O(k)), where k is length of key
    key_set = OrderedDict.fromkeys(key)
    key_stripped = "".join(key_set.keys())  # reduce key to unique characters only
    # pp(key_stripped) # sanity check

    # processing alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz".upper()  # use uppercase letters everywhere
    # print(len(alphabet)) # sanity check
    alphabet_set = OrderedDict.fromkeys(alphabet)
    del alphabet_set["J"]  # I and J are same character
    partial = sorted(
        alphabet_set.keys() - key_set.keys()
    )  # get characters that arent in key

    # getting playfair matrix in string form
    playfair = key_stripped + "".join(partial)
    # pp(playfair) # sanity check

    # turning string into matrix
    playfair_sep = " ".join([playfair[i : i + 5] for i in range(0, len(playfair), 5)])
    playfair_sep_split = playfair_sep.split()
    playfair_matrix = [
        list(playfair_sep_split[i]) for i in range(len(playfair_sep_split))
    ]
    # pp(playfair_matrix) # sanity check

    return playfair_matrix


def get_digraphs(text):
    text_sep = " ".join([text[i : i + 2] for i in range(0, len(text), 2)])
    return text_sep.split()


def get_coordinates(char, playfair_matrix):  # takes O(1) since matrix size is fixed
    if not char.isalpha():
        return False
    if char == "J":
        char = "I"
    else:  # loop through the matrix to find the coordinates of a character
        for i in range(len(playfair_matrix)):
            for j in range(len(playfair_matrix[i])):
                if char == playfair_matrix[i][j]:
                    return [i, j]


def encrypt(digraphs, playfair_matrix):
    # digraphs are encoded in a list of two character strings

    encrypted_digraphs = []
    for digraph in digraphs:
        char1 = digraph[0]
        char2 = digraph[1]

        char1_coords = get_coordinates(char1, playfair_matrix)
        char2_coords = get_coordinates(char2, playfair_matrix)

        # print(char1_coords, char2_coords) # sanity check

        encrypted_digraph = []

        if char1_coords[0] == char2_coords[0]:  # same row
            char1_coords_encrypted = [char1_coords[0], (char1_coords[1] + 1) % 5]
            char2_coords_encrypted = [char2_coords[0], (char2_coords[1] + 1) % 5]

            char1_encrypted = playfair_matrix[char1_coords_encrypted[0]][
                char1_coords_encrypted[1]
            ]
            char2_encrypted = playfair_matrix[char2_coords_encrypted[0]][
                char2_coords_encrypted[1]
            ]

            encrypted_digraph.append(char1_encrypted)
            encrypted_digraph.append(char2_encrypted)

        elif char1_coords[1] == char2_coords[1]:  # same column
            char1_coords_encrypted = [(char1_coords[0] + 1) % 5, char1_coords[1]]
            char2_coords_encrypted = [(char2_coords[0] + 1) % 5, char2_coords[1]]

            char1_encrypted = playfair_matrix[char1_coords_encrypted[0]][
                char1_coords_encrypted[1]
            ]
            char2_encrypted = playfair_matrix[char2_coords_encrypted[0]][
                char2_coords_encrypted[1]
            ]

            encrypted_digraph.append(char1_encrypted)
            encrypted_digraph.append(char2_encrypted)

        else:  # different row, different column
            char1_coords_encrypted = [char1_coords[0], char2_coords[1]]
            char2_coords_encrypted = [char2_coords[0], char1_coords[1]]

            char1_encrypted = playfair_matrix[char1_coords_encrypted[0]][
                char1_coords_encrypted[1]
            ]
            char2_encrypted = playfair_matrix[char2_coords_encrypted[0]][
                char2_coords_encrypted[1]
            ]

            encrypted_digraph.append(char1_encrypted)
            encrypted_digraph.append(char2_encrypted)

        encrypted_digraphs.append(encrypted_digraph)

    return [
        "".join(entry) for entry in encrypted_digraphs
    ]  # convert list of lists into list of digraphs


def decrypt(digraphs, playfair_matrix):
    # digraphs are encoded in a list of two character strings

    decrypted_digraphs = []
    for digraph in digraphs:
        char1 = digraph[0]
        char2 = digraph[1]

        char1_coords = get_coordinates(char1, playfair_matrix)
        char2_coords = get_coordinates(char2, playfair_matrix)

        # print(char1_coords, char2_coords) # sanity check

        decrypted_digraph = []

        if char1_coords[0] == char2_coords[0]:  # same row
            char1_coords_decrypted = [
                char1_coords[0],
                (char1_coords[1] - 1) % 5,
            ]  # reverse
            char2_coords_decrypted = [char2_coords[0], (char2_coords[1] - 1) % 5]

            char1_decrypted = playfair_matrix[char1_coords_decrypted[0]][
                char1_coords_decrypted[1]
            ]
            char2_decrypted = playfair_matrix[char2_coords_decrypted[0]][
                char2_coords_decrypted[1]
            ]

            decrypted_digraph.append(char1_decrypted)
            decrypted_digraph.append(char2_decrypted)

        elif char1_coords[1] == char2_coords[1]:  # same column
            char1_coords_decrypted = [
                (char1_coords[0] - 1) % 5,
                char1_coords[1],
            ]  # reverse
            char2_coords_decrypted = [(char2_coords[0] - 1) % 5, char2_coords[1]]

            char1_decrypted = playfair_matrix[char1_coords_decrypted[0]][
                char1_coords_decrypted[1]
            ]
            char2_decrypted = playfair_matrix[char2_coords_decrypted[0]][
                char2_coords_decrypted[1]
            ]

            decrypted_digraph.append(char1_decrypted)
            decrypted_digraph.append(char2_decrypted)

        else:  # different row, different column
            char1_coords_decrypted = [
                char1_coords[0],
                char2_coords[1],
            ]  # inverse of operation is itself
            char2_coords_decrypted = [char2_coords[0], char1_coords[1]]

            char1_decrypted = playfair_matrix[char1_coords_decrypted[0]][
                char1_coords_decrypted[1]
            ]
            char2_decrypted = playfair_matrix[char2_coords_decrypted[0]][
                char2_coords_decrypted[1]
            ]

            decrypted_digraph.append(char1_decrypted)
            decrypted_digraph.append(char2_decrypted)

        decrypted_digraphs.append(decrypted_digraph)

    return [
        "".join(entry) for entry in decrypted_digraphs
    ]  # convert list of lists into list of digraphs


if __name__ == "__main__":
    # input data
    encrypted = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"

    digraphs = get_digraphs(encrypted)
    playfair_matrix = get_playfair_matrix(key)

    # pp(playfair_matrix) # sanity check
    # print(digraphs) # sanity check

    encrypted_digraphs = encrypt(digraphs, playfair_matrix)
    # print(encrypted_digraphs)

    decrypted_digraphs = decrypt(digraphs, playfair_matrix)
    decrypted = "".join(decrypted_digraphs)  # put all the digraphs together
    decrypted = decrypted.translate({ord("X"): None})

    print(decrypted)
