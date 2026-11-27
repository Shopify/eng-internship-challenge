function initializeMatrixVals(key) {
    // if the key contains J, clean it. only include I to standardize matrix
    const keyArray = key.toUpperCase().split('')
    for (let i = 0; i < keyArray.length; i++) {
        if (keyArray[i] == 'J') {
            keyArray[i] = 'I'
        }
    }

    // create a set for unique characters and complete the matrix with remaining alphabet characters that were not part of the key
    const keyCharSet = new Set(keyArray)
    const alphabetString = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' // string without J
    const alphabetSet = new Set([...alphabetString])
    for (const char of alphabetSet) {
        keyCharSet.add(char)
    }
    return keyCharSet
}

// Locates the row and column of a character in the given matrix
function findPositionInTable(char, matrix) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === char) {
                return { row: i, column: j }
            }
        }
    }
    return null
}

function decryptText(encryptedText, matrixVals) {
    encryptedText = encryptedText.toUpperCase()
    encryptedText = encryptedText.replace(/[^a-zA-Z ]/g, "") // Source: https://stackoverflow.com/questions/6555182/remove-all-special-characters-except-space-from-a-string-using-javascript

    // populate the 5x5 matrix
    let cipherTable = []
    for (let i = 0; i < 5; i++) {
        let row = []
        for (let j = 0; j < 5; j++) {
            let value = matrixVals.values().next().value;
            row.push(value)
            matrixVals.delete(value)
        }
        cipherTable.push(row)
    }

    let decryptedText = ""
    for (let i = 0; i < encryptedText.length; i += 2) {
        // use helper function findPositionInTable to find the row and column indices of each letter
        const firstLetterPosition = findPositionInTable(encryptedText.charAt(i), cipherTable)
        const secondLetterPosition = findPositionInTable(encryptedText.charAt(i + 1), cipherTable)
        // find decrypted characters
        if (firstLetterPosition.column === secondLetterPosition.column) { // same column case
            decryptedText += cipherTable[(firstLetterPosition.row + 4) % 5][firstLetterPosition.column];
            decryptedText += cipherTable[(secondLetterPosition.row + 4) % 5][secondLetterPosition.column];
        } else if (firstLetterPosition.row === secondLetterPosition.row) { // same row case
            decryptedText += cipherTable[firstLetterPosition.row][(firstLetterPosition.column + 4) % 5];
            decryptedText += cipherTable[secondLetterPosition.row][(secondLetterPosition.column + 4) % 5];
        } else { // rectangle case
            decryptedText += cipherTable[firstLetterPosition.row][secondLetterPosition.column];
            decryptedText += cipherTable[secondLetterPosition.row][firstLetterPosition.column];
        }
    }

    // remove X's from result
    let result = ""
    for (let i = 0; i < decryptedText.length; i++) {
        if (decryptedText[i] !== 'X') {
            result += decryptedText[i]
        }
    }
    result = result.trim()
    console.log(result)
    return decryptedText;
}

// Initialize matrix values given the key
set = initializeMatrixVals("Superspy")

decryptText("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", set)
