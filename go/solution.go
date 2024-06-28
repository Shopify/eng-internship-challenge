package main

import (
	"fmt"
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
		if !used[c] {
			used[c] = true
			keyTable[tableIndex] = c
			tableIndex++
		}
	}
	return keyTable
}

func main() {
	hi := createKeyTable("HELLO")
	for _, c := range hi {
		fmt.Printf("%c ", c)
	}
}
