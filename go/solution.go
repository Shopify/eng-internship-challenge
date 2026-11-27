package main

import (
	"fmt"
)

// removeDuplicates removes duplicates from the string and returns a new string
func removeDuplicates(s string) string {
	seen := make(map[rune]struct{})
	var result []rune
	for _, char := range s {
		if _, exists := seen[char]; !exists {
			seen[char] = struct{}{}
			result = append(result, char)
		}
	}
	return string(result)
}

// createMatrix sets up a 5x5 Playfair cipher matrix using a given key
func createMatrix(encryptedMessage string) [][]rune {
	noDuplicatesEncryptedMessage := removeDuplicates(encryptedMessage)
	noDuplicatesEncryptedMessageFinal := removeDuplicates(noDuplicatesEncryptedMessage + "ABCDEFGHIKLMNOPQRSTUVWXYZ") //creating the input for the matrix

	// Matrix size is set to 5x5 for Playfair
	const size = 5
	matrix := make([][]rune, size)
	for i := range matrix {
		matrix[i] = make([]rune, size)
	}

	messageIndex := 0
	// Fill the matrix with the chars
	for i := 0; i < size; i++ {
		for j := 0; j < size; j++ {
			if messageIndex >= len(noDuplicatesEncryptedMessageFinal) {
				break
			}
			matrix[i][j] = rune(noDuplicatesEncryptedMessageFinal[messageIndex])
			messageIndex++
		}
	}
	return matrix
}

// finds location of letter, I realized I couldve converted them to numbers and searched with a quicker runtime then reverse them back but its too late now.
func findPosition(char rune, matrix [][]rune) (int, int) {
	for x, row := range matrix {
		for y, matrixChar := range row {
			if matrixChar == char {
				return x, y
			}
		}
	}
	return -1, -1 // Not found (should not happen)
}

func decodeMessage(matrix [][]rune, secretKey []string) string {
	decodedMessage := ""

	for _, pair := range secretKey {
		char1, char2 := rune(pair[0]), rune(pair[1])
		x1, y1 := findPosition(char1, matrix)
		x2, y2 := findPosition(char2, matrix)
		if x1 == -1 || x2 == -1 { // Check if characters were found in the matrix
			continue
		}

		if x1 == x2 {
			// row rule : Shift left
			decodedMessage += string(matrix[x1][(y1+4)%5]) // +4 to handle negative index on modulo operation
			decodedMessage += string(matrix[x2][(y2+4)%5])
		} else if y1 == y2 {
			// column rule: Shift up
			decodedMessage += string(matrix[(x1+4)%5][y1])
			decodedMessage += string(matrix[(x2+4)%5][y2])
		} else {
			// Rectangle rule: Swap columns
			decodedMessage += string(matrix[x1][y2])
			decodedMessage += string(matrix[x2][y1])
		}
	}
	//checks if chars behind and in front of X are the same, if so remove them
	for i := 1; i < len(decodedMessage)-1; i++ {
		if decodedMessage[i-1] == decodedMessage[i+1] && decodedMessage[i] == 'X' {
			decodedMessage = decodedMessage[:i] + decodedMessage[i+1:]
		}
	}
	//checks if len is odd and last char is X, if so removes it
	if len(decodedMessage)%2 != 0 && decodedMessage[len(decodedMessage)-1] == 'X' {
		decodedMessage = decodedMessage[:len(decodedMessage)-1]
	}

	return decodedMessage

}

// getting message ready for ciphering
func formatForPlayfair(input string) []string {
	var pairs []string

	// Handle pairs and duplicates
	i := 0
	for i < len(input) {
		if i+1 < len(input) && input[i] == input[i+1] {
			pairs = append(pairs, string(input[i])+"X") // Append 'X' to deal with duplicate
			i++
		} else if i+1 < len(input) {
			pairs = append(pairs, input[i:i+2]) // Append normal pair
			i += 2
		} else {
			break // Break if no more characters to process
		}
	}

	// Check if the last character needs pairing
	if i < len(input) {
		pairs = append(pairs, string(input[i])+"X") // Add X to end to create pair
	}
	return pairs
}

func main() {
	secretKey := formatForPlayfair("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")
	encryptedMessage := "SUPERSPY"
	matrix := createMatrix(encryptedMessage)
	message := decodeMessage(matrix, secretKey)
	fmt.Println(message)
}
