# Playfair Cypher

# Declare variables
key = "SUPERSPY"
key = key.replace("J", "I")
alphabet = key + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

# Create the cypher grid
cypher = []
for letter in alphabet:
    if letter not in cypher:
        cypher.append(letter)

cypher = [cypher[0:5], cypher[5:10], cypher[10:15], cypher[15:20], cypher[20:25]]

# Create the position map for referencing letter positions
x = 0
y = 0
positionMap = {}

for i in range(5):
    for j in range(5):
        positionMap[cypher[i][j]] = (i, j)

output = ""

# Decrypt the message
for i in range(0, len(message), 2):
    pair = message[i:i+2]

    index1 = positionMap[pair[0]]
    index2 = positionMap[pair[1]]

    # same row
    if (index1[0] == index2[0]):
        output += cypher[index1[0]][index1[1] - 1] + cypher[index2[0]][index2[1] - 1]
    # same column
    elif (index1[1] == index2[1]):
        output += cypher[index1[0] - 1][index1[1]] + cypher[index2[0] - 1][index2[1]]
    # rectangle case
    else:
        output += cypher[index1[0]][index2[1]] + cypher[index2[0]][index1[1]]

# get rid of X's since they aren't commonly used
output = output.replace("X", "")
print(output)


