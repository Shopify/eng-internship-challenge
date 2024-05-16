def generate_grid(keyword):
  keyword = "".join(dict.fromkeys(keyword.upper().replace(" ", "")))
  keyword = keyword.replace("X", "")
  grid = list(keyword)
  alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  for letter in alphabet:
      if letter not in grid:
          grid.append(letter)

  grid = [grid[i:i+5] for i in range(0, 25, 5)]
  return grid


def decrypt_message(message, keyword):
grid = generate_grid(keyword)
message = message.upper().replace(" ", "")
decrypted_message = ""
    i = 0
    while i < len(message) - 1:
        if message[i] == message[i + 1]:
            message = message[:i + 1] + 'X' + message[i + 1:]
        i += 2
        if len(message) % 2 != 0:
        message += 'X'
    i = 0
    while i < len(message):
        pair = message[i:i+2]

        pos1 = None
        pos2 = None
        for row in range(5):
            if pair[0] in grid[row]:
                pos1 = (row, grid[row].index(pair[0]))
            if pair[1] in grid[row]:
                pos2 = (row, grid[row].index(pair[1]))

        
        if pos1[1] == pos2[1]:
            decrypted_pair = grid[(pos1[0] - 1) % 5][pos1[1]] + grid[(pos2[0] - 1) % 5][pos2[1]]
        
        elif pos1[0] == pos2[0]:
            decrypted_pair = grid[pos1[0]][(pos1[1] - 1) % 5] + grid[pos2[0]][(pos2[1] - 1) % 5]
       
        else:
            decrypted_pair = grid[pos1[0]][pos2[1]] + grid[pos2[0]][pos1[1]]

        decrypted_message += decrypted_pair
        i += 2

    return decrypted_message

encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
keyword = "SUPERSPY"

decrypted_message = decrypt_message(encrypted_message, keyword)
print(decrypted_message)
