'''
Function to convert all the characters of a string to uppercase
str: a string to be converted
returns a string convered to upper case
'''
def toUpperCase(str):
   return str.upper()

'''
Function to remove all spaces in a string
str: a string to be checked
returns a string spaces are removed
''' 
def removeSpaces(str):
   return ''.join(str.split())

'''
Function to remove all special characters in a string
str: a string to be checked
returns a string special characters are removed
''' 
def removeSpecialCharactors(str):
   strToReturn = ""
   for ch in str:
      if ch.isalnum():
         strToReturn += ch
   return strToReturn

'''
Function to convert a string to the valid string
str: a string to be checked
returns a valid string
''' 
def validString(str):
   str = removeSpaces(removeSpecialCharactors(toUpperCase(str)))
   return str

'''
Function to generate a table
key: a string to be added in the table
returns the table
''' 
def generateTable(key):
   table = [['' for i in range(5)] for j in range(5)]
   alphabet = [chr(i + 65) for i in range(26)]
   seen = set()
   
   # add key in the table
   i, j, k = 0, 0, 0
   for k in range(len(key)):
      if key[k] not in seen:
         seen.add(key[k])
         table[i][j] = key[k]
         j += 1
         if j == 5:
               i += 1
               j = 0
      k += 1
   
   # add rest of the alphabet except "J"
   for k in range(len(alphabet)):
      if alphabet[k] not in seen:
         if alphabet[k] != 'J':
            seen.add(alphabet[k])
            table[i][j] = alphabet[k]
            j += 1
            if j == 5:
               i += 1
               j = 0
   return table

'''
Function to search for characters
table: table to search for the character from
ch: character to search
returns the position of the character
''' 
def search(table, ch):
   pos = [0, 0]

   if ch == 'J':
      ch = 'I'

   for i in range(5):
      for j in range(5):
         if table[i][j] == ch:
            pos[0], pos[1] = i, j

   return pos

'''
Function to find the modulus of 5
a: num to find the modulus of 5
returns the modulus of 5
''' 
def mod5(a):   
   if a < 0:
      return a     
   return a % 5

'''
Function to decrypt
table: table to search for the characters from
str: string to search
returns decrypted message
''' 
def decrypt(table, str):
   for i in range(0,len(str),2):
      if str[i] == str[i+1]:
         str = str[:i+1] + "X" + str[i+1:]
      pos1 = search(table, str[i])
      pos2 = search(table, str[i+1])
      # same row
      if pos1[0] == pos2[0]:
         str = str[:i] + table[pos1[0]][mod5(pos1[1]-1)] + table[pos2[0]][mod5(pos2[1]-1)] + str[i+2:]
      # same column
      elif pos1[1] == pos2[1]:
         str = str[:i] + table[mod5(pos1[0]-1)][pos1[1]] + table[mod5(pos2[0]-1)][pos2[1]] + str[i+2:]
      else:
         str = str[:i] + table[pos1[0]][pos2[1]] + table[pos2[0]][pos1[1]] + str[i+2:]
   
   # omit bogus letters, "X" and "Z", and space
   message = str.replace("X", "").replace(" ", "")
   if message[len(message)-1] == 'Z':
      message = message[:len(message)-1]
   return message

'''
Function to decrypt using Playfair Cipher
str: string to convert
key: key to generate table
returns decrypted message
''' 
def decipher(str, key):
   key = validString(key)
   str = validString(str)
   table = generateTable(key)
   decryptedMessage =decrypt(table, str)
   return decryptedMessage

if __name__ == '__main__':
   key = "SUPERSPY"
   encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
   decryptedMessage = decipher(encryptedMessage,key)
   print(decryptedMessage)
   