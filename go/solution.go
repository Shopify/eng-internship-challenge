package main

import (
	"fmt"
	"strings"
)

func createGrid(key string) [][]rune {
	alphabet := "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	seen := make(map[rune]bool)
	var matrix []rune

	// Process the key
	key = strings.ReplaceAll(strings.ToUpper(key), "J", "I")
	for _, ch := range key {
		if !seen[ch] && strings.ContainsRune(alphabet, ch) {
			seen[ch] = true
			matrix = append(matrix, ch)
		}
	}

	// Populate the Grid
	for _, ch := range alphabet {
		if !seen[ch] {
			matrix = append(matrix, ch)
		}
	}

	// Create grid
	grid := make([][]rune, 5)
	for i := range grid {
		grid[i] = matrix[i*5 : (i+1)*5]
	}
	return grid
}

func mapPositions(grid [][]rune) map[rune][2]int {
	posMap := make(map[rune][2]int)
	for i, row := range grid {
		for j, char := range row {
			posMap[char] = [2]int{i, j}
		}
	}
	return posMap
}

func decryptPairs(grid [][]rune, text string) string {
	posMap := mapPositions(grid)
	var result strings.Builder

	for i := 0; i < len(text); i += 2 {
		pos1 := posMap[rune(text[i])]
		pos2 := posMap[rune(text[i+1])]

		switch {
		case pos1[0] == pos2[0]: // Row Check
			result.WriteRune(grid[pos1[0]][(pos1[1]+4)%5])
			result.WriteRune(grid[pos2[0]][(pos2[1]+4)%5])
		case pos1[1] == pos2[1]: // Col Check
			result.WriteRune(grid[(pos1[0]+4)%5][pos1[1]])
			result.WriteRune(grid[(pos2[0]+4)%5][pos2[1]])
		default: // Rectangle Check
			result.WriteRune(grid[pos1[0]][pos2[1]])
			result.WriteRune(grid[pos2[0]][pos1[1]])
		}
	}

	return result.String()
}

func playfairDecrypt(key, text string) string {
	if len(text)%2 != 0 {
		text += "X"
	}
	grid := createGrid(key)
	decrypted := decryptPairs(grid, text)

	// Clean up message
	decrypted = strings.ReplaceAll(decrypted, "X", "")
	decrypted = strings.ToUpper(strings.Map(func(r rune) rune {
		if strings.ContainsRune(" `~!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?", r) {
			return -1
		}
		return r
	}, decrypted))

	return decrypted
}

func main() {
	fmt.Println(playfairDecrypt("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"))
}
