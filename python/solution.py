class PlayFairCipherDecoder:
  def __init__(self, key):
    self.pf_grid = self.__generate_playfair_grid(key)
  
  def __insert_into_grid(self, grid: list, letters: str, exclude: set):
    curIdx = 0
    seenChars = exclude.copy()
    curRow = []
    # Is there room in the last row of the grid to insert?
    if grid and len(grid[-1]) != 5:
      curRow = grid.pop()
    while len(grid) < 5 and curIdx < len(letters):
      if len(curRow) == 5:
        grid.append(curRow)
        curRow = []
      curChar = letters[curIdx]
      if curChar in seenChars:
        curIdx += 1
        continue
      seenChars.add(curChar)
      curRow.append(curChar)
      curIdx += 1
    
    if len(grid) < 5 and 1 <= len(curRow) < 5:
      grid.append(curRow)
  
  def __generate_playfair_grid(self, key: str):
    """
    Generates a Playfair Cipher grid, given a key.
    
    Parameters:
      key (str): The encoded message
    Returns:
      grid (list(list(str))): The Playfair Grid generated with key
    """
    key = ''.join(key.split(" ")).upper().replace("J", "I")
    # Append the rest of the characters
    exclude = set()
    grid = []
    # First insert key into the grid
    self.__insert_into_grid(grid, key, exclude)
    # Next insert the remaining characters of the alphabet (skip j)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    self.__insert_into_grid(grid, alphabet, exclude)
    return grid

  def decode(self, message: str):
    """
    Returns a decoded message which has been encrypted with
    a Playfair cipher.
    
    Parameters:
      message (str): The encoded message
    returns:
      decoded_message (str): The decoded message
    """
    print(self.pf_grid)
    return "init"

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "PLAY FAIR EXAMPLE"#"SUPERSPY"

playFairCipher = PlayFairCipherDecoder(key)
print(playFairCipher.decode(message))