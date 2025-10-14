package main

import (
	"fmt"
	"strings"
)

// Matrix creates a 5x5 matrix for the Playfair cipher
func Matrix(chavi string) [5][5]rune {
	chavi = strings.ToUpper(chavi)
	used := make(map[rune]bool)
	var matrix [5][5]rune
	row, col := 0, 0

	// Add key characters to the matrix
	for _, char := range chavi {
		if char == 'J' {
			char = 'I'
		}
		if !used[char] {
			matrix[row][col] = char
			used[char] = true
			col++
			if col == 5 {
				col = 0
				row++
			}
		}
	}

	// Add remaining characters to the matrix
	for char := 'A'; char <= 'Z'; char++ {
		if char == 'J' {
			continue
		}
		if !used[char] {
			matrix[row][col] = char
			used[char] = true
			col++
			if col == 5 {
				col = 0
				row++
			}
		}
	}
	return matrix
}

// FindPosition finds the row and column of a character in the matrix
func PositionLookUp(matrix [5][5]rune, char rune) (int, int) {
	if char == 'J' {
		char = 'I'
	}
	// Find the character in the matrix and return its position	
	for row := range matrix {
		for col := range matrix[row] {
			if matrix[row][col] == char {
				return row, col
			}
		}
	}
	return -1, -1
}

// DecryptPair decrypts a pair of characters using the Playfair cipher
func EncodePair(matrix [5][5]rune, char1, char2 rune) (rune, rune) {
	row1, col1 := PositionLookUp(matrix, char1)
	row2, col2 := PositionLookUp(matrix, char2)

	if row1 == row2 {
		col1 = (col1 + 4) % 5
		col2 = (col2 + 4) % 5
	} else if col1 == col2 {
		row1 = (row1 + 4) % 5
		row2 = (row2 + 4) % 5
	} else {
		col1, col2 = col2, col1
	}

	return matrix[row1][col1], matrix[row2][col2]
}

// DecryptPlayfair decrypts a message using the Playfair cipher
func decodePlayfair(matrix [5][5]rune, message string) string {
	message = strings.ToUpper(message)
	message = strings.ReplaceAll(message, " ", "")
	var decrypted []rune
	// Process pairs of characters in the message
	for i := 0; i < len(message); i += 2 {
		char1 := rune(message[i])
		char2 := rune(message[i+1])

		if char1 == 'X' {
			char1 = 'X'
		}
		if char2 == 'X' {
			char2 = 'X'
		}

		decryptedChar1, decryptedChar2 := EncodePair(matrix, char1, char2)
		decrypted = append(decrypted, decryptedChar1, decryptedChar2)
	}

	return string(decrypted)
}

func main() {
	key := "SUPERSPY"
	message := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

	matrix := Matrix(key)
	decryptedMessage := decodePlayfair(matrix, message)

	// Remove 'X' and output the result
	decryptedMessage = strings.ReplaceAll(decryptedMessage,"X", "")
	fmt.Println(decryptedMessage)
}
