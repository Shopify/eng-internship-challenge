function initializeMatrixVals(key) {
    // if the key contains j, clean it only include i omit J from matrix
    const keyArray = key.toUpperCase().split('')
    for (let i = 0; i < keyArray.length; i++) {
        if (keyArray[i] == 'J') {
            keyArray[i] = 'I'
        }
    }

    const keyCharSet = new Set(keyArray)
    const alphabetString = 'ABCDEFGHIKLMNOPQRSTUVWXYZ' // string without J
    const alphabetSet = new Set([...alphabetString])
    for (const char of alphabetSet) {
        keyCharSet.add(char)
    }
    console.log(keyCharSet)
    return keyCharSet
}

function decryptText(encryptedText, matrixVals) {
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

    for (let i = 0; i < cipherTable.length; i++) {
            console.log(cipherTable[i])
    }

    // break up encrypted text into digrams
    // add nonsense character to end of string for odd length
    if (encryptedText.toUpperCase().length % 2 != 0) {
        encryptedText += 'X'
    }

    // add nonsense characters to digrams with repeating letters
    

}

set = initializeMatrixVals("Superspy")
decryptText("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", set)
