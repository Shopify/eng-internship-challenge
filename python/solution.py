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
    if len(grid) < 5 and 1 <= len(curRow) <= 5:
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
    grid = []
    # First insert key into the grid
    self.__insert_into_grid(grid, key, set())
    # Next insert the remaining characters of the alphabet (skip j)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    self.__insert_into_grid(grid, alphabet, set(key))
    return grid

  def __decode_pair_same_col(self, col:int, pair: tuple):
    first, second = pair # the rows of the pair
    decoded_first = self.pf_grid[(first - 1)%5][col]
    decoded_second = self.pf_grid[(second - 1)%5][col]
    return decoded_first, decoded_second

  def __decode_pair_same_row(self, row: int, pair: tuple):
    first, second = pair # the columns of the pair
    decoded_first = self.pf_grid[row][(first - 1)%5]
    decoded_second = self.pf_grid[row][(second - 1)%5]
    return decoded_first, decoded_second

  def __decoded_diagonal_pair(self, pair: tuple):
    first_row, first_col = pair[0]
    second_row, second_col = pair[1]
    decoded_first = self.pf_grid[first_row][second_col]
    decoded_second = self.pf_grid[second_row][first_col]
    return decoded_first, decoded_second

  def __decode_pair(self, pair: tuple):
    # Find their indexes on the grid
    first = (0, 0)
    second = (0, 0)
    for i in range(5):
      for j in range(5):
        if self.pf_grid[i][j] == pair[0]:
          first = (i, j)
        if self.pf_grid[i][j] == pair[1]:
          second = (i, j)
    if first[0] == second[0]:
      return self.__decode_pair_same_row(first[0], (first[1], second[1]))
    elif first[1] == second[1]:
      return self.__decode_pair_same_col(first[1], (first[0], second[0]))
    else:
      return self.__decoded_diagonal_pair((first, second))
  def decode(self, message: str):
    """
    Returns a decoded message which has been encrypted with
    a Playfair cipher.
    
    Parameters:
      message (str): The encoded message
    returns:
      decoded_message (str): The decoded message
    """
    message = ''.join(message.upper().replace("J", "I").split(" "))
    decoded_message = ""
    for i in range(0, len(message), 2):
      decoded_pair = self.__decode_pair((message[i], message[i+1]))
      decoded_message += ''.join(decoded_pair)
    
    # Remove any Xs that were added to make the message even
    decoded_message = decoded_message.replace("X", "")
    return decoded_message

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
key = "SUPERSPY"

playFairCipher = PlayFairCipherDecoder(key)
print(playFairCipher.decode(message))