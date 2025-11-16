package main

import (
	"fmt"
	"strings"
	"unicode"
)

const gridSize = 5

// construct a 5x5 Playfair cipher grid using the provided key
func buildGrid(key string) [gridSize][gridSize]rune {
	var grid [gridSize][gridSize]rune
	extendedKey := key + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	seen := make(map[rune]bool)
	pos := 0

	for _, char := range extendedKey {
		if char == 'J' { // ommit letter J
			continue
		}
		if !seen[char] {
			seen[char] = true
			grid[pos/gridSize][pos%gridSize] = char
			pos++
			if pos == gridSize*gridSize { // end of grid
				break
			}
		}
	}

	return grid
}

// get the row and column of a character in the grid
func getPosition(grid [gridSize][gridSize]rune, char rune) (int, int) {
	for row := 0; row < gridSize; row++ {
		for col := 0; col < gridSize; col++ {
			if grid[row][col] == char {
				return row, col
			}
		}
	}
	return -1, -1
}

// decrypts a pair of characters based on their positions in the grid
func decryptPair(grid [gridSize][gridSize]rune, a, b rune) (rune, rune) {
	row1, col1 := getPosition(grid, a)
	row2, col2 := getPosition(grid, b)

	if row1 == row2 { // check row
		col1 = (col1 + 4) % gridSize
		col2 = (col2 + 4) % gridSize
	} else if col1 == col2 { // check col
		row1 = (row1 + 4) % gridSize
		row2 = (row2 + 4) % gridSize
	} else {
		col1, col2 = col2, col1
	}

	return grid[row1][col1], grid[row2][col2]
}

// use the Playfair cipher grid to decrypt ciphertext
func decryptText(ciphertext, key string) string {
	grid := buildGrid(strings.ToUpper(key))
	ciphertext = strings.ToUpper(ciphertext)
	result := ""
	length := len(ciphertext)

	for i := 0; i < length; i += 2 {
		a, b := rune(ciphertext[i]), rune(ciphertext[i+1])
		d1, d2 := decryptPair(grid, a, b)
		result += string(d1) + string(d2)
	}
	return result
}

// removes 'X', spaces, and non-letter characters from the decrypted text
func cleanDecryptedText(result string) string {
	result = strings.ReplaceAll(result, "X", "")
	result = strings.ReplaceAll(result, " ", "")
	cleanResult := strings.Builder{}
	for _, r := range result {
		if unicode.IsLetter(r) && unicode.IsUpper(r) {
			cleanResult.WriteRune(r)
		}
	}
	return cleanResult.String()
}

func main() {
	ciphertext := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	key := "SUPERSPY"
	decrypted := decryptText(ciphertext, key)
	cleanedDecrypted := cleanDecryptedText(decrypted)
	fmt.Println(cleanedDecrypted)
}
