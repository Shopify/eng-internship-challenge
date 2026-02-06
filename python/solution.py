import string


def create_key_table(keyword):
    """
    Creates a 5x5 key table based on the given keyword.
    """
    keyword = keyword.upper()

    # Initialize 1D key table
    key_table_list = []

    # Add to key table in order ensuring no duplicates
    for letter in keyword:
        if letter not in key_table_list:
            key_table_list.append(letter)

    # Add to key table letters from A-Z ensuring not already added
    for letter in string.ascii_uppercase:
        if letter not in key_table_list and letter != 'J':
            key_table_list.append(letter)

            # Break when table is fully populated
            if len(key_table_list) == 25:
                break

    # Initialize 2D key table
    key_table = [[""] * 5 for _ in range(5)]
    key_table_letter_position = {}

    # Populate 1D key table into 2D and store letter row/columns positions in dictionary
    for position, letter in enumerate(key_table_list):
        row = position // 5
        column = position % 5
        key_table[position // 5][position % 5] = letter
        key_table_letter_position[letter] = (row, column)

    return key_table, key_table_letter_position


def decode_cipher(cipher, key_table, key_table_letter_position):
    """
    Decodes a given cipher using the provided key table.
    """
    cipher = cipher.upper()

    # Initize list to add decoded bigrams
    message_list = []

    # Iterate through cipher bigrams
    for i in range(0, len(cipher), 2):
        bigram = cipher[i:i+2]

        # Get first letter in bigram and row/column position on key table
        first_letter = bigram[0]
        first_letter_position = key_table_letter_position[first_letter]
        first_letter_row = first_letter_position[0]
        first_letter_column = first_letter_position[1]

        # Get second letter in bigram and row/column position on key table
        second_letter = bigram[1]
        second_letter_position = key_table_letter_position[second_letter]
        second_letter_row = second_letter_position[0]
        second_letter_column = second_letter_position[1]

        # Check if same row
        if first_letter_row == second_letter_row:
            # Get letters to the left of positions
            decoded_first = key_table[first_letter_row][(
                first_letter_column-1) % 5]
            decoded_second = key_table[second_letter_row][(
                second_letter_column-1) % 5]

        # Check if same column
        elif first_letter_column == second_letter_column:
            # Get letters above positions
            decoded_first = key_table[(first_letter_row-1) %
                                      5][first_letter_column]
            decoded_second = key_table[(
                second_letter_row-1) % 5][second_letter_column]

        else:
            # get letter by row from current letter and column from opposing letter
            decoded_first = key_table[first_letter_row][second_letter_column]
            decoded_second = key_table[second_letter_row][first_letter_column]

        # Join both decoded letters
        decoded_bigram = (decoded_first + decoded_second)
        decoded_bigram = decoded_bigram.replace("X", "")  # Remove 'X'

        message_list.append(decoded_bigram)

    message = "".join(message_list)

    return message


if __name__ == "__main__":
    keyword = "SUPERSPY"
    cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    key_table, key_table_letter_position = create_key_table(keyword)
    decoded_message = decode_cipher(cipher,
                                    key_table, key_table_letter_position)

    print(decoded_message)
