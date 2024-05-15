
import numpy as np
def generate_key(key):
      # make a 2d array
        letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_list=[]
        
        # edge case : double letters 
        i=0
        while i < len(key):
            if key[i] not in key_list:
                key_list.append(key[i])
            if i > 0  and key[i-1] == key[i] : 
                 key_list.append("X")
            i +=1

        for l in letters:
            if l not in key_list:
                 key_list.append(l)

        # convert that into a 5*5 matrix
        key_array = np.array(key_list)
        key_matrix = key_array.reshape(-1,5)
        return key_matrix
                  
def find_row_col(letter, key_matrix):
     for i, row_value in enumerate(key_matrix):
          for j, col_value in enumerate(row_value):
               if col_value == letter:
                    return i ,j
    
def decipher_text(text, key_matrix):
    if len(text) == 1:
         return text

    first_letter = text[0]
    second_letter = text[1]

    # find row and columns of first and second letter
    first_letter_row, first_letter_col = find_row_col(first_letter, key_matrix)
    second_letter_row, second_letter_col = find_row_col(second_letter, key_matrix) 
    decrypted_first_letter=""
    decipher_second_letter=""
    # if same row
    if first_letter_row == second_letter_row:
         decrypted_first_letter += key_matrix[first_letter_row][(first_letter_col - 1 )% 5 ]
         decipher_second_letter += key_matrix[first_letter_row][(second_letter_col - 1) % 5]
    # if same column
    elif first_letter_col == second_letter_col:
         decrypted_first_letter += key_matrix[(first_letter_row - 1) % 5][first_letter_col]
         decipher_second_letter+=key_matrix[(second_letter_row - 1) % 5][second_letter_col]
    #for rect and squares
    else:
         decrypted_first_letter+=key_matrix[first_letter_row][second_letter_col]
         decipher_second_letter+=key_matrix[second_letter_row][first_letter_col]

    if decrypted_first_letter =="X":
         return decipher_second_letter
    if decipher_second_letter == "X" :
         return decrypted_first_letter
    return decrypted_first_letter + decipher_second_letter


def main():
        encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
        encryptedMessage_array = []        
        # edge case : double letters 
        i=0
        while i < len(encryptedMessage):
            if encryptedMessage[i] != " " and encryptedMessage[i].isalnum() == True: # for edge cases
                encryptedMessage_array.append(encryptedMessage[i])         
            i +=1
             
        key = "SUPERSPY"
        key_matrix = generate_key(key)
        # got the key matrix at this point
        # now divide the msg into chunks of 2 and decipher each chunk
        decryptedMessage=""
        j=0
        while j+1 < len(encryptedMessage_array):
             first_letter = encryptedMessage_array[j]
             second_letter = encryptedMessage_array[j+1]
             text = first_letter+second_letter
             decryptedMessage += decipher_text(text, key_matrix)
             j+=2
           
        print(decryptedMessage)
        return decryptedMessage

if __name__ == '__main__':
    main()

    #generate key should be :  S U P E R
    #                          Y A B C D
    #                          F G H I K 
    #                          L M N O Q 
    #                          T V W X Z 
