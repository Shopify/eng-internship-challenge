class PlayfairCipher:
  def __init__(self, key):
    self.grid_size = 5
    self.key = key
    # Cipher grid
    self.grid = [["" for _ in range(self.grid_size)] for _ in range(self.grid_size)]
    # Map of characters to their location in grid
    self.pos_of_char = {}

    # Add key to grid
    cur_row = 0
    cur_col = 0
    for c in self.key:
      if cur_col >= self.grid_size: 
        cur_col = 0
        cur_row += 1
      if c not in self.pos_of_char:
        self.grid[cur_row][cur_col] = c
        self.pos_of_char[c] = (cur_row, cur_col)
        cur_col += 1

    # Add remaining characters
    for c in range(65, 91):
      if cur_row >= self.grid_size:
        break
      if cur_col >= self.grid_size: 
        cur_col = 0
        cur_row += 1
      character = chr(c)
      if character not in self.pos_of_char and character != "J":
        self.grid[cur_row][cur_col] = character
        self.pos_of_char[character] = (cur_row, cur_col)
        cur_col += 1

  def positive_mod(self, x):
    if x < 0:
      x += self.grid_size
    return x % self.grid_size

  def decrypt(self, encrypted_text):
    decrypted_text_list = []
    # Decrypt characters in pairs
    for i in range(0, len(encrypted_text), 2):
      c1, c2 = encrypted_text[i], encrypted_text[i + 1]
      r1, c1 = self.pos_of_char[c1]
      r2, c2 = self.pos_of_char[c2]
      d1, d2 = "", ""
      if r1 == r2:
        # Same row: shift left
        d1 = self.grid[r1][self.positive_mod(c1 - 1)]
        d2 = self.grid[r2][self.positive_mod(c2 - 1)]
      elif c1 == c2:
        # Same column: shift up
        d1 = self.grid[self.positive_mod(r1 - 1)][c1]
        d2 = self.grid[self.positive_mod(r2 - 1)][c2]
      else:
        # Different row and column: form rectangle and take opposite corners
        d1 = self.grid[r1][c2]
        d2 = self.grid[r2][c1]
      if d1 != "X":
        decrypted_text_list.append(d1)
      if d2 != "X":
        decrypted_text_list.append(d2)
    return "".join(decrypted_text_list)

if __name__ == '__main__':
  encrypted_text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  key = "SUPERSPY"
  cipher = PlayfairCipher(key)
  decrypted_text = cipher.decrypt(encrypted_text)

  print(decrypted_text)
