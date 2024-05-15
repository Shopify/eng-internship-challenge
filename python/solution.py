
ENCRYPTED_MSSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
J_ASCII_VAL = 74
I_ASCII_VAL = 73
KEY = "SUPERSPY"
FILL_LETTER = 'X'

def createDigraphs(mssg, idx=0):
  if not (idx < len(mssg)):
    return []
  if not (idx + 1 < len(mssg)):
    return [(mssg[idx], FILL_LETTER)] 
  else:
    fst = mssg[idx]
    scnd = mssg[idx + 1]
    if fst == scnd:
      return [(mssg[idx], FILL_LETTER)] + createDigraphs(mssg, idx + 1)
    else:
      return [(mssg[idx], mssg[idx + 1])] + createDigraphs(mssg, idx + 2)


def cipherSolver(key, mssg):
  key_upper = key.upper().replace('J', 'I')
  
  digraphs = createDigraphs(list(mssg.upper()))
  alphabet = [chr(ascii_val) for ascii_val in range(65, 91) if (not ascii_val == 74) and (chr(ascii_val) not in key_upper) and not (ascii_val == I_ASCII_VAL and 'J' in key_upper)]
  
  duplicates = set()
  key_table = [char for char in key_upper if not (char in duplicates or duplicates.add(char))] + alphabet
  
  deciphered = []
  for (fst, scnd) in digraphs:
    fst_index = key_table.index(fst)
    scnd_index = key_table.index(scnd)
    fst_row = fst_index // 5
    fst_col = fst_index % 5
    snd_row = scnd_index // 5
    snd_col = scnd_index % 5

    if fst_row == snd_row:
      deciphered.append(key_table[fst_row * 5 + ((fst_col - 1) % 5)])
      deciphered.append(key_table[snd_row * 5 + ((snd_col - 1) % 5)])
    elif fst_col == snd_col:
      deciphered.append(key_table[(fst_index + 5) % len(key_table)])
      deciphered.append(key_table[(scnd_index + 5) % len(key_table)])
    else: 
      deciphered.append(key_table[fst_row * 5 + snd_col])
      deciphered.append(key_table[snd_row * 5 + fst_col])

  filtered = ''.join(deciphered).replace('X', "")
  print(filtered)

cipherSolver(KEY, ENCRYPTED_MSSG)