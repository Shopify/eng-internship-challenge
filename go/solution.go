package main

import (
	"fmt"
	"strings"
)

const (
	Size = 5
)

func createKeySquare(key string) [Size][Size]rune {
	var square [Size][Size]rune
	used := make(map[rune]bool)
	row, col := 0, 0

	// add the key to the square
	for _, char := range strings.ToUpper(key) {
		if char == 'J' { //'J' is merged with 'I'
			char = 'I'
		}
		if !used[char] && char >= 'A' && char <= 'Z' {
			used[char] = true
			square[row][col] = char
			col++
			if col == Size {
				row++
				col = 0
			}
		}
	}

	// fill remaining spaces in the square
	for char := 'A'; char <= 'Z'; char++ {
		if char == 'J' { // Skip 'J'
			continue
		}
		if !used[char] {
			square[row][col] = char
			col++
			if col == Size {
				row++
				col = 0
			}
		}
	}

	return square
}

func cleanText(input string) string {
	input = strings.ReplaceAll(input, "X", "")
	input = strings.ReplaceAll(input, " ", "")
	return strings.Map(func(r rune) rune {
		if r >= 'A' && r <= 'Z' {
			return r
		}
		return -1
	}, input)
}

func decryptPlayfair(cipherText, key string) string {
	square := createKeySquare(key)
	mapping := make(map[rune][2]int)
	// precompute positions in map
	for r := 0; r < Size; r++ {
		for c := 0; c < Size; c++ {
			mapping[square[r][c]] = [2]int{r, c}
		}
	}

	var plainText string
	cipherText = strings.ToUpper(cipherText)
	// decrypt digraphs
	for i := 0; i < len(cipherText); i += 2 {
		char1 := rune(cipherText[i])
		char2 := rune(cipherText[i+1])
		pos1 := mapping[char1]
		pos2 := mapping[char2]

		// check if same row
		if pos1[0] == pos2[0] {
			char1 = square[pos1[0]][(pos1[1]-1+Size)%Size]
			char2 = square[pos2[0]][(pos2[1]-1+Size)%Size]
		} else if pos1[1] == pos2[1] { // check if same column
			char1 = square[(pos1[0]-1+Size)%Size][pos1[1]]
			char2 = square[(pos2[0]-1+Size)%Size][pos2[1]]
		} else { // rectangle
			char1 = square[pos1[0]][pos2[1]]
			char2 = square[pos2[0]][pos1[1]]
		}

		plainText += string(char1) + string(char2)
	}
	plainText = cleanText(plainText)
	return plainText
}

func main() {
	cipherText := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	key := "SUPERSPY"
	plainText := decryptPlayfair(cipherText, key)
	fmt.Println(plainText)
}
