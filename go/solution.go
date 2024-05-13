package main

import (
	"fmt"
	"strings"
)

// Function to create the Playfair key matrix from the given key
func createMatrix(key string) [5][5]rune {
	var matrix [5][5]rune
	used := make(map[rune]bool)
	key = strings.ToUpper(key)
	alphabet := "ABCDEFGHIKLMNOPQRSTUVWXYZ" // 'J' is omitted

	// Add key letters to the matrix, avoiding duplicates
	index := 0
	for _, char := range key {
		if !used[char] && char != 'J' {
			matrix[index/5][index%5] = char
			used[char] = true
			index++
		}
	}

	// Add remaining letters of the alphabet to the matrix
	for _, char := range alphabet {
		if !used[char] {
			matrix[index/5][index%5] = char
			used[char] = true
			index++
		}
	}

	return matrix
}

// Function to find the row and column of a character in the matrix
func findPosition(matrix [5][5]rune, char rune) (int, int) {
	for i := 0; i < 5; i++ {
		for j := 0; j < 5; j++ {
			if matrix[i][j] == char {
				return i, j
			}
		}
	}
	return -1, -1
}

// Function to decrypt a pair of characters using the Playfair cipher rules
func decryptPair(matrix [5][5]rune, a, b rune) (rune, rune) {
	row1, col1 := findPosition(matrix, a)
	row2, col2 := findPosition(matrix, b)

	if row1 == row2 {
		// Same row: shift to the left
		return matrix[row1][(col1+4)%5], matrix[row2][(col2+4)%5]
	} else if col1 == col2 {
		// Same column: shift up
		return matrix[(row1+4)%5][col1], matrix[(row2+4)%5][col2]
	}
	// Rectangle: swap columns
	return matrix[row1][col2], matrix[row2][col1]
}

// Function to decrypt the entire message
func decryptMessage(key, message string) string {
	matrix := createMatrix(key)
	var decrypted strings.Builder
	message = strings.ToUpper(message)

	// Decrypt in pairs
	for i := 0; i < len(message); i += 2 {
		a, b := rune(message[i]), rune(message[i+1])
		first, second := decryptPair(matrix, a, b)
		decrypted.WriteRune(first)
		decrypted.WriteRune(second)
	}

	// Convert to string and remove 'X'
	result := decrypted.String()
	result = strings.ReplaceAll(result, "X", "")
	return result
}

func main() {
	key := "SUPERSPY"
	message := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	result := decryptMessage(key, message)
	fmt.Println(result) // Output only the decrypted string
}
