package main

import (
	"fmt"
	"unicode"
)

// Size of the matrix for Playfair Cipher
// Both for rows and cols
const (
	matrixSize = 5
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

/*
Utils
*/
// If the given rune is space, digit, a puncuation, or a symbol, it will return false.
// This is to remove the speical characters in the input message
func IsInvalidRune(r rune) bool {
	return unicode.IsSpace(r) || unicode.IsDigit(r) || unicode.IsPunct(r) || unicode.IsSymbol(r)
}

func IsRuneJ(r rune) bool {
	return r == 'J'
}

func IsValidForDecrypted(r rune) bool {
	if IsInvalidRune(r) {
		return false
	}
	return r != 'X'
}

func GetAlphabetLettersWihtoutJ() []rune {
	letters := make([]rune, 0, 25)
	for ch := 'A'; ch <= 'Z'; ch++ {
		if ch == 'J' {
			continue
		}
		letters = append(letters, ch)
	}
	return letters
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

func (p *PfCipher) newMatrix() {
	mat := make([][]rune, matrixSize)
	for i := 0; i < matrixSize; i++ {
		mat[i] = make([]rune, matrixSize)
	}
	p.Matrix = mat
}

func (p *PfCipher) validateKeyword(keyword string) error {
	if len(keyword) == 0 {
		return fmt.Errorf("provided string must have at least one character")
	}
	if len(keyword) > 25 {
		return fmt.Errorf("provided string must have less than or equal to 25 characters")
	}
	return nil
}

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

// Sets up the Playfair Cipher matrix using the provided keyword
func (p *PfCipher) SetUpMatrix(keyword string, alphabetLetters []rune) error {
	if err := p.validateKeyword(keyword); err != nil {
		return err
	}
	p.findUniqueKeywordLetters(keyword)

	p.newMatrix()
	// KeywordLetters field has all the unique values of the keyword
	for _, char := range p.UniqueKeywordLetters {
		i := p.LastEmptyIdx / matrixSize
		j := p.LastEmptyIdx % matrixSize
		p.Matrix[i][j] = char
		p.LettersLocation[char] = NewLetterLocation(i, j)
		p.LastEmptyIdx++
	}

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

// Encrypts the provided message
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

			if firstY > matrixSize-1 {
				firstY = 0
			}
			if secondY > matrixSize-1 {
				secondY = 0
			}

			// if two letters/runes are on the same col
		} else if firstY == secondY {
			// Letter should be replaced by the one at the bottom
			// adding one to the row to achieve this
			firstX++
			secondX++

			if firstX > matrixSize-1 {
				firstX = 0
			}
			if secondX > matrixSize-1 {
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

// Decrypts the provdid message
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
				firstY = matrixSize - 1
			}
			if secondY < 0 {
				secondY = matrixSize - 1
			}

			// if two letters/runes are on the same col
		} else if firstY == secondY {
			// The letter should be replaced with the one at the top
			// we deduct one from the row idx
			firstX--
			secondX--

			// wrap around the matrix if idx was zero
			if firstX < 0 {
				firstX = matrixSize - 1
			}
			if secondX < 0 {
				secondX = matrixSize - 1
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
	alphabetLetters := GetAlphabetLettersWihtoutJ()
	keyword := "SUPERSPY"

	messageToEncrypt := "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
	messageToDecrypt := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

	pfCipher := NewPfCipher()
	pfCipher.SetUpMatrix(keyword, alphabetLetters)

	fmt.Println("original message: ", messageToEncrypt)
	encryptedMsg := pfCipher.Encrypt(messageToEncrypt)
	fmt.Println("encrypted: ", encryptedMsg)
	fmt.Println(encryptedMsg == messageToDecrypt)

	decryptedMsg := pfCipher.Decrypt(messageToDecrypt)
	fmt.Println(decryptedMsg)
}
