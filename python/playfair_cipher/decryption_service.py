from playfair_cipher.cipher_matrix import CipherMatrix

"""Stores position of a character in Cipher Matrix"""
class CharacterPosition:
  def __init__(self, row, column):
    self.row = row
    self.column = column

"""This class comprises functions designed for decryption of an encrypted message."""
class DecryptionService:
  def __init__(self, cipher_key):
    self.cipher_key = cipher_key
    self.cipher_matrix = CipherMatrix(cipher_key).get()

  """This function will  :

  1. Generates character pairs from the encrypted message.
  2. Finds the indices of the decrypted message in the cipher matrix.
  3. Retrieves the decrypted message from the character positions.
  4. Reveals the final decrypted message.
  """
  def decrypt(self, message):
    message = self.__clean_message(message)
    character_pairs = self.__generate_character_pairs(message)
    decrypted_message_char_positions = self.__find_decrypted_message_char_positions(character_pairs)
    decrypted_message = self.__get_decrypted_message(decrypted_message_char_positions)
    
    return decrypted_message

  """Removes non-alphabet"""
  def __clean_message(self, message):
    return "".join(char for char in message if char.isalpha()).upper()

  """Generates pairs for decrypting the provided message. 
    It adds 'X' if the pair consists of the same character and returns a list of pairs.""" 
  def __generate_character_pairs(self, message) :
    character_pairs = []
    current_pair = ""
    index = 0

    while index < len(message):
      if len(current_pair) == 1 and current_pair[0] == message[index]:
        current_pair += "X"
      else:
        current_pair += message[index]
        index += 1

      if len(current_pair) == 2:
        character_pairs.append(current_pair)
        current_pair = ""

    return character_pairs

  """Gets position of the character to swap for decryption for all message pairs."""
  def __find_decrypted_message_char_positions(self, character_pairs):
    decrypted_message_char_positions=[]

    for each_character_pair in character_pairs:
      first_character_position = self.__find_position_of_character(each_character_pair[0])
      second_character_position = self.__find_position_of_character(each_character_pair[1])
      
      if first_character_position.column == second_character_position.column:
        # If both characters are in same column
        decrypted_message_char_positions.append([
          CharacterPosition((first_character_position.row - 1) % 5 , first_character_position.column),
          CharacterPosition((second_character_position.row - 1) % 5 , second_character_position.column)
        ])
      elif first_character_position.row == second_character_position.row:
        # If both characters are in same row
        decrypted_message_char_positions.append([
          CharacterPosition(first_character_position.row, (first_character_position.column - 1) % 5),
          CharacterPosition(second_character_position.row, (second_character_position.column - 1) % 5)
        ])
      else:
        # If both characters form a rectangle
        decrypted_message_char_positions.append([
          CharacterPosition(first_character_position.row, second_character_position.column),
          CharacterPosition(second_character_position.row, first_character_position.column)
        ])

    return decrypted_message_char_positions
  
  """This will return the decrypted message, including any 'X' characters added during pair generation."""
  def __get_decrypted_message(self, decrypted_message_char_positions):
    decrypted_message = ""

    for each_element in decrypted_message_char_positions:
      first_char_position = each_element[0]
      decrypted_message += self.__find_character_at_postition(first_char_position)

      second_char_position = each_element[1]
      decrypted_message += self.__find_character_at_postition(second_char_position)

    return decrypted_message.replace("X", "")
  
  """This function returns the indices of a character from the Cipher Matrix."""
  def __find_position_of_character(self, character):
    for row in range(0,5):
      for column in range(0,5):
        char_at_current_position = self.cipher_matrix[row][column]

        if char_at_current_position == character:
          return CharacterPosition(row, column)
    raise Exception(f"Character {character} was not found in Cipher matrix")
        
  """Returns character at a given position."""
  def __find_character_at_postition(self, character_position):
    return self.cipher_matrix[character_position.row][character_position.column]
