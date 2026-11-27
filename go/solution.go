// Package main implements Playfair Cipher diciphering logic.
package main

import (
	"fmt"
	"strings"
)

const (
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	// Normalization
	reduceLetter     = "J"
	reduceLetterWith = "I"

	// Repeated char replacement
	uncommonLetter = byte('X')
)

// =================
// KeyTable struture
// =================

const keyTableSize = 5

// To find char, we map position (row, column) => (table[row*5 + column])
type KeyTable string

// NewKeyTable creates a new KeyTable object, based on the provided cipher key.
func NewKeyTable(key string) KeyTable {
	charOrder := normalizeInput(key + alphabet)

	// Create table while removing duplicate chars
	exists := map[byte]bool{}
	var strBuilder strings.Builder
	for i := range charOrder {
		char := charOrder[i]

		if !exists[char] {
			exists[char] = true
			strBuilder.WriteByte(char)
		}
	}

	return KeyTable(strBuilder.String())
}

// GetChar returns the letter at the provided table coordinate.
// Assumes row and column inputs are bounded by table size.
func (kt KeyTable) GetChar(row, column int) byte {
	return kt[row*keyTableSize+column]
}

// FindIndex returns (row, column) indices of the letter.
// Assumes letter exists in the table.
func (kt KeyTable) FindIndex(letter byte) (int, int) {
	index := strings.IndexByte(string(kt), letter)
	return index / keyTableSize, index % keyTableSize
}

// ============
// Main program
// ============

func main() {
	// Problem inputs
	const (
		cipherKey  = "SUPERSPY"
		encryptMsg = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	)

	// Decrypt the cipher text
	decryptMsg := DecryptPlayfairCipher(encryptMsg, cipherKey)
	fmt.Println(decryptMsg)
}

// DecryptPlayfairCipher returns an unencrypted message of an encrypted Playfair Cipher message.
func DecryptPlayfairCipher(encryptMsg, key string) string {
	// Prepare input for processing
	normKey := normalizeInput(key)
	keyTable := NewKeyTable(normKey)

	// Normalize encrypted message to cipher standards
	normEncryptMsg := normalizeInput(encryptMsg)
	if len(normEncryptMsg)%2 == 1 {
		normEncryptMsg += string(uncommonLetter)
	}

	// Process each digram pair of encrypted message
	var msgBuilder strings.Builder
	msgBuilder.Grow(len(encryptMsg)) // allocate exact memory needed

	for i := 0; i < len(normEncryptMsg); i += 2 {
		// Find position of pair chars
		c1Val := normEncryptMsg[i]
		c2Val := normEncryptMsg[i+1]

		c1Row, c1Col := keyTable.FindIndex(c1Val)
		c2Row, c2Col := keyTable.FindIndex(c2Val)

		// Apply reverse of encryption rules
		if c1Row == c2Row {
			// reverse rule #2 => if chars in same row, replaced with chars to the left
			msgBuilder.WriteByte(keyTable.GetChar(c1Row, (c1Col+keyTableSize-1)%keyTableSize))
			msgBuilder.WriteByte(keyTable.GetChar(c2Row, (c2Col+keyTableSize-1)%keyTableSize))
		} else if c1Col == c2Col {
			// reverse rule #3 => if chars appear in the same column, replaced with chars immediately above
			msgBuilder.WriteByte(keyTable.GetChar((c1Row+keyTableSize-1)%keyTableSize, c1Col))
			msgBuilder.WriteByte(keyTable.GetChar((c2Row+keyTableSize-1)%keyTableSize, c2Col))
		} else {
			// reverse rule #4: if chars not in same row/col, replace with rectangle corner
			msgBuilder.WriteByte(keyTable.GetChar(c1Row, c2Col))
			msgBuilder.WriteByte(keyTable.GetChar(c2Row, c1Col))
		}
	}

	// reverse rule #1: remove any uncommon ('X') letters
	return strings.ReplaceAll(msgBuilder.String(), string(uncommonLetter), "")
}

// normalizeInput returned normalized provided string according to Playfair Cipher's conventions.
// - "usually ommiting 'J'" => remove all 'J'.
// - do not consider letters' case => normalize all to upper-case.
func normalizeInput(input string) string {
	return strings.ToUpper(strings.ReplaceAll(input, reduceLetter, ""))
}
