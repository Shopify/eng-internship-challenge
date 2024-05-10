/**
 * Create a 5 x 5 Playfair square using the given keyword
 * This 5 x 5 square is represented as a string of 25 characters
 * 
 * @param {string} - keyword - the keyword to be used to create the square
 * @returns {string} - the 5 x 5 Playfair square that consists of 25 characters
 */
function createSquare(keyword) {
    // letter J is not used in the square
    const letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    let square = "";

    // add the keyword to the square first
    for (let c of keyword) {
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
    console.log(pairs);
    return pairs;
}

// Test the function
createSquare("SUPERSPY");
preprocessEncryption("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV");