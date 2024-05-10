/**
 * This program decrypts an encrypted message using the Playfair cipher
 * Date: 2024-05-10
 * @author: Ge Xu
 */


/**
 * Create a 5 x 5 Playfair square using the given keyword
 * This 5 x 5 square is represented as a string of 25 characters
 * 
 * @param {string} - keyword - the keyword to be used to create the square
 * @returns {string} - the 5 x 5 Playfair square that consists of 25 characters
 */
function createSquare(keyword) {
    // letter 'J' is not used in the square
    const letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    let square = "";

    // add the keyword to the square first
    for (let c of keyword.toUpperCase()) {
        if (square.indexOf(c) === -1) {
            square += c;
        }
    }
    // add the remaining letters to the square
    for (let c of letters) {
        if (square.indexOf(c) === -1) {
            square += c;
        }
    }
    return square;
}

/**
 * Preprocess the ecrypted message by settinhg characters to be in pairs
 * @param {string} encryptedMessage - the encrypted message to preprocess
 * @returns {Array} - an array of strings that contains the pairs of characters
 */
function preprocessEncryption(encryptedMessage) {
    const pairs = [];
    // According to the rules of the Playfair cipher
    // the encrypted message must have even number of characters
    for (let i = 0; i < encryptedMessage.length; i += 2) {
        let pair = encryptedMessage.slice(i, i + 2);
        pairs.push(pair);
    }
    // console.log(pairs);
    return pairs;
}

/**
 * This function decrypts an encrypted message using the Playfair cipher
 * @param {string} keyword - the keyword used to create the Playfair square
 * @param {string} encryptedMessage - the encrypted message to decrypt
 * @returns {string} - the decrypted message
 */
function crackPlayfair(keyword, encryptedMessage) {
    const pairs = preprocessEncryption(encryptedMessage);
    // the 5x5 square is represented as a string of 25 characters
    const square = createSquare(keyword);
    let decryptedMessage = "";

    // process each pair of characters according to the rules of the Playfair cipher
    for (let pair of pairs) {
        let firstLetterIndex = square.indexOf(pair[0]);
        let secondLetterIndex = square.indexOf(pair[1]);

        let firstLetterRow = Math.floor(firstLetterIndex / 5);
        let firstLetterCol = firstLetterIndex % 5;
        let secondLetterRow = Math.floor(secondLetterIndex / 5);
        let secondLetterCol = secondLetterIndex % 5;
        
        // decrypt the pair of characters
        // case 1: if the characters are in the same row
        //         replace them with the characters to their left
        if (firstLetterRow === secondLetterRow) {
            // if the character is at the beginning of the row
            // replace it with the character at the end of the row
            if (firstLetterCol === 0) {
                decryptedMessage += square[firstLetterRow * 5 + 4];
            } else {
                decryptedMessage += square[firstLetterRow * 5 + (firstLetterCol - 1)];
            }
            if (secondLetterCol === 0) {
                decryptedMessage += square[secondLetterRow * 5 + 4];
            } else {
                decryptedMessage += square[secondLetterRow * 5 + (secondLetterCol - 1)];
            }
        } 
        // case 2: if the characters are in the same column
        //         replace them with the characters above them
        else if (firstLetterCol === secondLetterCol) {
            // if the character is at the top of the column
            // replace it with the character at the bottom of the column
            if (firstLetterRow === 0) {
                decryptedMessage += square[20 + firstLetterCol];
            } else {
                decryptedMessage += square[(firstLetterRow - 1) * 5 + firstLetterCol];
            }
            if (secondLetterRow === 0) {
                decryptedMessage += square[20 + secondLetterCol];
            } else {
                decryptedMessage += square[(secondLetterRow - 1) * 5 + secondLetterCol];
            }
        }
        // case 3: if the characters are in different rows and columns, these characters form a rectangle
        //         replace them with the characters on the same row but at the other corner of the rectangle
         else {
            decryptedMessage += square[firstLetterRow * 5 + secondLetterCol];
            decryptedMessage += square[secondLetterRow * 5 + firstLetterCol];
        }
    }
    // remove "X"s from the decrypted message
    decryptedMessage = decryptedMessage.replaceAll("X", "");
    return decryptedMessage;
}

// test the function
// console.log(crackPlayfair("", "CBNVNYSC")); // "BALLOON;
// console.log(crackPlayfair("", "PBDUPBDQOPPO")); // "MEETMEATNOON;
// console.log(crackPlayfair("LIZaRD", "EIAUSUMY")); // "BALLOON;

// run the program
console.log(crackPlayfair("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"));