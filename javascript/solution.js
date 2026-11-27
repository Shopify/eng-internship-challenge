/*

Author: Sumit Savaliya 
Email: sumit.savaliya@dal.ca
Github: https://www.github.com/sumitx28

Plan:
1. Generate a 5x5 cipher matrix based on a given secret key.
2. Break the encrypted text into pairs of characters, adding 'X' if needed to make pairs.
3. Decrypt each pair by following these rules:
   - If both characters are in the same row, replace each character with the character to its left, wrapping around if needed.
   - If both characters are in the same column, replace each character with the character above it, wrapping around if needed.
   - If the characters form a rectangle, swap them with the characters on the same row but at the opposite corners of the rectangle.
4. Concatenate the decrypted characters to get the original message.
5. Output the decrypted message.

 Cipher Matrix:
  [
    ["S", "U", "P", "E", "R"],
    ["Y", "A", "B", "C", "D"],
    ["F", "G", "H", "I", "K"],
    ["L", "M", "N", "O", "Q"],
    ["T", "V", "W", "X", "Z"]
  ]
  
*/

/**
 * Generates a 5x5 cipher matrix based on a given key.
 * 
 * @param {string} key - The secret key used to generate the cipher matrix.
 * @returns {Array<Array<string>>} The generated cipher matrix.
 */
function generateCipherMatrix(key) {
    // Created a string of unique characters by combining the key and standard alphabet (excluding 'J')
    const uniqueChars = [...new Set(key + "ABCDEFGHIKLMNOPQRSTUVWXYZ")];
    const matrix = [];

    for (let i = 0; i < uniqueChars.length; i += 5) {
        matrix.push(uniqueChars.slice(i, i + 5));
    }

    return matrix;
}

/**
 * Splits the encrypted text into pairs of characters.
 * If the number of characters is odd, adds 'X' to make pairs.
 * 
 * @param {string} encryptedText - The text to be split into pairs.
 * @returns {Array<Array<string>>} The array of character pairs.
 */
function createPairs(encryptedText) {
    const pairs = [];

    for (let i = 0; i < encryptedText.length; i += 2) {
        // Get the first character of the pair
        let firstChar = encryptedText[i];
        // Determine the second character of the pair
        let secondChar = (i + 1 < encryptedText.length && encryptedText[i] === encryptedText[i + 1]) ? 'X' : encryptedText[i + 1];
        // Add the pair to the pairs array
        pairs.push([firstChar, secondChar]);
    }

    // If the length of the encrypted text is odd, add the last character with 'X'
    if (encryptedText.length % 2 !== 0) {
        pairs.push([encryptedText[encryptedText.length - 1], 'X']);
    }

    return pairs;
}

/**
 * Finds the row and column index of a given value in the cipher matrix.
 * 
 * @param {Array<Array<string>>} matrix - The cipher matrix to search.
 * @param {string} value - The value to search for in the matrix.
 * @returns {Array<number>} An array containing the row and column index of the value.
 *                           If the value is not found, returns [-1, -1].
 */
function findMatrixIndex(matrix, value) {

    for (let i = 0; i < matrix.length; i++) {
        // Find the index of the value in the current row
        let j = matrix[i].indexOf(value);
        // If the value is found in the row, return its row and column index
        if (j !== -1) {
            return [i, j];
        }
    }
    // If the value is not found in the matrix, return [-1, -1]
    return [-1, -1];
}

/**
 * Decrypts an array of character pairs using a given cipher matrix.
 * 
 * @param {Array<Array<string>>} pairs - The array of character pairs to decrypt.
 * @param {Array<Array<string>>} matrix - The cipher matrix used for decryption.
 * @returns {string} The decrypted message.
 */
function decryptPairs(pairs, matrix) {
    let decryptedMessage = "";

    // Decrypt each pair
    for (let [firstChar, secondChar] of pairs) {
        // row and column indices of the characters in the matrix
        let [firstRow, firstCol] = findMatrixIndex(matrix, firstChar);
        let [secondRow, secondCol] = findMatrixIndex(matrix, secondChar);

        // Decrypt based on the positions of the characters in the matrix
        if (firstRow === secondRow) {
            // Same row: replace each character with the character to its left
            decryptedMessage += matrix[firstRow][(firstCol + 4) % 5];
            decryptedMessage += matrix[secondRow][(secondCol + 4) % 5];
        } else if (firstCol === secondCol) {
            // Same column: replace each character with the character above it
            decryptedMessage += matrix[(firstRow + 4) % 5][firstCol];
            decryptedMessage += matrix[(secondRow + 4) % 5][secondCol];
        } else {
            // Forming a rectangle: swap characters
            decryptedMessage += matrix[firstRow][secondCol];
            decryptedMessage += matrix[secondRow][firstCol];
        }
    }

    // Remove any 'X' characters and return the decrypted message
    return decryptedMessage.replace(/X/g, '');
}

// Command Line Runner
const secretKey = "SUPERSPY";
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

const cipherMatrix = generateCipherMatrix(secretKey);
const encryptedPairs = createPairs(encryptedMessage);
const decryptedMessage = decryptPairs(encryptedPairs, cipherMatrix);

console.log(decryptedMessage);