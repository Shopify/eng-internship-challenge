//Solution for Shopify Engineering Challenge: Playfair Cipher Solver
//Written by: Jay Patel
//Date: 15 May 2024

//This function generates the key table based on the provided key word 
function createKeyTable(keyWord) {
    // By the rules of the key table, we omit the letter 'J'
    let alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
    let keyTable = [];

    // Add the keyword into the key table while disregarding duplicate characters
    for (let character of keyWord) {
        if (!keyTable.includes(character.toUpperCase())) { 
            keyTable.push(character.toUpperCase());
        }
    }

    // Add remaining characters from the alphabet to fill in the key table 
    for (let character of alphabet) {
        if (!keyTable.includes(character)) {
            keyTable.push(character);
        }
    }
    return keyTable;
}

//This function creates pair of characters based on message we want to decrypt 
function pairCharacters(message) {
    let pairs = [];

    for (let i = 0; i < message.length; i+=2) {
        let firstCharacter = message[i];

        // Mitigate odd length messages by adding an additional character X
        let secondCharacter = (i === message.length - 1) ? 'X' : message[i + 1];

        // Mitigate identical characters by replacing the second one with X and by shifting everything to its right forward. The precedent is done by decrementing the index i by 1
        if (firstCharacter === secondCharacter) {
            secondCharacter = 'X';
            i--; 
        }
        pairs.push([firstCharacter, secondCharacter]);
    }
    return pairs;
}

// This helper function find the position of the character in question by row and column
function trackCharacterPosition(keyTable, character) {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keyTable[row * 5 + col] === character) {
                return [row, col];
            }
        }
    }
}

// This function decrypts the provided encoded message using Playfair Cipher
function decryptMessage(pairs, keyTable) {
    let decryptedMessage = '';
    pairs.forEach(pair => {
        let characterPosition1 = trackCharacterPosition(keyTable, pair[0]);
        let characterPosition2 = trackCharacterPosition(keyTable, pair[1]);

        let decryptedPair = '';
        //decrypt based on both characters being in the same row by shifting by 1 position to the left
        if (characterPosition1[0] === characterPosition2[0]) {
            decryptedPair += keyTable[characterPosition1[0] * 5 + (characterPosition1[1] + 4) % 5]; 
            decryptedPair += keyTable[characterPosition2[0] * 5 + (characterPosition2[1] + 4) % 5]; 
        }
        //decrypt based on both characters being in the same column by shifting by 1 position upwards
        else if (characterPosition1[1] === characterPosition2[1]) {
            decryptedPair += keyTable[((characterPosition1[0] + 4) % 5) * 5 + characterPosition1[1]]; 
            decryptedPair += keyTable[((characterPosition2[0] + 4) % 5) * 5 + characterPosition2[1]]; 
        }
        //decrypt based on both characters not being in the same column or row, resulting in both characters swapping each other's column position
        else {
            decryptedPair += keyTable[characterPosition1[0] * 5 + characterPosition2[1]];
            decryptedPair += keyTable[characterPosition2[0] * 5 + characterPosition1[1]];
        }
        decryptedMessage += decryptedPair;
    });
    // Refactor the message by removing Characters 'X' 
    decryptedMessage = decryptedMessage.replace(/X/g, '');
    return decryptedMessage;
}

// This function makes use of all previously defined functions to decrypt the message
function solution(keyword, message) {
    if (keyword === '' || message === '') {
        console.log("invalid parameters provided");
    }
    let keyTable = createKeyTable(keyword);
    let pairs = pairCharacters(message);
    let answer = decryptMessage (pairs, keyTable);
    return answer;
}
console.log(solution("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"));