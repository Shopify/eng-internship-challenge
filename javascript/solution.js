function generateKeySquare(key) {
    const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'; 
    let keyString = key.toUpperCase().replace(/J/g, 'I') + alphabet;
    keyString = [...new Set(keyString)]; 

   
    const keySquare = [];
    for (let i = 0; i < 25; i += 5) {
        keySquare.push(keyString.slice(i, i + 5));
    }
    return keySquare;
}

function preprocessCipherText(cipherText) {
    return cipherText.toUpperCase().replace(/[^A-Z]/g, '').replace(/J/g, 'I');
}

function findPosition(char, keySquare) {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keySquare[row][col] === char) {
                return { row, col };
            }
        }
    }
    return null;
}

function decryptPair(pair, keySquare) {
    const pos1 = findPosition(pair[0], keySquare);
    const pos2 = findPosition(pair[1], keySquare);

    if (pos1.row === pos2.row) {
        return keySquare[pos1.row][(pos1.col + 4) % 5] + keySquare[pos2.row][(pos2.col + 4) % 5];
    } else if (pos1.col === pos2.col) {
        return keySquare[(pos1.row + 4) % 5][pos1.col] + keySquare[(pos2.row + 4) % 5][pos2.col];
    } else {
        return keySquare[pos1.row][pos2.col] + keySquare[pos2.row][pos1.col];
    }
}

function decryptPlayfairCipher(cipherText, key) {
    const keySquare = generateKeySquare(key);
    const preparedText = preprocessCipherText(cipherText);

    let decryptedText = '';
    for (let i = 0; i < preparedText.length; i += 2) {
        decryptedText += decryptPair(preparedText.slice(i, i + 2), keySquare);
    }

    
    return decryptedText.replace(/X/g, '');
}

