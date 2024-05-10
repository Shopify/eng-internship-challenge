// This program will allow the user to perform Playfair Cipher given:
//   - keyword as a secret to this algorithm
//   - message to be encrypted or decrypted

package main

import (
	"fmt"
	"strings"
	"unicode"
)

// Size of the matrix for Playfair Cipher
// Both for rows and cols
const (
	matrixSize       = 5
	matrixValidBound = matrixSize - 1
)

// Define a custom type for the matrix of algorithm
type PfMatrix [][]rune

// Tracks the location of each letter by storing its row and col
type LetterLocation struct {
	X, Y int
}

func NewLetterLocation(x, y int) *LetterLocation {
	return &LetterLocation{
		X: x,
		Y: y,
	}
}

// If the given rune is space, digit, a puncuation, or a symbol, it will return false.
// This is to remove the speical characters in the input message
func IsInvalidRune(r rune) bool {
	return unicode.IsSpace(r) || unicode.IsDigit(r) || unicode.IsPunct(r) || unicode.IsSymbol(r)
}

// To check if J exists in the user message for encryption
// so it will be replaced by I based on Playfair Cipher rules
func IsRuneJ(r rune) bool {
	return r == 'J'
}

// This is to exclude the unacceptable runes for the final slice or rune
// since the instructions specifically asks for this
func IsValidForDecrypted(r rune) bool {
	if IsInvalidRune(r) {
		return false
	}
	return r != 'X'
}

// PfCipher holds all the necessary information for Playfair Cipher
type PfCipher struct {
	// Last index to be filled by the rest of the alphabet
	// after embedding the keyword in the matrix
	LastEmptyIdx int

	// Holds a modified version of the message that needs to be
	// encrypted.
	Message []rune

	// Contains all the unique letters of keyword
	UniqueKeywordLetters []rune

	// Map that acts as a set to keep track of the keyword letters
	// and to be able to find the unqiue values
	UniqueKeywordLettersSet map[rune]bool

	// Location (row and col) of every letter in the matrix
	LettersLocation map[rune]*LetterLocation

	// Playfair cipher matrix that holds the keyword and rest of the alphabet
	// with the condition that there is no 'J' and all the letters unique
	Matrix PfMatrix
}

// Starting a new cipher struct to be able to encrypt or decrypt the
// user's message
func NewPfCipher() *PfCipher {
	return &PfCipher{
		UniqueKeywordLettersSet: map[rune]bool{},
		LettersLocation:         map[rune]*LetterLocation{},
		LastEmptyIdx:            0,
	}

}

// Initializes a 5*5 matrix for Playfair Cipher. This will be
// filled with the keyword and the remaining words of the english
// alphabet that did not exist in keyword
func (p *PfCipher) newMatrix() {
	mat := make([][]rune, matrixSize)
	for i := 0; i < matrixSize; i++ {
		mat[i] = make([]rune, matrixSize)
	}
	p.Matrix = mat
}

// Ensures the provided keyword by the user is valid for
// Playfair Cipher algorithm.
func (p *PfCipher) validateKeyword(keyword string) error {
	keyword = strings.TrimSpace(keyword)
	if len(keyword) == 0 {
		return fmt.Errorf("provided keyword must have at least one character")
	}
	if len(keyword) > 25 {
		return fmt.Errorf("provided keyword must have less than or equal to 25 characters")
	}

	// handling digits and special characters
	for _, char := range keyword {
		if IsInvalidRune(char) {
			return fmt.Errorf("provided keyword must not contain special chars but found %v", char)
		}
	}

	return nil
}

// Finds the unique letters in the keyword provided by the user
// since Playfair Cipher needs to be filled row by row based on these
// unique letters
func (p *PfCipher) findUniqueKeywordLetters(keyword string) {
	p.UniqueKeywordLetters = make([]rune, 0, len(keyword))

	for _, char := range keyword {
		upperRune := unicode.ToUpper(char)
		_, prs := p.UniqueKeywordLettersSet[upperRune]
		if prs {
			continue
		}
		p.UniqueKeywordLettersSet[upperRune] = true
		p.UniqueKeywordLetters = append(p.UniqueKeywordLetters, upperRune)
	}
}

// After receving a pair of runes (digraphs), it returns the row and col of
// each rune
func (p *PfCipher) extractLocationFromPair(pair []rune) (int, int, int, int) {
	firstX := p.LettersLocation[pair[0]].X
	firstY := p.LettersLocation[pair[0]].Y
	secondX := p.LettersLocation[pair[1]].X
	secondY := p.LettersLocation[pair[1]].Y
	return firstX, firstY, secondX, secondY
}

// Returns a slice of rune of all the uppercase letter of english
// alphabet excluding J based on the rules of Playfair Cipher
func (p *PfCipher) getAlphabetLettersWihtoutJ() []rune {
	letters := make([]rune, 0, 25)
	for ch := 'A'; ch <= 'Z'; ch++ {
		if ch == 'J' {
			continue
		}
		letters = append(letters, ch)
	}
	return letters
}

// Sets up the Playfair Cipher matrix using the provided keyword
func (p *PfCipher) SetUpMatrix(keyword string) error {
	// keyword preparation
	alphabetLetters := p.getAlphabetLettersWihtoutJ()
	if err := p.validateKeyword(keyword); err != nil {
		return err
	}
	p.findUniqueKeywordLetters(keyword)

	// Setting up the matrix
	p.newMatrix()

	// First, filling the matrix row by row with the unique
	// runes from keyword
	for _, char := range p.UniqueKeywordLetters {
		i := p.LastEmptyIdx / matrixSize
		j := p.LastEmptyIdx % matrixSize
		p.Matrix[i][j] = char
		p.LettersLocation[char] = NewLetterLocation(i, j)
		p.LastEmptyIdx++
	}

	// Fill the rest of the matrix with the remaining letters of alphabet
	// that does not exist in keyword
	for _, letterRune := range alphabetLetters {
		_, prs := p.UniqueKeywordLettersSet[letterRune]
		if prs {
			continue
		}
		i := p.LastEmptyIdx / matrixSize
		j := p.LastEmptyIdx % matrixSize
		p.Matrix[i][j] = letterRune
		p.LettersLocation[letterRune] = NewLetterLocation(i, j)
		p.LastEmptyIdx++
	}

	return nil
}

