const KEY_TABLE_WIDTH = 5
const KEY_TABLE_HEIGHT = 5

const message: string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const cipher: string = "SUPERSPY";

// Generate key table
const keys: string[] = [...new Set(`${cipher}ABCDEFGHIKLMNOPQRSTUVWXYZ`.split(""))] // JS Sets retain order

let keyTable: string[][] = []
let row: string[] = []

for (const letter of keys) {    
    row.push(letter)
    if (row.length === KEY_TABLE_WIDTH) {
        keyTable.push(row)
        row = []
    }
}

// Tokenize message
let tokens: string[] = []
for (let i = 0; i < message.length; i += 2) {
    tokens.push(message.substring(i, i + 2))
}

// Decrypt message
let res: string[] = [] 
for (const token of tokens) {
    const letter1 = token.charAt(0)
    const letter2 = token.charAt(1)

    // Get positions of each letter 
    let [row1, col1, row2, col2] = [0, 0, 0, 0]
    for (let i = 0; i < KEY_TABLE_HEIGHT; i ++) {
        if (keyTable[i].indexOf(letter1) > -1) {
            row1 = i
            col1 = keyTable[i].indexOf(letter1)
        }

        if (keyTable[i].indexOf(letter2) > -1) {
            row2 = i
            col2 = keyTable[i].indexOf(letter2)
        }
    }

    // Get new letters based on Playfair decryption rules
    let newLetter1 = ""
    let newLetter2 = ""
    if (letter1 === letter2) {
        newLetter1 = letter1
    } else if (col1 === col2) {
        // JavaScript modulo returns negative numbers for negative inputs so we first offset to a positive number 
        newLetter1 = keyTable[(row1 - 1 + KEY_TABLE_HEIGHT) % KEY_TABLE_HEIGHT][col1]
        newLetter2 = keyTable[(row2 - 1 + KEY_TABLE_HEIGHT) % KEY_TABLE_HEIGHT][col2]
    } else if (row1 === row2) {
        newLetter1 = keyTable[row1][(col1 - 1 + KEY_TABLE_WIDTH) % KEY_TABLE_WIDTH]
        newLetter2 = keyTable[row2][(col2 - 1 + KEY_TABLE_WIDTH) % KEY_TABLE_WIDTH]
    } else {
        newLetter1 = keyTable[row1][col2]
        newLetter2 = keyTable[row2][col1]
    }

    // Check to exclude Xs before pushing result
    res.push(`${newLetter1 === 'X' ? '' : newLetter1}${newLetter2 === 'X' ? '' : newLetter2}`)
}

console.log(res.join(""))