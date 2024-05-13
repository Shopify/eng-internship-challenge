import string

class CipherMatrix:
  def __init__(self,cipherkey):
    self.matrix = []
    self.cipher_key = cipherkey
    self.__create()

  def __create(self):
    cipher_chars = self.__get_all_cipher_chars()
    self.__populate_matrix(cipher_chars)

  def get(self):
    return self.matrix
  
  def __populate_matrix(self, cipher_chars):
    letter_count = 0
    for _ in range(5):
      matrix_row = []
      for _ in range(5):
        matrix_row.append(cipher_chars[letter_count])
        letter_count += 1
      self.matrix.append(matrix_row)

  def __get_all_cipher_chars(self):
    cipher_chars = []
    for each_char in self.cipher_key:
      if each_char not in cipher_chars:
        cipher_chars.append(each_char.upper())
    
    for each_letter in string.ascii_uppercase:
      if each_letter not in cipher_chars and each_letter not in ('I', 'J'):
        cipher_chars.append(each_letter)
      elif 'I/J' not in cipher_chars and each_letter  in ('I', 'J'):
        cipher_chars.append('I/J')
    return cipher_chars
  