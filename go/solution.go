package main

import (
	"fmt"
	"strings"
)

const gridLength = 5
const cipherTableOmitChar = 'J'
const cipherTableOmitReplaceChar = 'I'
const plainTextOmitChar = 'X'

func generateCipherTable(key string, table *[gridLength][gridLength]rune) {
	key = strings.ToUpper(key)
	charsUsed := make(map[rune]bool)
	pos := 0

	for _, char := range key {
		// Out of bounds check
		if pos >= gridLength*gridLength {
			break
		}
		// Interchage 'J' into 'I'
		if char == cipherTableOmitChar {
			char = cipherTableOmitReplaceChar
		}
		// Omit any previously seen characters
		if _, used := charsUsed[char]; !used {
			charsUsed[char] = true
			table[pos/gridLength][pos%gridLength] = char
			pos += 1
		}
	}

	// Represent the alphabet in decimal ASCII
	char := rune(65)
	for pos < gridLength*gridLength {
		if _, used := charsUsed[char]; !used && char != cipherTableOmitChar {
			charsUsed[char] = true
			table[pos/gridLength][pos%gridLength] = char
			pos += 1
		}
		char += 1
	}
}

func decipherCipherText(cipherText string, table *[gridLength][gridLength]rune) string {
	cipherText = strings.ToUpper(cipherText)
	var plainTextBuidler strings.Builder

	for i := 0; i < len(cipherText); i += 2 {
		fst := rune(cipherText[i])
		snd := rune(cipherText[i+1])

		fstRow, fstCol := getCharPosition(fst, table)
		sndRow, sndCol := getCharPosition(snd, table)

		if fstRow == sndRow {
			// Case 2 - Same Row
			plainTextBuidler.WriteRune(table[fstRow][(fstCol+gridLength-1)%gridLength])
			plainTextBuidler.WriteRune(table[sndRow][(sndCol+gridLength-1)%gridLength])
		} else if fstCol == sndCol {
			// Case 3 - Same Col
			plainTextBuidler.WriteRune(table[(fstRow+gridLength-1)%gridLength][fstCol])
			plainTextBuidler.WriteRune(table[(sndRow+gridLength-1)%gridLength][sndCol])
		} else {
			// Case 4 - Different Row and Col
			plainTextBuidler.WriteRune(table[fstRow][sndCol])
			plainTextBuidler.WriteRune(table[sndRow][fstCol])
		}
	}
	plainText := plainTextBuidler.String()
	plainText = strings.ReplaceAll(plainText, string(plainTextOmitChar), "")
	plainText = strings.ReplaceAll(plainText, " ", "")
	return plainText
}

func getCharPosition(char rune, table *[gridLength][gridLength]rune) (int, int) {
	for i, row := range table {
		for j, ch := range row {
			if ch == char {
				return i, j
			}
		}
	}
	return -1, -1
}

func main() {
	key := "SUPERSPY"
	message := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	var table [gridLength][gridLength]rune

	generateCipherTable(key, &table)
	plainText := decipherCipherText(message, &table)
	fmt.Println(plainText)
}
