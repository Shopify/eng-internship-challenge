"""
Name: Aditya Keerthi
Date: May 10, 2024
"""

ENCRYPTED_MESSAGE: str = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
CIPHER_KEY: str = "SUPERSPY"

# PlayfairCipher class
class PlayfairCipher:
  def __init__(self, key: str) -> None:
    """
    Generates matrix based off key phrase
    """
    self.matrix = self.generate_matrix(key)
  
  def generate_cipher_string(self, key: str) -> str:
    """
    Cleaning and setting up the cipher string for the 5x5 matrix
    """
    temp_key = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    seen = set()
    cipher_string = "" 
    for char in temp_key:
      if char not in seen:
        seen.add(char)
        cipher_string += char
    return cipher_string

  def generate_matrix(self, key: str) -> list:
    """
    Generates 5x5 matrix to help decrypt using the PlayfairCipher
    """
    matrix = [[None] * 5 for _ in range(5)]
    cipher_string = self.generate_cipher_string(key)
    for i in range(5):
      for j in range(5):
        loc = 5*i + j
        matrix[i][j] = cipher_string[loc]
    return matrix
  
  def find_letter(self, letter: str) -> tuple:
    """
    Returns an x, y coordinate of the letter in the matrix
    """
    for i, tuple in enumerate(self.matrix):
      if letter in tuple:
        return (i, tuple.index(letter))
  
  def filter_text(self, text):
    """
    Flatten consecutive letters to [1:] + 'X'
    """
    if len(text) % 2 != 0: text += 'X'
    n: int = len(text)
    filtered_text: str = text.replace(' ', '') # get rid of whitespace
    filtered_text = filtered_text.upper() # normalize to uppercase
    result: str = ""
    for i in range(0, len(filtered_text), 2):
      result += filtered_text[i]
      if i + 1 < n and filtered_text[i] == filtered_text[i+1]:
        result += "X"
      else:
        result += filtered_text[i+1]
    return result

  def decrypt_pair(self, l1: str, l2: str):
    """
    Main logic of the PlayfairCipher that locates the corresponding shifted letters when decrypting strings
    """
    l1x, l1y = self.find_letter(l1)
    l2x, l2y = self.find_letter(l2)
    if l1x == l2x:
      return self.matrix[l1x][(l1y - 1) % 5] + self.matrix[l2x][(l2y - 1) % 5]
    elif l1y == l2y:
      return self.matrix[(l1x - 1) % 5][l1y] + self.matrix[(l2x - 1) % 5][l2y]
    else:
      return self.matrix[l1x][l2y] + self.matrix[l2x][l1y]

  def decrypt(self, phrase: str) -> str:
    """
    Decrypt phrase with the use of some helper functions
    """
    phrase = self.filter_text(phrase)
    n: int = len(phrase)

    message: str = ""

    for i in range(0, n, 2):
      message += self.decrypt_pair(phrase[i], phrase[i + 1])
    
    return message.replace('X', '')

if __name__ == '__main__':
  """
  Driver that initializes a PlayfairCipher with the CIPHER_KEY and decrypts the ENCRYPTED_MESSAGE
  """
  cipher: PlayfairCipher = PlayfairCipher(CIPHER_KEY)
  message: str = cipher.decrypt(ENCRYPTED_MESSAGE)
  print(message)