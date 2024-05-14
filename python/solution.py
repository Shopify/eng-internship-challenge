import string 

TABLE_SIZE = 5 

def generate_key_table(key: str) -> list[list[str]]:
    """Generate a key table based on the given key"""
    key = key + string.ascii_uppercase
    key = key.replace("J", "") # remove J to fit the alphabet
    key = "".join(dict.fromkeys(key)) # remove duplicates

    if len(key) == TABLE_SIZE * TABLE_SIZE:
      # Create empty 5 x 5 table
      key_table = [['' for x in range(TABLE_SIZE)] for y in range(TABLE_SIZE)]
      k = 0
      for i in range(TABLE_SIZE):
          for j in range(TABLE_SIZE):
              key_table[i][j] = key[k]
              k += 1
      return key_table
    else:
        # Key is not valid
        return None

def split_into_pairs(encrpted_msg: str) -> list[str]:
    """Split the encrypted message into pairs of two"""
    pairs = []
    for i in range(0, len(encrpted_msg), 2):
        pairs.append(encrpted_msg[i:i+2])
    return pairs

def find_row_col(pair: str) -> list[int]:
    """Find the row and column of the pair in the key table"""
    row_col = []
    for letter in pair:
        for i in range(TABLE_SIZE):
            for j in range(TABLE_SIZE):
                if key_table[i][j] == letter:
                    row_col.append(i)
                    row_col.append(j)
    return row_col

def same_row(row_col: list[int]) -> bool:
    "Check if the pair is in the same row in the key table"
    if row_col[0] == row_col[2]:
        return True
    return False

def same_column(row_col : list[int]) -> bool:
    "Check if the pair is in the same column in the key table"
    if row_col[1] == row_col[3]:
        return True
    return False

def decrypt(encrypted_msg: str, key_table: list[list[str]]) -> str:
    """Decrypt the encrypted message"""
    pairs = split_into_pairs(encrypted_msg)
    
    decrypted_msg = ""
    for pair in pairs:
        row_col = find_row_col(pair)
        if same_row(row_col):
            # replace with the letter immediately to the left
            new_pair = key_table[row_col[0]][row_col[1] - 1] + key_table[row_col[2]][row_col[3] - 1]
        elif same_column(row_col):
            # replace with the letter immediately above
            new_pair = key_table[row_col[0] - 1][row_col[1]] + key_table[row_col[2] - 1][row_col[3]]
        else:
            # replace with the letter in the same row but at the other pair's column
            new_pair = key_table[row_col[0]][row_col[3]] + key_table[row_col[2]][row_col[1]]
        decrypted_msg += new_pair

    # remove "X"s (used to seperate repeated letters during encryption)
    decrypted_msg = decrypted_msg.replace("X", "")
    return decrypted_msg

# Run the decryption
if __name__ == "__main__":
  encrypted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  key = "SUPERSPY"

  key_table = generate_key_table(key)
  print(decrypt(encrypted_msg, key_table))
  