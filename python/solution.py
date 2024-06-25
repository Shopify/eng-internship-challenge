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

        if repeated == True:
            if i == len(keyword) - 1: #if we are analyzing the last index, remove the last index
                keyword = keyword[:i] + " "

            else:
                keyword = keyword[:i] + " " + keyword[i+1:]

    keyword = keyword.replace(" ", "") #we now have the keyword with no repeated letters

    print(keyword)


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


    print(square)


#function for returning the decoded text
            
            
#def return_text():
keyword = "SUPERSPY"
create_square(keyword)



