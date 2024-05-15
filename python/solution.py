#!/usr/bin/env python3

def generate_matrix(key):
    """
    generate a 5x5 matrix using the argument key, the key should not contain duplicates and the letter J is replaced with I
    """

    #convert the string to upper characters, then replace 'J' with 'I'
    key="".join(dict.fromkeys(key.replace("J", "I").upper()))

    #defining the alphabet, excluding the letter 'J'
    alphabet= "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    #initializing the key matrix with characters from the key that are not in the alphabet
    key_matrix= [c for c in key if c in alphabet]

    #filling in the remaining spaces in the matrix with the rest of the alphabet
    for letter in alphabet:
        if letter not in key_matrix:
            key_matrix.append(letter)

    #converting the list into a 5x5 matrix
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(char, key_matrix):
    """
    find the position of the argument: char in the argument: key_matrix
    """

    #iterating throught the matrix to find the character's position
    for row in range(5):
        for col in range(5):
            if key_matrix[row][col] == char:
                return row, col
    return None

def decrypt_pair(pair, key_matrix):
    """
    decrypt the pair of characters in the argument: pair,
    using the matrix in the argument: key_matrix, using the playfair cipher rules
    """

    #finding the positions of both characters in the matrix
    row1, col1 = find_position(pair[0], key_matrix)
    row2, col2 = find_position(pair[1], key_matrix)

    #if either of the characters are not found in the matrix, print an error message.
    if row1 is None or row2 is None:
        raise ValueError(f"Character not found in key matrix: {pair}")

    #if characters are in the same row, shift left
    if row1 == row2:
        return key_matrix[row1][(col1 - 1) % 5] + key_matrix[row2][(col2 - 1) % 5]

    #if characters are in the same column, shift up
    elif col1 == col2:
        return key_matrix[(row1 - 1) % 5][col1] + key_matrix[(row2 - 1) % 5][col2]

    #if characters form a rectangle, swap columns
    else:
        return key_matrix[row1][col2] + key_matrix[row2][col1]

def decrypt_message(encrypted_message, key_matrix):
    """
    decrypt a message in the argument: encrypted_message encrypted with the playfair cipher rules
    using the matrix in the argument: key_matrix
    """

    #remove spaces from the message if there is any
    encrypted_message = encrypted_message.replace(" ", "")
    decrypted_message = ""

    #process the message in pairs using the decrypt_pair function
    for i in range(0, len(encrypted_message), 2):
        pair = encrypted_message[i:i + 2]
        decrypted_message += decrypt_pair(pair, key_matrix)
    return decrypted_message

def main():
    """
    main function to decrypte a message using the playfair cipher rules
    """
    key = "SUPERSPY"
    encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key_matrix = generate_matrix(key)
    decrypted_message = decrypt_message(encrypted_message, key_matrix)
    decrypted_message = decrypted_message.replace("X", "")
    print(decrypted_message)

if __name__ == "__main__":
    main()
