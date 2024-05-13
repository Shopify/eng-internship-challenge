import string

class CipherMatrix:
  def __init__(self,cipherkey):
    self.matrix=[]
    self.cipherKey=cipherkey
    self.__create()

  def __create(self):
    cipherChars = self.__getAllCipherChars()
    self.__populateMatrix(cipherChars)

  def get(self):
    return self.matrix
  
  def __populateMatrix(self, cipherChars):
    letter_count=0
    for _ in range(5):
      matrix_row=[]
      for _ in range(5):
        matrix_row.append(cipherChars[letter_count])
        letter_count+=1
      self.matrix.append(matrix_row)

  def __getAllCipherChars(self):
    cipherChars = []
    for each_char in self.cipherKey:
      if each_char not in cipherChars:
        cipherChars.append(each_char.upper())
    
    for each_letter in string.ascii_uppercase:
      if each_letter not in cipherChars and each_letter not in ('I','J'):
        cipherChars.append(each_letter)
      elif 'I/J' not in cipherChars and each_letter  in ('I','J'):
        cipherChars.append('I/J')
    return cipherChars
  