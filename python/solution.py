import string

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
cipher_key="SUPERSPY"

 #creates the table
def generate_table(cipher_key, alphabet):
    cipher_key = cipher_key.upper()
    table =[]
    #add all the cipher key characters to the table
    for char in cipher_key:
        #if the unadded character is 'I' add it to the table
        if char not in table:
            if char == 'I':
                table.append(char)
                continue
        #skip if the character is 'J' because I will get added anyway
            if char == 'J':
                continue
               
            table.append(char)
            
    #add all the characters in the alphabet(not already present in the table) to the table
    for char in alphabet:
        if char not in table:
            if char == 'I':
                table.append(char)
                continue
            if char == 'J':
                continue
            table.append(char)
    
    table_2d =[table[i:i+5] for i in range(0, len(table), 5)]
    # print(table_2d)
    return table_2d
        
#searches for the (x,y) coordinates of a character in the table in terms of rows and colummns
def find_char_in_table(table, char):
    row = col =0
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] == char:
                row =i
                col =j
    return row, col
    

#decrupts the encrypted text
def decrypt(encrypted_text, cipher_key):
    cipher_key = cipher_key.upper().replace(" ", "")
    
    table = generate_table(cipher_key, alphabet)
    
    decrypted_text = ""
    
    
    for i in range(0, len(encrypted_text),2):
        #sets the characters in a digraph
        char1 = encrypted_text[i]
        char2 = encrypted_text[i+1]
        
        #sets coordinates of the characters in the table
        row1, col1 = find_char_in_table(table, char1)
        row2, col2 = find_char_in_table(table, char2)
        
        #decryption process
        #same row
        if row1 == row2:
            decrypted_text += table[row1][(col1-1)%5] + table[row2][(col2-1)%5]
        #same column
        elif col1 == col2:
            decrypted_text += table[(row1-1)%5][col1] + table[(row2-1)%5][col2]
        else:
            decrypted_text += table[row1][col2] + table[row2][col1]
            
    #remove the 'X' characters from the decrypted text
    decrypted_text = decrypted_text.replace("X", "")
    print(decrypted_text)
    return decrypted_text


#begins the program
def main():
    return decrypt(encrypted_text, cipher_key)
   

#entry point for the program
if __name__ == "__main__":
    main()