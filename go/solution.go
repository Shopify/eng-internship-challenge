package main

import (
	"fmt"
	"strings"
)

/*
Algorithm Breakdown:
-  Receiver constructs a 5 by 5 cipher matrix.
- Ciphertext is split into pairs of two letters or digraphs.
- Decrypt each digraph based on very specific rules based on same col, same row, or neither.

Ciphertext: "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
Even # of characters

Key: SUPERSPY => SUPERY
We remove repeated characters


Expanding on Step 1)
-> Constructing a 5x5 cipher  matrix (letter J is omitted from the table since matrix can only hold 25 alphabets)
-> Initial alphabets in the decryption key are the the first letters in the cipher matrix followed by the rest of the alphabet.
*/

// Helper function to remove any duplicates in the key
func removeDuplicates(key string) string {
	keyNoDuplicates := ""
	seen := make(map[rune]bool)
	for _, char := range key {
		if !seen[char] {
			seen[char] = true
			keyNoDuplicates += string(char)
		}
	}
	return keyNoDuplicates
}

// Helper function to construct a 5x5 Cipher Matrix. Returns a 5 by 5 rune matrix
// We fill the Cipher matrix with key and the rest of the alphabet in order omitting J (make sure if key has duplicate characters)
func constructCipherMatrix(key string) [5][5]rune {
	// declare matrix of runes
	var matrix [5][5]rune
	alphabet := "ABCDEFGHIKLMNOPQRSTUVWXYZ" // omitting J since matrix can only fit 25 letters
	seen := make(map[rune]bool)

	key = strings.ToUpper(key)               // make the key upper
	key = strings.Replace(key, "J", "I", -1) // replace every instance of J with I in the key
	key = removeDuplicates(key)              // remove duplicates in the key

	// populating matrix with key chars
	index := 0
	for _, char := range key {
		matrix[index/5][index%5] = char // column gets updated each iteration (shifting one to the right), but row gets updated after 5 chars have been appended to that row
		seen[char] = true
		index++
	}

	// populating matrix with the remaining alphabet characters
	for _, char := range alphabet {
		if !seen[char] {
			matrix[index/5][index%5] = char
			seen[char] = true
			index++
		}
	}
	return matrix
}

// Helper function to make a hashmap where key is each character in the cipher matrix and the value is the x & y coordinates
func makeCoordinatesMap(cipherMatrix [5][5]rune) map[rune][2]int {
	coordinatesMap := make(map[rune][2]int) // making the map for each char with coords i and j where they are row and col respectively
	for i, array := range cipherMatrix {
		for j, char := range array {
			coordinatesMap[char] = [2]int{i, j}
		}
	}
	return coordinatesMap
}

// Helper function to get coordinates for the target character from the coordinates map
func getCoordinates(targetChar rune, coordinatesMap map[rune][2]int) (int, int) {
	coords, ok := coordinatesMap[targetChar]
	if ok {
		return coords[0], coords[1]
	}
	fmt.Println("Character does not exist.")
	return -1, -1
}

// Helper function to make a hashmap where key is the x and y coordinates in the cipher matrix and the value is the character
func makeCharMap(cipherMatrix [5][5]rune) map[[2]int]rune {
	charMap := make(map[[2]int]rune)
	for i, array := range cipherMatrix {
		for j, char := range array {
			charMap[[2]int{i, j}] = char
		}
	}
	return charMap
}

// Helper function to get the target character given coordinates extracted from the character map
func getCharFromCoords(targetChar rune, charMap map[[2]int]rune, i int, j int) rune {
	// make map with key as coords and value as
	char, ok := charMap[[2]int{i, j}]
	if ok {
		return char
	}
	fmt.Println("Character does not exist.")
	return '0'
}

// Helper function to decrypt the cipher text given 3 rules: same row, same column, or neither. Do this for each digraph
func decryptCipherText(coordinatesMap map[rune][2]int, cipherMatrix [5][5]rune, cipherText string) string {
	decodedCipherText := ""
	for index := 1; index < len(cipherText); index += 2 {
		row1, col1 := getCoordinates(rune(cipherText[index-1]), coordinatesMap)
		row2, col2 := getCoordinates(rune(cipherText[index]), coordinatesMap)

		charMap := makeCharMap(cipherMatrix)

		if row1 == row2 { // same row, move left one (decrement col)
			// edge case it wraps around
			col1 = (col1 + 5 - 1) % 5
			col2 = (col2 + 5 - 1) % 5
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index-1]), charMap, row1, col1))
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index]), charMap, row2, col2))
		} else if col1 == col2 { // same col, move up (decrement row)
			// edge case it is at the topmost position so wraps around
			row1 = (row1 + 5 - 1) % 5
			row2 = (row2 + 5 - 1) % 5
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index-1]), charMap, row1, col1))
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index]), charMap, row2, col2))
		} else { // neither, make a rectangle, then get char in the same row for current char but the column of the complement char
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index-1]), charMap, row1, col2)) // col1 becomes col2
			decodedCipherText += string(getCharFromCoords(rune(cipherText[index]), charMap, row2, col1))   // col12 becomes col1
		}
	}
	decodedCipherText = strings.Replace(decodedCipherText, "X", "", -1) // remove any extraneous letters ('X')
	return decodedCipherText
}

// Main function where we construct our cipher matrix based on our given key then make our coordinates map then decrypt the cipher text
func main() {
	key := "SUPERSPY"
	cipherText := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	cipherMatrix := constructCipherMatrix(key)
	coordinatesMap := makeCoordinatesMap(cipherMatrix)

	decodedCipherText := decryptCipherText(coordinatesMap, cipherMatrix, cipherText)
	fmt.Println(decodedCipherText)
}
