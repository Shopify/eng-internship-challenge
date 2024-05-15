# Shopify Eng Intership Challenge
# Name: Delin Gu
import string

# generateTable takes the given keyword (and alphabet) and generates an array simulation of the Playfair cipher table and a 
# dict mapping each letter in the table to their respective row and column (for easier searching purposes)
def generateTable(keyword): # this can also just be hardcoded since the keyword is given.
   tableDict = {}
   tableArray = [[], [], [], [], []]
   index = 0
   letters = keyword + string.ascii_uppercase # sequence of letters in order to be added to the cipher table

   for row in range(5):
      for col in range(5):
         while letters[index] in tableDict or letters[index] == "J": # omitting the letter J and making sure only the first instance of each letter is added to array/dict
            index += 1
         tableArray[row].append(letters[index])
         tableDict[letters[index]] = [row, col]
         index += 1 
         
   return [tableDict, tableArray]

# decrypt takes in a cipher and the keyword for the cipher, decryping and printing the resulting phrase
def decrypt(cipher, keyword):
   tableDict, tableArray = generateTable(keyword)
   result = ""
   cipherIndex = 0 # index to loop through each pair in the cipher
   
   while cipherIndex < len(cipher) - 1:
      # row and col of the pair of letters
      row1 = tableDict[cipher[cipherIndex]][0] 
      col1 = tableDict[cipher[cipherIndex]][1]
      row2 = tableDict[cipher[cipherIndex + 1]][0] 
      col2 = tableDict[cipher[cipherIndex + 1]][1]
      
      if row1 == row2: # if the two letters are in the same row, take the character to the left of the current letter
         # append1 and append2: the rows and columns of the letters in the pair (to later check for irregular character "X")
         append1 = [row1, 4] if col1 == 0 else [row1, col1 - 1] # condition checks if there is no character to the left, instead looping to the end of the row
         append2 = [row1, 4] if col2 == 0 else [row1, col2 - 1] 
      elif col1 == col2: # if the two letters are in the same col, take the character above the current letter
         append1 = [col1, 4] if row1 == 0 else [col1, row1 - 1] # condition checks if there is no character above, instead looping to the bottom of the col
         append2 = [col1, 4] if row2 == 0 else [col1, row2 - 1]
      else: # if the two letters meet neither above condition
         # takes the coordinates of the horizontal opposite corner of the rectangle formed by the two letters
         append1 = [row1, col2]
         append2 = [row2, col1]
      
      # checks if the resulting row and col of each decrypted letter corresponds to an "X", in which case the letter will not be included in the final result
      # otherwise add the letters at the decrypted rows and cols to the resulting string
      if tableArray[append1[0]][append1[1]] != "X":
         result += tableArray[append1[0]][append1[1]]
      if tableArray[append2[0]][append2[1]] != "X":
         result += tableArray[append2[0]][append2[1]]
      
      cipherIndex += 2 # next pair
         
   print(result)
   
if __name__ == '__main__':
   decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCVA", "SUPERSPY")
   
   

