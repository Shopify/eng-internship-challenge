package main

import (
	"strings"
)

// First, we need a function to create the table.
// Instead of having a 2D array, we can just use a 1D array and calculate the index of the element in the 2D array.
func createKeyTable(key string) [25]rune {
	alphabet := "ABCDEFGHIKLMNOPQRSTUVWXYZ" // J is removed
	key = strings.ToUpper(key)              //makes sure all the characters are uppercase
	used := make(map[rune]bool)             // To keep track of the used characters
	keyTable := [25]rune{}                  // The key table
	tableIndex := 0                         // The index to keep track of the table
	// Add the characters from the key and the alphabet to the key table
	for _, c := range key + alphabet {
		if c == 'J' {
			used['I'] = true
			keyTable[tableIndex] = 'I'
			tableIndex++
		} else if !used[c] {
			used[c] = true
			keyTable[tableIndex] = c
			tableIndex++
		}
	}
	return keyTable
}

// A helper function to decrypt 2 characters
func decryptPair(c1, c2 rune, keyTable [25]rune) (rune, rune) {
	// Find the index of the characters in the key table (assuming they are not the same)
	i1, i2 := -1, -1
	for i, c := range keyTable {
		if c == c1 {
			i1 = i
		} else if c == c2 {
			i2 = i
		}
	}
	// Calculate the row and column of the characters to check if they're in the same row or column
	row1, col1 := i1/5, i1%5
	row2, col2 := i2/5, i2%5
	// If the characters are in the same row, return the characters to the left (to decrypt)
	if row1 == row2 {
		return keyTable[row1*5+(col1+4)%5], keyTable[row2*5+(col2+4)%5]
	}
	// If the characters are in the same column, return the characters above (to decrypt)
	if col1 == col2 {
		return keyTable[((row1+4)%5)*5+col1], keyTable[((row2+4)%5)*5+col2]
	}
	// If the characters are in different rows and columns,
	//	return the characters in the same row but in the other column (to decrypt)
	return keyTable[row1*5+col2], keyTable[row2*5+col1]
}

// Finally, we can decrypt any Playfair cipher text using the key and the encrypted text
func decryptPlayfairCipher(key, text string) string {
	// Create the key table from the key
	keyTable := createKeyTable(key)
	decrypted := ""
	// For each pair of characters in the text
	for i := 0; i < len(text); i += 2 {
		// Get the characters from text
		c1, c2 := rune(text[i]), rune(text[i+1])
		// Decrypt the pair of characters using the table
		d1, d2 := decryptPair(c1, c2, keyTable)
		// Add the string version of decrypted characters to the result
		decrypted += string(d1) + string(d2)
	}
	// We need to remove the X's that were added for padding
	decrypted = strings.ReplaceAll(decrypted, "X", "")

	// Return the decrypted text
	return decrypted
}

func main() {
	key := "SUPERSPY"
	text := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	decrypted := decryptPlayfairCipher(key, text)
	println(decrypted)
}
