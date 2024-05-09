class PlayFairCipherDecoder:
  def __init__(self, key):
    self.pf_grid = self.__generate_playfair_grid(key)
  
  def __generate_playfair_grid(self, key: str):
    """
    Generates a Playfair Cipher grid, given a key.
    
    Parameters:
      key (str): The encoded message
    Returns:
      grid (list(list(str))): The Playfair Grid generated with key
    """
    grid = []
    curRow = []
    curIdx = 0
    seenChars = set()
    while curIdx < len(key):
      if len(curRow) == 5:
        grid.append(curRow)
        curRow = []
      curChar = key[curIdx]
      if curChar in seenChars:
        curIdx += 1
        continue
      seenChars.add(curChar)
      curRow.append(curChar)
      curIdx += 1
    # Append the rest of the characters
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    curIdx = 0
    while len(grid) != 5:
      if len(curRow) == 5:
        grid.append(curRow)
        curRow = []
      curChar = alphabet[curIdx]
      if curChar in seenChars:
        curIdx += 1
        continue
      seenChars.add(curChar)
      curRow.append(curChar)
      curIdx += 1
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
key = "SUPERSPY"

playFairCipher = PlayFairCipherDecoder(key)
print(playFairCipher.decode(message))