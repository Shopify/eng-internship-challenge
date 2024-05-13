package main

import (
	"fmt"
	"strings"
)

const (
	SIZE = 5
)

type PlayfairCipher struct {
	Message         string
	Keyword         string
	LettersPosition map[rune]*LetterPosition
	Matrix          PlayfairMatrix
}

type PlayfairMatrix [][]rune

// row, col for each letter
type LetterPosition struct {
	X, Y int
}

func NewLetterPositon(x, y int) *LetterPosition {
	return &LetterPosition{
		X: x,
		Y: y,
	}
}

// creates a new PlayfairCipher instance and populates the matrix and letter locations
func NewPlayfairCipher(msg, kw string) (*PlayfairCipher, error) {
	msg = strings.ToUpper(msg)
	kw = strings.ToUpper(kw)
	cipher := &PlayfairCipher{
		Message:         msg,
		Keyword:         kw,
		LettersPosition: make(map[rune]*LetterPosition),
		Matrix:          createEmptyMatrix(),
	}
	if err := cipher.validateInput(); err != nil {
		return nil, err
	}
	cipher.populateMatrix()
	cipher.populateLetterPositions()
	return cipher, nil
}

// initializes an empty Playfair matrix
func createEmptyMatrix() PlayfairMatrix {
	matrix := make(PlayfairMatrix, SIZE)
	for i := range matrix {
		matrix[i] = make([]rune, SIZE)
	}
	return matrix
}

// ensures the cipherText and keyword are of valid lengths
func (p *PlayfairCipher) validateInput() error {
	if len(p.Message) == 0 || len(p.Message)%2 != 0 {
		return fmt.Errorf("cipher text length must be even and non zero length")
	}
	if len(p.Keyword) == 0 || len(p.Keyword) > 25 {
		return fmt.Errorf("keyword length must be between 1 and 25 characters")
	}
	return nil
}

// fills the Playfair matrix with the keyword and remaining alphabet letters
func (p *PlayfairCipher) populateMatrix() {
	used := make(map[rune]bool)
	row, col := 0, 0

	for _, char := range p.Keyword {
		if char == 'J' {
			char = 'I'
		}
		if !used[char] && char >= 'A' && char <= 'Z' {
			used[char] = true
			p.Matrix[row][col] = char
			col++
			if col == SIZE {
				row++
				col = 0
			}
		}
	}

	for char := 'A'; char <= 'Z'; char++ {
		if char == 'J' {
			continue
		}
		if !used[char] {
			p.Matrix[row][col] = char
			col++
			if col == SIZE {
				row++
				col = 0
			}
		}
	}
}

// creates a mapping of each letter to its location in the matrix
func (p *PlayfairCipher) populateLetterPositions() {
	for r := 0; r < SIZE; r++ {
		for c := 0; c < SIZE; c++ {
			char := p.Matrix[r][c]
			p.LettersPosition[char] = NewLetterPositon(r, c)
		}
	}
}

// removes 'X', spaces and special characters from the input text
func (p *PlayfairCipher) cleanText(input string) string {
	input = strings.ReplaceAll(input, "X", "")
	input = strings.ReplaceAll(input, " ", "")
	return strings.Map(func(r rune) rune {
		if r >= 'A' && r <= 'Z' {
			return r
		}
		return -1
	}, input)
}

// decrypts the ciphertext using the Playfair cipher
func (p *PlayfairCipher) decrypt() string {
	var plainText string
	cipherText := p.Message

	for i := 0; i < len(cipherText); i += 2 {
		char1 := rune(cipherText[i])
		char2 := rune(cipherText[i+1])
		pos1 := p.LettersPosition[char1]
		pos2 := p.LettersPosition[char2]

		// check for same row
		if pos1.X == pos2.X {
			char1 = p.Matrix[pos1.X][(pos1.Y-1+SIZE)%SIZE]
			char2 = p.Matrix[pos2.X][(pos2.Y-1+SIZE)%SIZE]
		} else if pos1.Y == pos2.Y { // check for same column
			char1 = p.Matrix[(pos1.X-1+SIZE)%SIZE][pos1.Y]
			char2 = p.Matrix[(pos2.X-1+SIZE)%SIZE][pos2.Y]
		} else { // rectangle
			char1 = p.Matrix[pos1.X][pos2.Y]
			char2 = p.Matrix[pos2.X][pos1.Y]
		}

		plainText += string(char1) + string(char2)
	}
	plainText = p.cleanText(plainText)
	return plainText
}

func main() {
	cipherText := "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
	key := "SUPERSPY"

	pfCipher, err := NewPlayfairCipher(cipherText, key)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	plainText := pfCipher.decrypt()

	fmt.Println(plainText)
}
