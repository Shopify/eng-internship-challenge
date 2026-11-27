# - Replacing J with I
# - Using X if both characters in pair are same
# - Same row -> move one cell left and wrap if required
# - Same col -> move one cell up and wrap if required

# Function to build the cipher matrix
def buildMatrix(cipherKey):

	# A set to avoid adding duplicates in matrix
	seen = set()
	flatMatrix = []
	letters = ''.join([chr(ord('A') + i) for i in range(26)])
	letters = letters.replace('J', 'I')

	for c in cipherKey:
		if c not in seen:
			flatMatrix.append(c)
			seen.add(c)
	
	for c in letters:
		if c not in seen:
			flatMatrix.append(c)
			seen.add(c)
	
	# Building 2D matrix from flat matrix
	matrix = [flatMatrix[i:i+5] for i in range(0, 25, 5)]

	return matrix

# Function to return row and col of a letter in matrix
def findPosition(letter, matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if matrix[i][j] == letter:
				return [i, j]

# Function to form pairs by padding message with X if required
def formPairs(message):
	i = 0
	resMessage = ''
	while i < len(message):
		firstChar = message[i]
		secondChar = message[i+1] if i+1 < len(message) else 'X'

		if firstChar == secondChar:
			resMessage += firstChar + 'X'
			i += 1
		else:
			resMessage += firstChar + secondChar
			i += 2
	return resMessage

# Clean input message
def cleanInput(input):
	input = ''.join([c for c in input if c.isalpha()])				# Remove spaces and special characters
	input = input.upper().replace('J', 'I')							# Convert to upper case and remove J
	return input

# Decryption function
def decrypt(encryptedMessage, cipherKey):
	decryptedMessage = ""

	# Clean the inputs
	encryptedMessage = cleanInput(encryptedMessage)
	cipherKey = cleanInput(cipherKey)

	# Add X if same adjacent characters or odd length message
	encryptedMessage = formPairs(encryptedMessage)

	# Build matrix using given cipher key
	matrix = buildMatrix(cipherKey)

	for i in range(0, len(encryptedMessage), 2):
		firstChar, secondChar = encryptedMessage[i], encryptedMessage[i+1]

		[row1, col1] = findPosition(firstChar, matrix)
		[row2, col2] = findPosition(secondChar, matrix)
		
		if row1 == row2:
			decryptedMessage += (matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5])
		elif col1 == col2:
			decryptedMessage += (matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2])
		else:
			decryptedMessage += (matrix[row1][col2] + matrix[row2][col1])
	
	# Remove occurrences of X from decrypted message, there can be no space or special characters
	decryptedMessage = decryptedMessage.replace('X', '')
	
	return decryptedMessage

def main():
	encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	cipherKey = "SUPERSPY"
	
	print(decrypt(encryptedMessage, cipherKey))

if __name__ == "__main__":
	main()

# Thanks!