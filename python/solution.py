#Import re module to use regular expression suport
import re

'''
Before the keyword 'SUPERSPY' can be used in the array to come, it must be proccessed to meet the cipher rules

Cipher Rules for the Keyword Include:
1. All characters must be uppercase - as all of our values will be uppercase in the matrix
2. There are no repeating letters in the keyword
3. There are no special characters in the keyword

For the purpose of this application, I will only be needing to process the keyword 'SUPERSPY' but to allow users to process any keyword, a method is written to and a keyword is used as the parameter of this method.
'''

def keyword_processor (keyword):
  #Remove all characters that are not A-Z and a-z (i.e. special characters) within the capitzalized keyword string 
  keyword = re.sub(r'^a-zA-Z]', '', keyword.upper())

  #In the matrix, J is replaced with I, so we must do the same within the keyword. We must do this before removing duplicates in case we create a duplicate as a result of this proccess.
  keyword = keyword.replace('J', 'I')

  #Now we must remove any potential duplicates. This is done by 
  new_value = []
  #processed_keyword = ""

  for char in keyword:
    if char not in new_value:
      new_value.append(char)
     # processed_keyword += char
  
  #Build matrix and initalize allphabets variable without the letter 'J'
  matrix = []
  alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

  #Fill the matrix with the keyword and remove common letters between the alphabets and keyword
  for char in new_value:
    matrix.append(char)
    alphabet = alphabet.replace(char, '')

  #Fill the matrix with any uncommon and remaining alphabet letters
  for char in alphabet:
    matrix.append(char)
  return matrix

def decrypt_msg(ciphertext, keyword):
  #initialize matrix from the keyword_processor function, text matrix, and clean ciphertext to be used for length/loop operations
  matrix = keyword_processor(keyword)
  text = []
  i = 0
  ciphertext = re.sub(r'[^A-Za-z]', '', ciphertext.upper()) 

  while i < len(ciphertext) -1:
    #Split the encrypted message into character pairs char 1, char 2
    char1 = ciphertext[i]
    char2 = ciphertext[i+1]

# Find positions in the matrix
    index1 = matrix.index(char1)
    index2 = matrix.index(char2)
        
    # Same row, shift left
    if index1 // 5 == index2 // 5:
      text.append(matrix[index1 - 1 if index1 % 5 != 0 else index1 + 4])
      text.append(matrix[index2 - 1 if index2 % 5 != 0 else index2 + 4])
        
    # Same column, shift up
    elif index1 % 5 == index2 % 5:            
      text.append(matrix[index1 - 5 if index1 >= 5 else index1 + 20])
      text.append(matrix[index2 - 5 if index2 >= 5 else index2 + 20])
        
    # Forming a rectangle, swap corners
    else:
      text.append(matrix[index1 - (index1 % 5 - index2 % 5)])
      text.append(matrix[index2 - (index2 % 5 - index1 % 5)])
        
    i += 2

  # Remove 'X' characters from the decrypted message
  decrypted_message = ''.join(text).replace('X', '')  
  return decrypted_message

#Executable
if __name__ == "__main__":
    ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
    key = "SUPERSPY"
    
    decrypted_message = decrypt_msg(ciphertext, key)
    print(decrypted_message)
