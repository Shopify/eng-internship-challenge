from playfair_cipher.cipher_matrix import CipherMatrix

"""Stores position of a character in Cipher Matrix"""
class CharacterPosition:
  def __init__(self, row: int, column: int):
    self.row = row
    self.column = column

"""This class comprises functions designed for decryption of an encrypted message."""
class DecryptionService:
  def __init__(self, cipher_key: str) -> None:
    self.cipher_key = cipher_key
    self.cipher_matrix = CipherMatrix(cipher_key).get()

  """This function will  :

  1. Generates character pairs from the encrypted message.
  2. Finds the indices of the decrypted message in the cipher matrix.
  3. Retrieves the decrypted message from the character positions.
  4. Reveals the final decrypted message.
  """
  def decrypt(self, message: str) -> str:
    character_pairs = self.__generate_character_pairs(message)
    decrypted_message_char_positions = self.__find_decrypted_message_char_positions(character_pairs)
    decrypted_message = self.__get_message_from_char_positions(decrypted_message_char_positions)
    revealed_decrypted_message = self.__remove_fillers_from_decrypted_message(decrypted_message)

    return revealed_decrypted_message

  """This function generates pairs for decrypting the provided message. 
    It adds 'X' if the pair consists of the same character and returns a list of pairs.""" 
  def __generate_character_pairs(self, message: str) -> list[str]:
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
  
  """This function returns the indices of a character from the Cipher Matrix."""
  def __find_position_of_character(self, character: str) -> CharacterPosition:
    for row in range(0,5):
      for column in range(0,5):
        char_at_current_position = self.cipher_matrix[row][column]

        if char_at_current_position == character or (
          character in ('I', 'J') and char_at_current_position == 'I/J'
        ):
          return CharacterPosition(row, column)
        
  """Returns character at a given position."""
  def __find_character_at_postition(self, character_position: CharacterPosition):
    cipher_char = self.cipher_matrix[character_position.row][character_position.column]

    # This will returns 'I' for both 'I' and 'J', treating them as equivalent.
    if cipher_char == 'I/J':
      cipher_char = 'I'
    return cipher_char
  
  """Gets position of the character to swap if both characters in the pair are in same column."""
  def __get_same_column_decrypted_position(self, message_char: CharacterPosition):
    return CharacterPosition((message_char.row - 1) % 5 , message_char.column)
  
  """Gets position of the character to swap if both characters in the pair are in same rows."""
  def __get_same_row_decrypted_position(self, message_char: CharacterPosition):
    return CharacterPosition(message_char.row, (message_char.column - 1) % 5)
  
  """Gets position of the character to swap if both characters in the pair forms a rectangle."""
  def __get_rectangle_decrypted_position(self, first_message_char: CharacterPosition, second_message_char: CharacterPosition):
    return [
      CharacterPosition(first_message_char.row, second_message_char.column),
      CharacterPosition(second_message_char.row, first_message_char.column)
    ]

  """Gets position of the character to swap for decryption for all message pairs."""
  def __find_decrypted_message_char_positions(self, character_pairs: list[str]) -> list[CharacterPosition]:
    decrypted_message_char_positions=[]

    for each_character_pair in character_pairs:
      first_character_position = self.__find_position_of_character(each_character_pair[0])
      second_character_position = self.__find_position_of_character(each_character_pair[1])
      
      if first_character_position.column == second_character_position.column:
        decrypted_message_char_positions.append([
          self.__get_same_column_decrypted_position(first_character_position),
          self.__get_same_column_decrypted_position(second_character_position)
        ])
      elif first_character_position.row == second_character_position.row:
        decrypted_message_char_positions.append([
          self.__get_same_row_decrypted_position(first_character_position),
          self.__get_same_row_decrypted_position(second_character_position)
        ])
      else:
        decrypted_message_char_positions.append(self.__get_rectangle_decrypted_position(first_character_position, second_character_position))

    return decrypted_message_char_positions
  
  """This will return the decrypted message, including any 'X' characters added during pair generation."""
  def __get_message_from_char_positions(self, decrypted_message_char_positions: list[CharacterPosition]) -> str:
    decrypted_message = ""

    for each_element in decrypted_message_char_positions:
      first_char_position = each_element[0]
      decrypted_message += self.__find_character_at_postition(first_char_position)

      second_char_position = each_element[1]
      decrypted_message += self.__find_character_at_postition(second_char_position)

    return decrypted_message
  
  """This function removes any 'X' characters added during pair generation to obtain the original decrypted message."""
  def __remove_fillers_from_decrypted_message(self, decrypted_message: str) -> str:
    index = 1
    while index < len(decrypted_message) - 1:
      if decrypted_message[index] == "X" and decrypted_message[index-1] == decrypted_message[index+1]:
        decrypted_message = decrypted_message.replace(decrypted_message[index], "")
      index += 1

    # check for  extra 'X' char at the end of decrypted message
    if decrypted_message[-1] == "X" and len(decrypted_message) % 2 == 0:
      decrypted_message = decrypted_message[:-1]

    return decrypted_message
