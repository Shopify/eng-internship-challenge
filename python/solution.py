import string

cipher_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
secret_key = "SUPERSPY"

def create_playfair_key_matrix(key):
    # Convert the key to uppercase and remove non-alphabetic characters
    filtered_key = key.upper().replace('J', 'I').replace(' ', '')
    
    # Remove duplicate characters
    unique_characters = {}
    key_without_duplicates = ''
    
    for char in filtered_key:
        if char not in unique_characters:
            unique_characters[char] = True
            key_without_duplicates += char
    
    # Create a list of the alphabet without 'J' and already used characters
    remaining_letters = [chr(i) for i in range(65, 91) if chr(i) not in unique_characters and chr(i) != 'J']
    
    # Combine the characters without duplicates and the remaining letters
    complete_key = key_without_duplicates + ''.join(remaining_letters)
    
    # Form a 5x5 matrix from the complete key
    key_matrix = [list(complete_key[i:i + 5]) for i in range(0, 25, 5)]
    return key_matrix

def decrypt_message_with_playfair(cipher_text, secret_key):
    # Generate the key matrix from the secret key
    key_matrix = create_playfair_key_matrix(secret_key)
    plain_text = ""
    
    # Divide the cipher text into digraphs (pairs of two letters)
    digraphs = [cipher_text[i:i + 2] for i in range(0, len(cipher_text), 2)]
    
    # Decrypt each digraph according to the Playfair rules
    for first_letter, second_letter in digraphs:
        flat_key_matrix = sum(key_matrix, [])
        position1 = flat_key_matrix.index(first_letter)
        position2 = flat_key_matrix.index(second_letter)
        
        row1, column1 = position1 // 5, position1 % 5
        row2, column2 = position2 // 5, position2 % 5
        
        if row1 == row2:  # Letters in the same row
            shifted_column1 = (column1 - 1) % 5
            shifted_column2 = (column2 - 1) % 5
            plain_text += key_matrix[row1][shifted_column1] + key_matrix[row2][shifted_column2]
        elif column1 == column2:  # Letters in the same column
            shifted_row1 = (row1 - 1) % 5
            shifted_row2 = (row2 - 1) % 5
            plain_text += key_matrix[shifted_row1][column1] + key_matrix[shifted_row2][column2]
        else:  # Letters form a rectangle
            plain_text += key_matrix[row1][column2] + key_matrix[row2][column1]
    
    # Remove padding characters (if 'X' was used as a padding character)
    return plain_text.replace('X', '')

#testing


decrypted_text = decrypt_message_with_playfair(cipher_text, secret_key)

print(decrypted_text)
