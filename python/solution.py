key  = "SUPERSPY"

#Append the rest of the alphabet to the key
for i in range(65, 91):
    key = key + chr(i) if i != 74 else key

#Keep only the first copy of each letter, remove all the other duplicates
noDuplicate_key =  "".join(dict.fromkeys(key))

encrypted_msg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

#Store result characters
result = list()

matrix = [["" for i in range(5)] for j in range(5)]

#Fill the Playfair cipher matrix
for row in range(5):
    for col in range(5):
        matrix[row][col] = noDuplicate_key[row * 5 + col]

#Helper method for locate characters in matrix
def locate(character):
    for index, line in enumerate(matrix): 
        words = ''.join(line)
        col = words.find(character)
        if col > -1:
            return index, col
        else:
            continue
#Decrypt characters in pairs of two
for i in range(0, len(encrypted_msg), 2):
    r1, c1 = locate(encrypted_msg[i])
    r2, c2 = locate(encrypted_msg[i+1])

    if r1 == r2:
        result.append(matrix[r1][(c1-1+5) % 5])
        result.append(matrix[r2][(c2-1+5) % 5])
    elif c1 == c2:
        result.append(matrix[(r1-1+5) % 5][c1])
        result.append(matrix[(r2-1+5) % 5][c2])
    else:
        result.append(matrix[r1][c2])
        result.append(matrix[r2][c1])

#Remove potential X-s  
print("".join(result).replace("X", "")) 


