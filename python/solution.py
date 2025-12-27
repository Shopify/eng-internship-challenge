############## LOGIC ##############

#using SUPERSPY as the key, the table becomes:
# S U P E R
# Y A B C D
# F G H I K
# L M N O Q
# T V W X Z

#we want to decrpyt the given message "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
#to decrypt, we would perform the opposite of operations used to encrypt via Playfair Cipher
#Case 1: if a pair forms a rectangle, we take the opposite corners
#Case 2: if a pair is in a column, we replace it with the above letters
#Case 3: if a pair is in a row, we replace it with the left letters

#IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV
#HI PX PO PO TO MO NS TR OS ES QU IP PE DA LI OP HO BI AX

#If we omit spaces and "X" we get the decrypted string HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA

############## CODE ##############

def formatMsg(text):
    #remove spaces, and any non-alphabetical special characters
    text = "".join(text.split())
    for char in text:
        if char.isalpha() == False:
            char = ""
    return text

def gen_table(key):
    key = formatMsg(key)
    #format key further by removingduplicates and interchanging "J" with "I".
    temp = ""
    for char in key:
        if char not in temp:
            temp += char
    key = temp
    key = key.replace("J","I").upper()

    #initialize alphabet list excluding "J"
    alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    table = []
    pred_letter = set()
    #add unique letters in key to table
    #letters are not repeated by checking predecessor set first
    for char in key:
        if char not in pred_letter:
            table.append(char)
            pred_letter.add(char)
    #fill rest of table with unique letters from the alphabet
    for char in alpha:
        if char not in pred_letter:
            table.append(char)
            pred_letter.add(char)
    #return list with sublists as rows to simulate a 5x5 key table
    return [table[i:i+5] for i in range(0,25,5)]

def findChar(table, char):
    #determine position of character in the table in terms of row and column
    list = [0,0]
    for i in range(5):
        for j in range(5):
            if table[i][j] == char:
                list[0], list[1] = i,j
    return list

def decryptCipher(encryptedMsg, key):
    sol = ""
    table = gen_table(key)

    #split encrypted message into pairs
    pairs = [encryptedMsg[i:i+2] for i in range(0, len(encryptedMsg), 2)]

    #find the position of the first and second letter of each pair in terms of row and column
    for i in range(0, len(encryptedMsg)//2):
        row1, col1 = findChar(table, pairs[i][0])
        row2, col2 = findChar(table, pairs[i][1])

        #if both letters are in the same column, we follow case 2 (see logic section)
        if col1 == col2:
            sol += table[(row1 - 1) % 5][col1]
            sol += table[(row2 - 1) % 5][col2]
        #if both letters are in the same row, we follow case 3
        elif row1 == row2:
            sol += table[row1][(col1 - 1) % 5]
            sol += table[row2][(col2 - 1) % 5]
        #if row and column differ, we create a rectangle and follow case 1
        else:
            sol += table[row1][col2]
            sol += table[row2][col1]
    #format by making uppercase, removing spaces, special characters, and "X"
    sol = formatMsg(sol)
    sol = sol.replace("X","")
    sol = sol.upper()
    return sol


def main():
    key = "SUPERSPY"
    encryptedMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    decryptedMsg = decryptCipher(encryptedMsg, key)
    print(decryptedMsg)

if __name__ == '__main__':
    main()
