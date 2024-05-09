
def solution(key,encrypted_message):
    """ 
    This solution involves manipulating the alphabet and dcrypting the message using 
    the playfair cipher system. 
    Create a 5x5 Grid and exclude J as it does not appear in the Encrypted Message.
    Divide the encrypted message into pairs.
    """

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    altered_key=""

    #Remove duplicates from the key
    for i in range(0,len(key)):
        if (key[i] not in key[:i]):
            altered_key=altered_key+key[i]

    for i in range(0,len(altered_key)):
        if(altered_key[i]in alphabet):
            alphabet = alphabet.replace(altered_key[i],"")


    combined = altered_key+alphabet
    print(combined)
    grid=[[],[],[],[],[]]
    row_pointer=0
    column_pointer=0
    counter=0
    row=[]
    while (counter<len(combined)):
        if(counter>=1 and row_pointer%5==0):
            row_pointer=0
            column_pointer+=1
        print(column_pointer)
        grid[column_pointer].append(combined[counter])
        row_pointer+=1
        counter+=1


    print(altered_key)
    encypted_pairs = []
    for i in range(0,len(encrypted_message),2):
        encypted_pairs.append((encrypted_message[i:i+2]))
    
    print(encypted_pairs)
    print(grid)

    first_char=""
    second_char=""
    final_string=""
    row1=0
    col1=0
    row2=0
    col2=0
    for i in range(0,len(encypted_pairs)):
        print(encypted_pairs[i])

        for row_index in range(0,5):
            for col_index in range(0,5):
                if(grid[row_index][col_index]==encypted_pairs[i][0]):
                    row1=row_index
                    col1=col_index

                if(grid[row_index][col_index]==encypted_pairs[i][1]):
                    row2=row_index
                    col2=col_index
                
        # first_char=encypted_pairs[i][0]
        # second_char=encypted_pairs[i][1]
        # row1,col1 = divmod(grid.index(first_char),5)
        # row2,col2 = divmod(grid.index(second_char),5)
        #print(row1,col1)


        if(row1 == row2):
            if(row1<4):
                final_string = final_string+str(grid[row1+1][col1])
            else:
                final_string=final_string+str(grid[0][col1])
            if(row2<4):
                final_string = final_string+str(grid[row2+1][col1])
            else:
                final_string=final_string+str(grid[0][col1])

        

        if(col1 == col2):
            if(col1<4):
                final_string = final_string+str(grid[row1+1][col1+1])
            else:
                final_string=final_string+str(grid[row1][0])
            if(col2<4):
                final_string = final_string+str(grid[row2][col2+1])
            else:
                final_string=final_string+str(grid[row1][0])

        if(row1 != row2 and col1 != col2):

            final_string=final_string+str(grid[row1][col2])
            final_string=final_string+str(grid[row2][col1])

    # for i in range(0,len(final_string)):
    #     if (final_string[i]=="X"):
    final_string=final_string.replace("X","")
    print(final_string)
    



        







if __name__ == "__main__":
    solution("SUPERSPY","IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")