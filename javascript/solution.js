// Generate the key table for the Playfair cipher
function generateKeyTable(keyword) {
    let keyTable = [];
    // Alphabet without 'J' as per the rules of the Playfair cipher
    let alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';

    // Add the keyword to the keyTable while removing any duplicate characters
    for (let char of keyword) {
        if (!keyTable.includes(char)) {
            keyTable.push(char);
        }
    }

    // Populate the remaining key table
    for (let char of alphabet) {
        if (!keyTable.includes(char) && keyTable.length < 25) {
            keyTable.push(char);
        }
    }
    return keyTable;
}

// Function to divide the message into pairs of characters
function dividePairs(message) {
    let pairs = [];
    // Split message into pairs of characters
    for (let i = 0; i < message.length; i+=2) {
        let first = message[i];
        let second;
        // Handle odd length message
        if (i === message.length - 1) {
            second = 'X';
        } else {
            second = message[i + 1];
        }
        // If both characters are the same, replace the second character with 'X', and decrement i
        if (first === second) {
            second = 'X';
            i--;
        }
        pairs.push([first, second]);
    }
    return pairs;
}

// Function to find the position of a character in the keyTable
function findPosition(char, keyTable) {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keyTable[row * 5 + col] === char) {
                return [row, col];
            }
        }
    }
}

function decrypt(pairs, keyTable) {
    let answer = '';
    for (let i = 0; i < pairs.length; i++) {
        // Find the positions of the characters in the keyTable in [row, column] format
        const pos1 = findPosition(pairs[i][0], keyTable);
        const pos2 = findPosition(pairs[i][1], keyTable);

        let decryptedString = '';
        if (pos1[0] === pos2[0]) { // Same row, replace each character with the one on its left
            decryptedString += keyTable[pos1[0] * 5 + (pos1[1] + 4) % 5];
            decryptedString += keyTable[pos2[0] * 5 + (pos2[1] + 4) % 5];
        } else if (pos1[1] === pos2[1]) { // Same column, replace each character with the one above it
            decryptedString += keyTable[((pos1[0] + 4) % 5) * 5 + pos1[1]];
            decryptedString += keyTable[((pos2[0] + 4) % 5) * 5 + pos2[1]];
        } else { // Replace each character with the same row but diff column
            decryptedString += keyTable[pos1[0] * 5 + pos2[1]];
            decryptedString += keyTable[pos2[0] * 5 + pos1[1]];
        }

        answer += decryptedString;
    }

    // Remove any 'X' characters to clean up the message
    answer = answer.replace(/X/g, ''); 

    console.log(answer);
}

function solvePlayfairCipher(message, keyword) {
    let keyTable = generateKeyTable(keyword);
    let pairArray = dividePairs(message);
    decrypt(pairArray, keyTable);
}


solvePlayfairCipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY");
