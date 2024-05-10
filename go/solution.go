package main

import (
	"fmt"
	"unicode"
)

const (
	matrixSize = 5
)

type LetterLocation struct {
	X, Y int
}

func NewLetterLocation(x, y int) *LetterLocation {
	return &LetterLocation{
		X: x,
		Y: y,
	}

}

type PfMatrix [][]rune

func NewMatrix() PfMatrix {
	mat := make([][]rune, matrixSize)
	for i := 0; i < matrixSize; i++ {
		mat[i] = make([]rune, matrixSize)
	}
	return mat
}

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

type PfCipher struct {
	LastEmptyIdx    int
	Message         []rune
	KeywordLetters  []rune
	ExistingChars   map[rune]bool
	LettersLocation map[rune]*LetterLocation
	Matrix          PfMatrix
}

func NewPfCipher(keyword string) *PfCipher {
	if len(keyword) == 0 {
		fmt.Println("provided string must have at least one character")
		return nil
	}

	if len(keyword) > 25 {
		fmt.Println("provided string must have less than or equal to 25 characters")
		return nil
	}

	pfc := PfCipher{
		ExistingChars:   map[rune]bool{},
		LettersLocation: map[rune]*LetterLocation{},
		KeywordLetters:  make([]rune, 0, len(keyword)),
	}

	for _, char := range keyword {
		upperRune := unicode.ToUpper(char)
		_, prs := pfc.ExistingChars[upperRune]
		if prs {
			continue
		}
		pfc.ExistingChars[upperRune] = true
		pfc.KeywordLetters = append(pfc.KeywordLetters, upperRune)
	}

	return &pfc
}

func (p *PfCipher) SetUpMatrix(alphabetLetters []rune) {
	mat := NewMatrix()
	lastEmptyIdx := 0

	// KeywordLetters field has all the unique values of the keyword
	for _, char := range p.KeywordLetters {
		i := lastEmptyIdx / matrixSize
		j := lastEmptyIdx % matrixSize
		mat[i][j] = char
		p.LettersLocation[char] = NewLetterLocation(i, j)
		lastEmptyIdx++
	}

	for _, letterRune := range alphabetLetters {
		_, prs := p.ExistingChars[letterRune]
		if prs {
			continue
		}

		i := lastEmptyIdx / matrixSize
		j := lastEmptyIdx % matrixSize
		mat[i][j] = letterRune
		p.LettersLocation[letterRune] = NewLetterLocation(i, j)
		lastEmptyIdx++
	}

	p.LastEmptyIdx = lastEmptyIdx
	p.Matrix = mat
}

func (p *PfCipher) PrepareMessage(message string) {
	originalMsg := []rune(message)
	normalizedMsg := make([]rune, 0, len(originalMsg))

	// Removing any speical characters
	for _, char := range originalMsg {
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

	// Create digraphs and handle same letter situation
	finalMsg := make([]rune, 0, len(normalizedMsg))
	for i := 0; i < len(normalizedMsg); i++ {
		if i+1 < len(normalizedMsg) && normalizedMsg[i] == normalizedMsg[i+1] {
			finalMsg = append(finalMsg, normalizedMsg[i], 'X')
			i++ // skip the next since it's the same and we've added 'X'
		} else {
			finalMsg = append(finalMsg, normalizedMsg[i])
		}
	}

	// Add 'X' if odd number of runes
	if len(finalMsg)%2 != 0 {
		finalMsg = append(finalMsg, 'X')
	}

	// // Create digraphs
	// finalMsg := make([]rune, 0, len(normalizedMsg))
	// for i := 0; i < len(normalizedMsg)-1; i += 2 {
	// 	pair := normalizedMsg[i : i+2]
	// 	if pair[0] == pair[1] {
	// 		pair[1] = 'X'
	// 	}
	// 	finalMsg = append(finalMsg, pair...)
	// }

	// if len(finalMsg)%2 != 0 {
	// 	finalMsg = append(finalMsg, 'X')
	// }
	p.Message = finalMsg
}

func (p *PfCipher) extractLocationFromPair(pair []rune) (int, int, int, int) {
	firstX := p.LettersLocation[pair[0]].X
	firstY := p.LettersLocation[pair[0]].Y
	secondX := p.LettersLocation[pair[1]].X
	secondY := p.LettersLocation[pair[1]].Y
	return firstX, firstY, secondX, secondY
}

func (p *PfCipher) Encrypt(message string) string {
	p.PrepareMessage(message)
	encryptedMsg := make([]rune, 0, len(p.Message))

	for i := 0; i < len(p.Message)-1; i += 2 {
		pair := p.Message[i : i+2]
		firstX, firstY, secondX, secondY := p.extractLocationFromPair(pair)

		if firstX == secondX {
			firstY++
			secondY++

			if firstY > matrixSize-1 {
				firstY = 0
			}
			if secondY > matrixSize-1 {
				secondY = 0
			}

		} else if firstY == secondY {
			firstX++
			secondX++

			if firstX > matrixSize-1 {
				firstX = 0
			}
			if secondX > matrixSize-1 {
				secondX = 0
			}
		} else {
			firstY, secondY = secondY, firstY
		}

		encryptedMsg = append(encryptedMsg, p.Matrix[firstX][firstY])
		encryptedMsg = append(encryptedMsg, p.Matrix[secondX][secondY])
	}

	return string(encryptedMsg)
}

func (p *PfCipher) Decrypt(message string) string {
	decryptedMsg := make([]rune, 0, len(message))
	messageRune := []rune(message)

	for i := 0; i < len(messageRune)-1; i += 2 {
		pair := messageRune[i : i+2]
		firstX, firstY, secondX, secondY := p.extractLocationFromPair(pair)

		// Case of same row
		if firstX == secondX {
			// based on pf algorithm, the letter should be replace with the one to the left
			firstY--
			secondY--

			// wrap around the matrix if idx was zero
			if firstY < 0 {
				firstY = matrixSize - 1
			}
			if secondY < 0 {
				secondY = matrixSize - 1
			}

			// Case of same column
		} else if firstY == secondY {
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

	pfCipher := NewPfCipher(keyword)
	pfCipher.SetUpMatrix(alphabetLetters)

	decryptedMsg := pfCipher.Decrypt(messageToDecrypt)
	encryptedMsg := pfCipher.Encrypt(messageToEncrypt)
	fmt.Println(decryptedMsg)
	fmt.Println(encryptedMsg)
}
