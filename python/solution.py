def gen_matrix(key):
    '''
    Generate 5x5 matrix to solve playfair cipher!
    Input: String:key
    Output: 2d matrix
    '''

    key = key.upper().replace("J", "I")
    seen = set()

    # no duplicate chars in key
    uniq = [ch for ch in key if ch not in seen and not seen.add(ch)]
    
    playfair_alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    for ch in playfair_alpha:
        if ch not in seen:
            uniq.append(ch)

    # form matrix of unique chars
    return [ uniq[i:i+5] for i in range(0,25,5) ]


def decrypt(encrypted_text, matrix):
    '''
    Decrypts playfair cipher!
    Input:
        Str:encrypted_text
        List[][]: 2d matrix
    Output:
        Str:decrypted_text
    '''
    # store position of chars of matrix
    ch_pos = {}
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            ch_pos[char] = (i, j)
    
    # convert encrypted_text -> char pairs
    pairs = [encrypted_text[i:i+2] for i in range(0, len(encrypted_text), 2)]
    
    # decrypt
    decrypted_text = ""
    for pair in pairs:
        row1, col1 = ch_pos[pair[0]]
        row2, col2 = ch_pos[pair[1]]
        
        if row1 == row2: 
            new_1 = matrix[row1][(col1 - 1) % 5]
            new_2 = matrix[row2][(col2 - 1) % 5]
        elif col1 == col2: 
            new_1 = matrix[(row1 - 1) % 5][col1]
            new_2 = matrix[(row2 - 1) % 5][col2]
        else: 
            new_1 = matrix[row1][col2]
            new_2 = matrix[row2][col1]

        decrypted_text += new_1 + new_2

    decrypted_text = decrypted_text.replace("X", "")

    return decrypted_text


if __name__ == '__main__':
    key = "SUPERSPY"
    encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

    matrix = gen_matrix(key)
    decrypted_text = decrypt(encrypted_text, matrix)
    
    print(decrypted_text)