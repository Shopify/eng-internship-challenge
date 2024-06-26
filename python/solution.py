#creates the 5x5 square with the given keyword
def create_square(keyword):
    #this will be the 5x5 square of letters
    square = ["-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-"]

    #first get rid of repeated letters in keyword
    repeated = False

    for i in range(len(keyword)):
        repeated = False
        
        for j in range(i): #index through all values before currently analyzed value to check for duplicates
            if i>0 and keyword[j] == keyword[i] and keyword[j] != " ": # if the value being analyzed has appeared previously in string, eliminate the currently anaylzed value
                repeated = True

        if repeated == True: #remove repeated value from string
            if i == len(keyword) - 1: #if we are analyzing the last index, remove the last index
                keyword = keyword[:i] + " "

            else:
                keyword = keyword[:i] + " " + keyword[i+1:]

    keyword = keyword.replace(" ", "") #we now have the keyword with no repeated letters

    #print(keyword)

    #create the 5x5 square by going through keyword then through all values of alphabet
    alphabet_value = 65 #starting at A, which is ascii value 65

    for i in range(25):
        if i <= len(keyword)-1: #insert values of keyword first
            square[i] = keyword[i]
        else: #insert values of rest of alphabet next
            while (chr(alphabet_value) in keyword) or alphabet_value == 74: #skip over any letters that are already in the keyword and skip J (ascii value 74)
                alphabet_value += 1 
            
            square[i] = chr(alphabet_value)
            alphabet_value += 1


    #print(square)

    return square



#function for returning the decoded text, takes in the 5x5 square as input
def decode(square, message):  

    decoded_message = "" 

    for i in range(int(len(message))):
        if i % 2 == 0:
            #compare two values at a time, each the next two values in message string
            val1 = message[i]
            val2 = message[i+1]

            #record the index where val1 exists in the square
            val1_index = square.index(val1) 
            val2_index = square.index(val2)


            #check if values are in the same column
            if ( (val1_index - val2_index ) % 5 == 0 ):
                #print(val1 + val2 + "column!")

                #each letter in the square goes up a row; if at the top row, loop back down to botton
                if val1_index < 5 :
                    decoded_message += square[val1_index + 20] + square[val2_index - 5]
                elif val2_index < 5:
                    decoded_message += square[val1_index - 5] + square[val2_index + 20]
                else:
                    decoded_message += square[val1_index - 5] + square[val2_index - 5]


            #check if they are in the same row
            elif int(val1_index / 5) == int(val2_index / 5 ):
                #print(val1 + val2 + "row!")

                #each letter in the square goes to the left column; if at the leftmost column, loop back to rightmost column
                if val1_index % 5 == 0:
                    decoded_message += square[val1_index + 4] + square[val2_index - 1]
                elif val2_index % 5 == 0:
                    decoded_message += square[val1_index - 1] + square[val2_index + 4]
                else:
                    decoded_message += square[val1_index - 1] + square[val2_index - 1]

            #check for rectangle
            else:
                #print(val1 + val2 + "rectangle!")

                #find the other corners of the rectangle:

                corner_check_val1 = 5 * int(val1_index / 5) #we start at the very left index of the val1's row
                corner_check_val2 = 5 * int(val2_index / 5) #we start at the very left index of the val2's row

                for i in range(5):
                    if((corner_check_val1 - val2_index) % 5  != 0): #keep going through val1's row until we get to the same column as val2, this will be a corner
                        corner_check_val1 += 1

                    if((corner_check_val2 - val1_index) % 5  != 0): #keep going through val2's row until we get to the same column as val1, this will be a corner
                        corner_check_val2 += 1
                
                decoded_message += square[corner_check_val1] + square[corner_check_val2]
    
    decoded_message = decoded_message.replace("X", "") #remove any X's from decoded message
    print(decoded_message)

    return decoded_message

            

def main():
    keyword = "SUPERSPY"
    message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    #create_square(keyword)
    decoded_message = decode(create_square(keyword), message)


if __name__ == '__main__':
    main()

