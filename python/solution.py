
# Playfair Decoding - Shopify
# By: Ryan Lin
# Tuesday, May 14th, 2024

# Assumptions made:
# - Bogus/Insert letter is X 
#       - Remove all X in the decoded string according to instruction 6
#
# - Matrix size is 5x5 (standard for playfair cipher)
# - All plaintext and ciphertext have to be alphabetical
# - I and J are interchangeable
# - Output should be in all caps
# - Ciphertext should be even length


class PlayfairCipher:
  MATRIX_SIZE = 5
  DECODE_STEP = -1
  BOGUS_LETTER = "X"

  def __init__(self, key):
    self.key = key
    self.letter_coords = dict()  # map letters to row and col
    self.matrix = self.generate_matrix()

  # Generates a 5x5 matrix given using the cipher key
  def generate_matrix(self):

    used_letters = set()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    row_index = 0
    col_index = 0
    matrix = []
    current_row = []

    for letter in self.key + alphabet:
      if not letter.isalpha():
        raise ValueError("Key contains non-alphabetical elements")
        
      if letter == "J": letter = "I"
      letter = letter.upper()
      if letter in used_letters:
        continue

      # Add letter to current row, keep track of use, and coords
      current_row += [letter]
      used_letters.add(letter)
      self.letter_coords[letter] = (row_index, col_index)
      col_index += 1
      if col_index == self.MATRIX_SIZE:
        matrix += [current_row]
        current_row = []
        col_index = 0
        row_index += 1

    return matrix

  # Given 2 letters, return their letter mappings
  def map_letters(self, first_letter, second_letter):
    first_x, first_y = self.letter_coords[first_letter]
    second_x, second_y = self.letter_coords[second_letter]

    first_mapping = ""
    second_mapping = ""
    # If letters are in the same column, get letters above each one
    if first_y == second_y:
      first_above_ind = (first_x + self.DECODE_STEP) % self.MATRIX_SIZE
      second_above_ind = (second_x + self.DECODE_STEP) % self.MATRIX_SIZE
      first_mapping = self.matrix[first_above_ind][first_y]
      second_mapping = self.matrix[second_above_ind][second_y]

    # If letters are in the same row, get letters to the left of each one
    elif first_x == second_x:
      first_left_ind = (first_y + self.DECODE_STEP) % self.MATRIX_SIZE
      second_left_ind = (second_y + self.DECODE_STEP) % self.MATRIX_SIZE
      first_mapping = self.matrix[first_x][first_left_ind]
      second_mapping = self.matrix[second_x][second_left_ind]

    # If neither same row or column, form a rectangle using coords and
    # get letters on horizontal opposite corner of the rectangle
    else:
      first_mapping = self.matrix[first_x][second_y]
      second_mapping = self.matrix[second_x][first_y]

    return first_mapping, second_mapping

  # Given ciphertext, decrypts it using Playfair matrix
  def decrypt(self, ciphertext):
    if len(ciphertext) % 2 != 0:
      raise ValueError("Ciphertext is not even length")

    plaintext = ""
    for i in range(0, len(ciphertext), 2):

      # Gather pairs of letters and add their mapping to the plaintext result
      first_letter = ciphertext[i]
      second_letter = ciphertext[i + 1]

      if not first_letter.isalpha() or not second_letter.isalpha():
        raise ValueError("Ciphertext contains non-alphabetical elements")

      first_mapping, second_mapping = self.map_letters(first_letter, second_letter)
      plaintext = plaintext + first_mapping + second_mapping

    return plaintext

  # Remove extraneous bogus/inserted letter, ensure alphabetical
  def format_output(self, plaintext):
    formatted_plaintext = ""
    
    for i in range(len(plaintext)):
      letter = plaintext[i]
      if not letter.isalpha():
        raise ValueError("Plaintext contains non-alphabetical elements")

      if letter == self.BOGUS_LETTER:
        continue

      formatted_plaintext += letter
    return formatted_plaintext


def main():
  # Set the ciphertext and the key
  ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  key = "SUPERSPY"

  # Create a PlayfairCipher instance then decrypt it
  playfair_cipher = PlayfairCipher(key)
  plaintext = playfair_cipher.decrypt(ciphertext)

  # Format and output the decrypted message
  formatted_plaintext = playfair_cipher.format_output(plaintext)
  print(formatted_plaintext)

if __name__ == "__main__":
    main()
