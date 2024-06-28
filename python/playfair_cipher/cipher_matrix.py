import string

"""The Cipher Matrix includes a 2D list with the Cipher Key's letters and non-repeating alphabet letters."""
class CipherMatrix:
  def __init__(self, cipher_key):
    self.matrix = []
    self.cipher_key = self.__clean_cipher_key(cipher_key)
    self.__create()

  """Gets the matrix"""
  def get(self):
    return self.matrix
  
  """Gets cipher chars and creates a 2D 5x5 matrix"""
  def __create(self):
    cipher_chars = self.__get_all_cipher_chars()
    self.__populate_matrix(cipher_chars)

  """Removes non-alphabet, replaces 'J' with 'I'"""
  def __clean_cipher_key(self, cipher_key):
    return "".join([char for char in cipher_key if char.isalpha()]).replace("J", "I").upper()
  
  """Populates 2D cipher matrix with cipher chars"""
  def __populate_matrix(self, cipher_chars):
    letter_count = 0
    for _ in range(5):
      matrix_row = []
      for _ in range(5):
        matrix_row.append(cipher_chars[letter_count])
        letter_count += 1
      self.matrix.append(matrix_row)

  """Gets all characters for cipher matrix."""  
  def __get_all_cipher_chars(self):
    cipher_chars = []
    for each_char in self.cipher_key:
      if each_char not in cipher_chars:
        cipher_chars.append(each_char.upper())

    # Replaces 'J' with 'I' to fit in matrix
    for each_letter in string.ascii_uppercase.replace('J', 'I'):
      if each_letter not in cipher_chars:
        cipher_chars.append(each_letter)

    return cipher_chars
