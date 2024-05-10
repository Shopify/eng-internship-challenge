package main

import (
	"fmt"
	"strings"
)

// generate the key table
func generateTable(key string, table *[5][5]rune) {
	letterExist := make([]bool, 26)
	keyArr := []rune(key)
	index := 0
	letter := 'A'

	for i := range table {
		for j := range table {
			// ignore the repeatitive letter
			for index < len(key) && letterExist[keyArr[index]-'A'] {
				index++
			}
			if index < len(key) {
				// fill in the spaces in the table with the letters of the keyword
				table[i][j] = keyArr[index]
				letterExist[keyArr[index]-'A'] = true
				index++
			} else {
				// fill the remaining spaces with the rest of the letters in order
				for letterExist[letter-'A'] || letter == 'J' {
					letter++
				}
				table[i][j] = letter
				letter++
			}
		}
	}
}

// decrypt the message
func decryptPlayFair(message string, table [5][5]rune) string {
	msgArr := []rune(message)
	var b strings.Builder

	for i := 0; i < len(msgArr); i += 2 {
		newPair := decryptPair(msgArr[i], msgArr[i+1], table)
		b.WriteRune(newPair[0])

		// ignore the X after the first same letter or the last letter
		if newPair[1] != 'X' {
			b.WriteRune(newPair[1])
		}
	}
	return b.String()
}

// return the pair after decryption
func decryptPair(x rune, y rune, table [5][5]rune) []rune {
	xIndex := findIndex(x, table)
	yIndex := findIndex(y, table)

	if xIndex[0] != yIndex[0] && xIndex[1] != yIndex[1] {
		// rule 4: If the letters are not on the same row or column
		return []rune{table[xIndex[0]][yIndex[1]], table[yIndex[0]][xIndex[1]]}
	} else if xIndex[0] == yIndex[0] {
		// rule 2: If the letters appear on the same row of your table
		return []rune{table[xIndex[0]][(xIndex[1]+4)%5], table[yIndex[0]][(yIndex[1]+4)%5]}
	} else if xIndex[1] == yIndex[1] {
		// rule 3: If the letters appear on the same column of your table
		return []rune{table[(xIndex[0]-1)%5][xIndex[1]], table[(yIndex[0]-1)%5][yIndex[1]]}
	} else {
		// impossible: same row && same column
		return []rune{x, y}
	}
}

// return the index of the letter x in the table
func findIndex(x rune, table [5][5]rune) []int {
	// both 'I' and 'J' in the same space
	if x == 'J' {
		x = 'I'
	}

	for i := range table {
		for j := range table[i] {
			if table[i][j] == x {
				return []int{i, j}
			}
		}
	}

	return []int{-1, -1}
}

func main() {
	message := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	key := "SUPERSPY"

	var table [5][5]rune
	generateTable(key, &table)

	fmt.Println(decryptPlayFair(message, table))
}
