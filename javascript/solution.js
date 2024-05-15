const key = "SUPERSPY";
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"


/**
 * Function that decrypts a message using the Playfair Cipher, given a key and an encrypted message.
 * @param {string} key 
 * @param {string} encryptedMessage 
 * @returns string
 */


function decryptMessage(key, encryptedMessage) {

    // Validate the inputs
    if (!validateInput(key, encryptedMessage)) {
        return;
    }

    // Format the inputs
    const { formattedKey, formattedMessage } = formatInput(key, encryptedMessage);

    // Create the matrix & the character position map
    const {matrix, charPositionMap} = createMatrix(formattedKey);

    // Decrypt the message
    const decryptedMessage = decrypt(matrix, charPositionMap, formattedMessage);

    // Remove spaces from decrypted message
    decryptedMessage.trim();

    // Remove all non-alphabetic characters and "X" from the decrypted message
    const finalMessage = decryptedMessage.replace(/[^A-WYZ]/g, '');

    console.log(finalMessage);

    return finalMessage;
    
}


/**
 * Function that performs the actual decryption of the message, given the matrix, the character position map and the formatted message.
 * @param {string[][]} matrix 
 * @param {Object} charPositionMap 
 * @param {string} formattedMessage
 * @returns string
 */
function decrypt(matrix, charPositionMap, formattedMessage) {

    const decryptedMessage = [];
    
    for (let i = 0; i < formattedMessage.length; i += 2) {

        // Get the pair of characters to decrypt
        const char1 = formattedMessage[i];
        // If the message has an odd number of characters, we add an "X" at the end
        const char2 = i + 1 < formattedMessage.length ? formattedMessage[i + 1] : "X";

        // Get the position of the characters in the matrix, using the map we created before
        // Avoid traversing the matrix, which is O(n^2)
        const pos1 = charPositionMap[char1];
        const pos2 = charPositionMap[char2];

        if (pos1.row === pos2.row) {
            // If the characters are in the same row
            decryptedMessage.push(matrix[pos1.row][(pos1.col + 4) % 5]);
            decryptedMessage.push(matrix[pos2.row][(pos2.col + 4) % 5]);
        } else if (pos1.col === pos2.col) {
            // Same column
            decryptedMessage.push(matrix[(pos1.row + 4) % 5][pos1.col]);
            decryptedMessage.push(matrix[(pos2.row + 4) % 5][pos2.col]);
        } else {
            // Rectangle swap
            decryptedMessage.push(matrix[pos1.row][pos2.col]);
            decryptedMessage.push(matrix[pos2.row][pos1.col]);
        }
    }

    return decryptedMessage.join('');
}


/**
 * Create the Playfair Cipher matrix and a character mapping object
 * @param {*} key 
 * @returns [Array, Object]
 */

function createMatrix(key){

    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

    let keyString = key + alphabet;

    keyString = removeDuplicates(keyString);

    // Create the 5x5 matrix
    const matrix = [];

    // Create a mapping object so that we can check in a O(1) time the position of a character, without having to iterate over the matrix
    const charPositionMap = {};


    const numberOfRows = 5;
    const numberOfCols = 5;

    let index = 0;


    for (let row = 0; row < numberOfRows; row++) {
        matrix[row] = [];
        for (let col = 0; col < numberOfCols; col++) {
            matrix[row][col] = keyString[index++];
            charPositionMap[matrix[row][col]] = { row, col };
        }
    }

    return {matrix, charPositionMap};

}



/**
 * This function's goal is to validate  the input.
 * Validation :  key and message are both non-empty-strings that contains only alphabetic characters. 
 * @param {string} key 
 * @param {string} message 
 * @returns boolean
 */
function validateInput(key, message){

    //Regex which checks for alphabetic characters
    const alphaRegex = /^[A-Za-z]+$/;

    try {
        // Check that key is a non-empty string and contains only alphabetic characters
        if (typeof key !== 'string' || key.length === 0 || !alphaRegex.test(key)) {
            throw new Error("Invalid key: The key should be a non-empty string containing only alphabetic characters.");
        }

        // Check that message is a non-empty string and contains only alphabetic characters
        if (typeof message !== 'string' || message.length === 0 || !alphaRegex.test(message)) {
            throw new Error("Invalid message: The message should be a non-empty string containing only alphabetic characters.");
        }

        return true;
        
    } catch (error) {
        console.error("Validation Error:", error.message);
        // Indicate that the validation failed
        return false;
    }

}


/**
 * This function's goal is to format the input.
 * Formatting : key and message are converted to uppercase. Duplicates are removed from the key.
 * @param {string} key 
 * @param {string} message 
 * @returns Object
 */
function formatInput(key, message){

    // Convert key and message to uppercase
    key = key.toUpperCase();
    message = message.toUpperCase();

    //Remove the duplicate from the key
    key = removeDuplicates(key);

    return { formattedKey: key, formattedMessage: message };

}


/**
 * Remove duplicates from a string
 * @param {string} key 
 * @returns string
 */
function removeDuplicates(key){
    let result = '';
    let seen = new Set();
    
    for (let char of key) {
        if (!seen.has(char)) {
            seen.add(char);
            result += char;
        }
    }

    return result;
}


decryptMessage(key, encryptedMessage);