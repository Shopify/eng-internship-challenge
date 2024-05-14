# This function generates a table based on the keyword
def generate_table(keyword):
    # This code block filters out duplicate characters in the keyword as well as marking characters that were seen during the filtering process.
    filtered_keyword = ""
    seen = set(["J"])
    for char in keyword:
        if char in seen:
            continue
        seen.add(char)
        filtered_keyword += char

    # Table creation block
    table = []
    remaining_chars = "A"
    k = 0
    for _ in range(5):
        table.append([])
        for _ in range(5):
            # Use the characters from the keyword if they aren't already used
            if k < len(filtered_keyword):
                table[-1].append(filtered_keyword[k])
                k += 1
                continue
            
            # Iterate from the last discovered character until you find the next character that hasn't been discovered
            while remaining_chars in seen:
                remaining_chars = chr(ord(remaining_chars) + 1)
            table[-1].append(remaining_chars)
            seen.add(remaining_chars)
            
    return table

def decrypt(cipher, keyword):
    table = generate_table(keyword)
    decipher = ""

    # Creates two maps:
    # 1. Alphabet: (row, column) indices of the alphabet
    # 2. (row, column) indices of the alphabet: Alphabet
    char_to_pos = {table[i][j]: (i, j) for i in range(5) for j in range(5)}
    pos_to_char = {(i, j): table[i][j] for i in range(5) for j in range(5)}
    
    # Inspect the cipher from left to right, 2 characters at a time.
    for i in range(0, len(cipher), 2):

        # Extract the row and column position of the two characters of the pair
        pair = cipher[i:i+2]
        char1_r, char1_c = char_to_pos[pair[0]]
        char2_r, char2_c = char_to_pos[pair[1]]

        # If the two characters are in the same row, shift the column positions to the left by 1
        if char1_r == char2_r:
            decipher += pos_to_char[(char1_r, (char1_c - 1) % 5)] + pos_to_char[(char2_r, (char2_c - 1) % 5)]
            
        # If the two characters are in the same column, shift the row positions upwards by 1
        elif char1_c == char2_c:
            decipher += pos_to_char[((char1_r - 1) % 5, char1_c)] + pos_to_char[((char2_r - 1) % 5, char2_c)]
        
        # If none of the above conditions apply, swap their column positions
        else:
            decipher += pos_to_char[(char1_r, char2_c)] + pos_to_char[(char2_r, char1_c)]
    
    # Remove all "X" in the decipher
    return decipher.replace("X", "")

keyword = "SUPERSPY"
cipher = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
print(decrypt(cipher, keyword))