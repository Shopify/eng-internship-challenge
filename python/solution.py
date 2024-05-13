class Playfair():
  
  '''
  Parameters:
    key: type string, the input key for the instance
    message: type string, the input message for the instance
  
  Variables:
    self.key: type string, represents an uppercase version of the input key
    self.message: type string, represents an uppercase version of the input message to be decoded
    self.digrams: type list, represents the input message in pairs
    self.table_letters: type string, represents the order of the letters as they would appear in the 5x5 grid reading from left to right
    self.letter_map: type dictionary, represents the 5x5 grid locations for self.table_letters
  '''
  def __init__(self, key, message):
    self.key = key.upper()
    self.message = message.upper()
    self.digrams = self.split_message(self.message) #note: looping to split to digrams then looping through the digrams means O(2n) instead of O(n) is used, but this is done for readability
    self.table_letters = self.table_generation(self.key)
    self.letter_map = self.letter_mapping(self.table_letters)


  '''
  Parameters:
    key: type string, will be self.key

  Return type: string, used to create self.table_letters
  '''
  def table_generation(self, key):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' #omits 'J' as it is replaceable with 'I'
    
    encrypted_key = ''
    for letter in key: #loop through each letter in the key and add it encrypted_key only if it has not been encountered before
      if letter not in encrypted_key:
        encrypted_key += letter

    encrypted_rest = ''.join(char for char in alphabet if char not in key)

    combined = encrypted_key + encrypted_rest #return the letters from the key first, then the remaining unused letters

    return combined
  

  '''
  Parameters:
    letters: type string, will be self.table_letters

  Return type: dictionary, used to create self.letter_map
  '''
  def letter_mapping(self, letters):
    map = dict()
    table_letters = letters

    for i in range(0, 25): #loop through the string and assign the 5x5 grid location to each letter
      letter = table_letters[i]
      row = i // 5
      column = i % 5
      map[letter] = (row, column) #store the locations by letter in the map
    
    return map #return the map which has the grid locations
  

  '''
  Parameters:
    message: type string, will be self.message

  Return type: list, will contain self.message broken into individual pairs
  '''
  def split_message(self, message):
    digrams = []
    
    for i in range(0, len(message) - 1, 2): #encrypted message will always have an even number of letters
      digrams.append(message[i] + message[i + 1]) #loop through the message and append pairs
    
    return digrams
  

  '''
  Parameters:
    digrams: type list, will be self.digrams

  Return type: string, representing the final decrypted message
  '''
  def decrypt(self, digrams):
    decrypted_string = [] #use a list instead of a string to collect decryptiongs and join the list later to use O(n) complexity and avoid creating copies of immutable strings

    for digram in digrams: #loop through digrams and decrypt each one
      locations = self.get_locations(digram)
      row1, column1, row2, column2 = locations[0], locations[1], locations[2], locations[3] #access and store the coordinates of the letters for the current digram

      if row1 == row2: #case 1 for decryption, where the letters are in the same row
        letter1 = self.return_letter(row1, (column1 - 1) % 5) 
        letter2 = self.return_letter(row2, (column2 - 1) % 5)

        decrypted_string.append(letter1)
        decrypted_string.append(letter2)
    
      elif column1 == column2: #case 2 for decryption, where the letters are in the same column
        letter1 = self.return_letter((row1 - 1) % 5, column1)
        letter2 = self.return_letter((row2 - 1) % 5, column2)

        decrypted_string.append(letter1)
        decrypted_string.append(letter2)

      else: #case 3 for decryption, where the letters form a rectangle
        letter1 = self.return_letter(row1, column2)
        letter2 = self.return_letter(row2, column1)

        decrypted_string.append(letter1)
        decrypted_string.append(letter2)
    
    if decrypted_string[-1] == 'X': #removes a trailing 'X', as 'X' would be appended if the plaintext word has an odd amount of letters
      decrypted_string = decrypted_string[:-1]      
    
    final_string = [] #prepare a list to loop through the decrypted string to remove 'X'; this is done in a second loop instead of the first loop to improve readability
    for i in range(0, len(decrypted_string)): #loop through the string to ensure no bogus 'X' were included 
      if i == 0 or i == len(decrypted_string): #ignore the first and last letters during the 'X' check since these will never be 'X' after removing the trailing 'X'
        final_string.append(decrypted_string[i])
      elif decrypted_string[i] == 'X':
        if decrypted_string[i - 1] == decrypted_string[i + 1]:
          continue
      else:
        final_string.append(decrypted_string[i])

    return ''.join(final_string) #return the decrypted message as a string
  

  '''
  Parameters:
    digram: type string, will be the current digram where coordinates are required

  Return type: list, where the first two values and the last two values represent the coordinates of the first and second letter, respectively
  '''
  def get_locations(self, digram):
    map = self.letter_map
    letter1, letter2 = digram[0], digram[1] #split the digram into its two letters
    row1, column1 = map[letter1][0], map[letter1][1] #search the dictionary for letter1 and record its coordinates
    row2, column2 = map[letter2][0], map[letter2][1] #search the dictionary for letter2 and record its coordinates
    return [row1, column1, row2, column2] #return a list containing the coordinates
  

  '''
  Parameters:
    row: type int, representing the row coordinate of a letter
    column: type int, representing the column coordinate of a letter

  Return type: string, representing the letter associated with the coordinates pair
  '''
  def return_letter(self, row, column):
    locations = (row, column) #convert the row and column inputs to a tuple so equality can be compared
    map = self.letter_map

    for letter in map: #loop through the map to find the letter with the corresponding coordinates
      if map[letter] == locations:
        return letter #return the found letter

def main():
  test = Playfair('superspy', 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV')
  print(test.decrypt(test.digrams))
  return(test.decrypt(test.digrams))

main()
