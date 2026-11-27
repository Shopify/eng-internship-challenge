import re

class PlayfairCipher:

  def __init__(self, key):
    self.cipher_matrix, self.char_coordinates = self._build_cypher_square(key)

  #Returns the cipher Matrix and the coordinates of characters in the cipher Matrix in a tuple (List[List[str]], Dict[str, Tuple[int, int]])
  def _build_cypher_square(self, key):
    key = self._remove_special_characters(key.replace(' ', '').upper().replace('J', 'I'))
    cipher_matrix = [['' for _ in range(5)] for _ in range(5)]
    char_coordinates = {}
    r, c = 0, 0

    # Process Key First
    for char in key:
      if char not in char_coordinates:
        cipher_matrix[r][c] = char
        char_coordinates[char] = (r, c)
        c += 1
        if c >= 5:
          c = 0
          r += 1

    # Process the remaining letters
    for i in range(26):
      char = chr(ord('A') + i)
      #Add characters to matrix in order, making sure repeated charachers and 'J' is not added
      if char != 'J' and char not in char_coordinates:
        cipher_matrix[r][c] = char
        char_coordinates[char] = (r, c)
        c += 1
        if c >= 5:
          c = 0
          r += 1
          
    return cipher_matrix, char_coordinates

  #Returns a text with no special characters
  def _remove_special_characters(self, text):
    # Regular expression pattern to match special characters
    pattern = r'[^a-zA-Z0-9\s]'  

    return re.sub(pattern, '', text)
  
  def decrypt(self, encrypted_text):
    #Remove all the spaces, special characters,and replace J with I as we can only fit 25 letters in 5 by 5
    encrypted_text = self._remove_special_characters(
                        encrypted_text.replace(' ', '').upper().replace('J', 'I')
                      )
    decrypted_text = ''

    # Ensure length of encrypted_text is even
    if len(encrypted_text) % 2 != 0:
      encrypted_text += 'X'

    i = 0
    for i in range(0, len(encrypted_text) - 1, 2):
      #Postion of the digram
      row_one, col_one = self.char_coordinates[encrypted_text[i]]
      row_two, col_two = self.char_coordinates[encrypted_text[i + 1]]

      # Rule for same row
      if row_one == row_two:
        #We use % for wraping from the row
        decrypted_text += self.cipher_matrix[row_one][(col_one - 1) % 5]
        decrypted_text += self.cipher_matrix[row_two][(col_two - 1) % 5]

      # Rule for same column
      elif col_one == col_two:
         #We use % for wraping from the column
        decrypted_text += self.cipher_matrix[(row_one - 1) % 5][col_one]
        decrypted_text += self.cipher_matrix[(row_two - 1) % 5][col_two]

      # Froms Rectange, take the corners of the rectangle
      else:
        decrypted_text += self.cipher_matrix[row_one][col_two]
        decrypted_text += self.cipher_matrix[row_two][col_one]

    return decrypted_text.replace('X', '')

if __name__ == "__main__":
  text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  key = "SUPERSPY"
  cipher = PlayfairCipher(key)
  print(cipher.decrypt(text))