// Prepare the message for encryption. It gets rid of the special
// characters and letter 'J'. Then, each rune becomes uppercase.
// Finally, the repeated letters are dealt with using a filler 'X'
// and if the length of the []rune was not even, another 'X' gets added
// to the end of the message
func (p *PfCipher) prepareMessage(message string) {
	originalMsg := []rune(message)
	normalizedMsg := make([]rune, 0, len(originalMsg))

	for _, char := range originalMsg {
		// Removing any speical characters
		if IsInvalidRune(char) {
			fmt.Printf("invalid char:\t%v\n", char)
			continue
		}
		// Based on pf algorithm, if a letter is J, should be replaced by I
		if IsRuneJ(char) {
			normalizedMsg = append(normalizedMsg, 'I')
			continue
		}
		normalizedMsg = append(normalizedMsg, unicode.ToUpper(char))
	}

	// Create digraphs and handle same letter issue
	finalMsg := make([]rune, 0, len(normalizedMsg))
	i := 0
	for i < len(normalizedMsg) {
		if i+1 < len(normalizedMsg) && normalizedMsg[i] == normalizedMsg[i+1] {
			// If the pair has a repeating letter, add a filling 'X' and for the
			// the next iteration, we increment by one since 'X' caused a pair
			finalMsg = append(finalMsg, normalizedMsg[i], 'X')
			i++

		} else if i+1 < len(normalizedMsg) {
			// In case of no repetition, append the pair to the slice and increment
			// by 2 since this pair is done and we're moving forward to the next pair
			finalMsg = append(finalMsg, normalizedMsg[i], normalizedMsg[i+1])
			i += 2

		} else {
			// If it has odd number of characters, add 'X' to the end
			finalMsg = append(finalMsg, normalizedMsg[i], 'X')
			i++
		}
	}
	p.Message = finalMsg
}

// Encrypts the provided message.
//
// The message must not contains any special characters or spaces
// in the middle of string.
func (p *PfCipher) Encrypt(message string) string {
	p.prepareMessage(message)
	encryptedMsg := make([]rune, 0, len(p.Message))

	for i := 0; i < len(p.Message)-1; i += 2 {
		pair := p.Message[i : i+2]
		firstX, firstY, secondX, secondY := p.extractLocationFromPair(pair)

		// if two letters/runes are on the same row
		if firstX == secondX {
			// The letter should be replaced by the one to the right
			// adding one to col index to achieve this
			firstY++
			secondY++
			if firstY > matrixValidBound {
				firstY = 0
			}
			if secondY > matrixValidBound {
				secondY = 0
			}

			// if two letters/runes are on the same col
		} else if firstY == secondY {
			// Letter should be replaced by the one at the bottom
			// adding one to the row to achieve this
			firstX++
			secondX++
			if firstX > matrixValidBound {
				firstX = 0
			}
			if secondX > matrixValidBound {
				secondX = 0
			}

			// In case of rectangle formation
		} else {
			firstY, secondY = secondY, firstY
		}

		encryptedMsg = append(encryptedMsg, p.Matrix[firstX][firstY])
		encryptedMsg = append(encryptedMsg, p.Matrix[secondX][secondY])
	}

	return string(encryptedMsg)
}

// Decrypts the provided message based on the keyword
// passed to the PfCipher struct
func (p *PfCipher) Decrypt(message string) string {
	decryptedMsg := make([]rune, 0, len(message))
	messageRune := []rune(message)

	for i := 0; i < len(messageRune)-1; i += 2 {
		pair := messageRune[i : i+2]
		firstX, firstY, secondX, secondY := p.extractLocationFromPair(pair)

		// if two letters/runes are on the same row
		if firstX == secondX {
			// based on pf algorithm, the letter should be replaced with the one to the left
			// we shift one the left
			firstY--
			secondY--

			// wrap around the matrix if idx was zero
			if firstY < 0 {
				firstY = matrixValidBound
			}
			if secondY < 0 {
				secondY = matrixValidBound
			}

			// if two letters/runes are on the same col
		} else if firstY == secondY {
			// The letter should be replaced with the one at the top
			// we deduct one from the row idx
			firstX--
			secondX--

			// wrap around the matrix if idx was zero
			if firstX < 0 {
				firstX = matrixValidBound
			}
			if secondX < 0 {
				secondX = matrixValidBound
			}

			// Case of Rectangle formation
		} else {
			// We assign the column of the second letter to the first one and vice versa
			firstY, secondY = secondY, firstY
		}

		if IsValidForDecrypted(p.Matrix[firstX][firstY]) {
			decryptedMsg = append(decryptedMsg, p.Matrix[firstX][firstY])
		}
		if IsValidForDecrypted(p.Matrix[secondX][secondY]) {
			decryptedMsg = append(decryptedMsg, p.Matrix[secondX][secondY])
		}
	}
	return string(decryptedMsg)
}

func main() {
	keyword := "SUPERSPY"
	// messageToEncrypt := "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
	messageToDecrypt := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

	pfCipher := NewPfCipher()
	pfCipher.SetUpMatrix(keyword)
	decryptedMsg := pfCipher.Decrypt(messageToDecrypt)
	fmt.Println(decryptedMsg)
}
