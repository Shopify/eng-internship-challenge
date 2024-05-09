ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

def __clean_string(key: str) -> str:
  """ Convert key to uppercase and remove non-alphabetical chars """
  key = key.upper().replace('J', 'I')
  return ''.join(filter(str.isalpha, key.upper()))

def __build_playfair_grid(secret_key: str) -> list[list[str]]:
  """ Create the playfair cipher grid using secret key """
  cleaned_key = __clean_string(secret_key)
  duplicates = set()
  grid = [char for char in cleaned_key if not(char in duplicates or duplicates.add(char))]
  grid = grid + [letter for letter in ALPHABET if letter not in duplicates]
  return [grid[i:i+5] for i in range(0, 25, 5)]

def __find_position(letter: str, grid: list[list[str]]) -> tuple[int, int]:
  """ Find row and column of a letter in given grid """
  for i, row in enumerate(grid):
    for j, char in enumerate(row):
      if char == letter:
        return i, j
  return None

def __decrypt_playfair(encrypted_message: str, key: str) -> str:
    """ Decrypt message using Playfair cipher algorithm """
    grid = __build_playfair_grid(key)
    encrypted_message = __clean_string(encrypted_message)

    if len(encrypted_message) % 2 != 0:
      text += 'X'
    
    digraphs = [encrypted_message[i:i+2] for i in range(0, len(encrypted_message), 2)]

    decrypted_message = ""
    for pair in digraphs:
      row1, col1 = __find_position(pair[0], grid)
      row2, col2 = __find_position(pair[1], grid)
        
      if row1 == row2:
        col1 = (col1 - 1) % 5
        col2 = (col2 - 1) % 5
      elif col1 == col2:
        row1 = (row1 - 1) % 5
        row2 = (row2 - 1) % 5
      else:
          col1, col2 = col2, col1
      
      decrypted_message += grid[row1][col1] + grid[row2][col2]
    
    return decrypted_message.replace('X', "")

def main() -> None:
  KEY: str = "SUPERSPY"
  ENCRYPTED_MESSAGE: str = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

  print(__decrypt_playfair(ENCRYPTED_MESSAGE, KEY))

if __name__ == "__main__":
  main()
  