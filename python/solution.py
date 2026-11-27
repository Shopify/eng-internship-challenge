# Rhys Martin
# GitHub : ItsRhysNotRhys
# June 27th 2024

text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
decrypted = ""
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
key = "SUPERSPY"
cipher = [[0 for x in range(5)] for y in range(5)]

def main():
    build_array()
    decrypt()
    remove_Xs()
    print(decrypted)


def build_array():
    global key, alphabet, cipher
    for row in range(len(cipher)):
        for col in range(len(cipher[0])):
            if key != "":
                #Use letters from key and remove letters from alphabet array
                letter = key[0]
                cipher[row][col] = letter
                alphabet = alphabet.replace(letter, '')
                key = key.replace(letter, '')
            else:
                #Use letters in the alphabet that haven't been used yet
                cipher[row][col] = alphabet[0]
                alphabet = alphabet[1:]

def decrypt():
    global text, decrypted, cipher
    #Pad text with an 'x' if it's not an even number of letters
    if len(text) % 2 != 0:
        text += 'X'

    while text != "":
        #Start breaking the text into it's pairs of two letters
        pair = text[:2]
        letter1 = pair[0]
        letter2 = pair[1]
        text = text[2:]

        #Find the row and column of each letter to use to decide what swap we are doing
        row1, col1 = find_row_col(letter1)
        row2, col2 = find_row_col(letter2)

        if row1 == row2:
            #Shift letters left 1
            search_col = 0

            search_col = one_less(col1)
            letter1 = cipher[row1][search_col]
            search_col = one_less(col2)
            letter2 = cipher[row2][search_col]
            
        elif col1 == col2:
            #Shift letters up 1
            search_row = 0

            search_row = one_less(row1)
            letter1 = cipher[search_row][col1]
            search_row = one_less(row2)
            letter2 = cipher[search_row][col2]
            
        else:
            #Find letter of the other letters column but remain in own row
            letter1 = cipher[row1][col2]
            letter2 = cipher[row2][col1]
        
        decrypted += letter1
        decrypted += letter2

def one_less(num):
    if num == 0 :
        return 4
    else:
        return num - 1

def find_row_col(letter):
    for row in range(len(cipher)):
        for col in range(len(cipher[0])):
            cur = cipher[row][col]
            if cur == letter:
                return row, col
    return -1, -1

def remove_Xs():
    global decrypted

    decrypted = decrypted.replace("X", "")

if __name__ == "__main__":
    main()

