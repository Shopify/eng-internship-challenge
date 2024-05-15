

/**
 * Creates a 5x5 Playfair Cipher matrix
 * @param {string} key - Cipher key
 * @returns {Object} An object containing:
 *   - matrix: The 5x5 Cipher matrix.
 *   - positionMap: Map, holding each character's position {row, col} in the matrix.
 * @throws {Error} Throws an error if the final set of characters does not equal 25.
 */
function createMatrix(key) {
    // Ensures key is uppercase, replaces J with I and removes any special characters
    const cleanKey = key.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');
    const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'; // Omitts 'J'
    const matrix = [];
    let row = []

    // Concatenate the two strings
    const combined = cleanKey + alphabet;

    // Removes any duplicates within the key and alphabet
    const uniqueSet = new Set(combined);

    if (uniqueSet.size !== 25) {
        throw new Error("Set must contain exactly 25 elements.");
    }

    // Creates 5x5 matrix
    uniqueSet.forEach(char => {
        if (row.push(char) === 5) {
            matrix.push(row);
            row = [];
        }
    });

    // Creates a map to optimize finding positions of characters in the matrix
    const positionMap = new Map();
    matrix.forEach((row, rowIndex) => {
        row.forEach((char, colIndex) => {
            positionMap.set(char, { row: rowIndex, col: colIndex }); // Maps each char to its row and column values
        });
    });

    return { matrix, positionMap }; // Object containing both matrix and positionMap
}


/**
 * Decrypts a pair of characters using the Playfair cipher rules.
 * @param {Object} matrixInfo - Contains the Playfair cipher's matrix and position map.
 * @param {string} digram - Two characters that need to be decrypted.
 * @returns {string} The decrypted characters.
 */
function decrypt(matrixInfo, digram) {
    // Retrieve positions of each character in the digram
    const pos1 = matrixInfo.positionMap.get(digram[0]);
    const pos2 = matrixInfo.positionMap.get(digram[1]);
    let decrypted = '';

    if (pos1.row === pos2.row) {
        decrypted += matrixInfo.matrix[pos1.row][(pos1.col + 4) % 5]; // Shift left by one in the row
        decrypted += matrixInfo.matrix[pos2.row][(pos2.col + 4) % 5];
    } else if (pos1.col === pos2.col) {
        decrypted += matrixInfo.matrix[(pos1.row + 4) % 5][pos1.col]; // Shift up by one in the column
        decrypted += matrixInfo.matrix[(pos2.row + 4) % 5][pos2.col];
    } else {
        decrypted += matrixInfo.matrix[pos1.row][pos2.col]; // Swap columns
        decrypted += matrixInfo.matrix[pos2.row][pos1.col];
    }

    return decrypted;
}

/**
 * Removes unwanted 'X' characters from a given message that could have been added to:
 * 1. Make the original message an even number of characters
 * 2. To seperate duplicate letters in the original message
 * @param {string} message - The decrypted message
 * @returns {string} The cleaned message with specific 'X' characters removed.
 */
function removeX(message) {
    // Check if the last character is 'X' and the length of the string is even
    if (message.endsWith('X') && message.length % 2 === 0) {
        message = message.slice(0, -1); // Remove the last character
    }

    // Remove 'X' between two identical letters
    message = message.replace(/([A-Z])X\1/gi, '$1$1');

    return message;
}


/**
 * Decrypts an encrypted message.
 * The decryption is handled in pairs (digraphs), applying the Playfair cipher decryption rules.
 * @param {Object} matrixInfo - Contains the Playfair cipher's matrix and position map.
 * @param {string} encryptedMessage - The message to be decrypted. 
 * @returns {string} The decrypted message.
 * @throws {Error} Throws an error if the encrypted message is not even in length.
 */
function decryptMessage(matrixInfo, encryptedMessage) {
    let decryptedMessage = '';

    if (encryptedMessage.length % 2 !== 0) {
        throw new Error("Encrypted message should be of even length ");
    }

    for (let i = 0; i < encryptedMessage.length; i += 2) {
        decryptedMessage += decrypt(matrixInfo, encryptedMessage.substring(i, i + 2));
    }

    return removeX(decryptedMessage);
}


// Given key
const key = 'SUPERSPY';
// Given encrypted message
const encryptedMessage = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
const matrixInfo = createMatrix(key);
const decryptedMessage = decryptMessage(matrixInfo, encryptedMessage);
console.log(decryptedMessage);
