def remove_duplicates_from_keyword(keyword):
    keyword_dict = {}

    # preprocess keyword
    keyword = keyword.replace(" ", '').upper()

    for chr in keyword:
        if chr not in keyword_dict:
            keyword_dict[chr] = None
        else:
            continue
    
    sanitized_word = ""
    for key in keyword_dict.keys():
        sanitized_word += key
    
    return sanitized_word
            
def create_table(keyword):
    # alphabet letters without the letter "J"
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

    for char in keyword:
        if char in alphabet:
            alphabet = alphabet.replace(char, '')

    rows, cols = (5, 5)
    
    # Create an empty table with 2D array 
    table = [[None for _ in range(cols)] for _ in range(rows)]
    
    key_index = 0  
    for i in range(rows):
        for j in range(cols):
            if key_index < len(keyword):
                table[i][j] = keyword[key_index]
                key_index += 1
            else:
                table[i][j] = alphabet[key_index - len(keyword)]
                key_index += 1
                
    return table

def get_position(char, table): 
    for i, row in enumerate(table):
        for j, value in enumerate(row):
            if  value == char:
                return (i, j)
            
def decrypt_playfair_cipher(message, table):
    decrypted_message = ""
    
    # preprocess encrypted message
    message = message.replace(" ", '').upper()
    
    for i in range(0, len(message), 2):
        pair = message[i: i+2]
        
        pos1 = get_position(pair[0], table)
        pos2 = get_position(pair[1], table)
        
        if pos1[0] == pos2[0]:
            decrypted_message += table[pos1[0]][(pos1[1] - 1) % 5]
            decrypted_message += table[pos2[0]][(pos2[1] - 1) % 5]
        elif pos1[1] == pos2[1]:
            decrypted_message += table[(pos1[0] - 1) % 5][pos1[1]]
            decrypted_message += table[(pos2[0] - 1) % 5][pos2[1]]
        else:
            decrypted_message += table[pos1[0]][pos2[1]]
            decrypted_message += table[pos2[0]][pos1[1]]
             
    decrypted_message = decrypted_message.upper()
    decrypted_message = decrypted_message.replace("X", "")
    decrypted_message = "".join(e for e in decrypted_message if e.isalnum())
            
    return decrypted_message


def main():
    keyword = 'SUPERSPY'
    message = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV'
    
    sanitized_word = remove_duplicates_from_keyword(keyword)
    table = create_table(sanitized_word)
    
    output = decrypt_playfair_cipher(message, table)
    print(output)

if __name__ == '__main__':
    main()