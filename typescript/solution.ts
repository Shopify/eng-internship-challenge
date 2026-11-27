/** 
 * Shopify Engineer Intern Challenge - Fall 2024
 * Author: Viet An Truong
 * The Playfair cipher is a digraph substitution cipher. It employs a table where one letter of the alphabet is omitted, and the letters are arranged in a 5x5 grid.
 * The key for the Playfair cipher is a word that is used to create the key square. The key square is a 5x5 grid of letters that acts as the key for encrypting the plaintext.
 * The key square is filled with the letters of the keyword (minus duplicates) and then the remaining letters of the alphabet in order.
*/

// Generate the key square based on the key
// explanation: The key square is a 5x5 grid of letters that acts as the key for encrypting the plaintext.
// The key square is filled with the letters of the keyword (minus duplicates) and then the remaining letters of the alphabet in order.
function generateKeySquare(key: string): string[][] {
    const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
    key = key.toUpperCase().replace(/J/g, 'I');
    let keyString = '';

    // fill the key square with the letters of the keyword (minus duplicates)
    for (const char of key) {
        if (!keyString.includes(char) && alphabet.includes(char)) {
            keyString += char;
        }
    }

    // fill the key square with the remaining letters of the alphabet in order
    for (const char of alphabet) {
        if (!keyString.includes(char)) {
            keyString += char;
        }
    }

    // convert the key string to a 5x5 grid
    const keySquare: string[][] = [];
    for (let i = 0; i < 5; i++) {
        keySquare.push(keyString.slice(i * 5, i * 5 + 5).split(''));
    }

    return keySquare;
}

// Find the position of a character in the key square
function findPosition(char: string, keySquare: string[][]): [number, number] {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keySquare[row][col] === char) {
                // return the position of the character in the key square
                return [row, col];
            }
        }
    }
    throw new Error('Character not found in key square');
}

// Decode a pair of characters
// explanation: To decrypt a pair of characters, we find the positions of the characters in the key square.
// If the characters are in the same row, we take the character to the left of each one.
// If the characters are in the same column, we take the character above each one.
// Otherwise, we take the character that is in the same row as the first character but in the same column as the second character.
function decodePair(pair: string, keySquare: string[][]): string {
    const [row1, col1] = findPosition(pair[0], keySquare);
    const [row2, col2] = findPosition(pair[1], keySquare);

    if (row1 === row2) {
        // same row. take the character to the left of each one
        return keySquare[row1][(col1 + 4) % 5] + keySquare[row2][(col2 + 4) % 5];
    } else if (col1 === col2) {
        // same column. take the character above each one
        return keySquare[(row1 + 4) % 5][col1] + keySquare[(row2 + 4) % 5][col2];
    } else {
        // take the character that is in the same row as the first character but in the same column as the second character
        return keySquare[row1][col2] + keySquare[row2][col1];
    }
}

// Decode the message using the key square
// explanation: To decrypt the message, we split it into pairs of characters.
// If the second character of a pair is 'X' and the first character is the same as the third character, we remove the 'X'.
// We then decode each pair of characters using the key square.
function decodeMessage(message: string, key: string): string {
    const keySquare = generateKeySquare(key);
    message = message.toUpperCase().replace(/[^A-Z]/g, '').replace(/J/g, 'I');
    let decodedMessage = '';

    for (let i = 0; i < message.length; i += 2) {
        if (i + 1 < message.length) {
            const pair = message[i] + message[i + 1];
            let decodedPair = decodePair(pair, keySquare);

            // remove 'X' if the second character of a pair is 'X' and the first character is the same as the third character
            if (decodedPair[1] === 'X' && (i + 2 >= message.length || message[i + 2] !== 'X')) {
                decodedPair = decodedPair[0];
            }

            decodedMessage += decodedPair;
        }
    }

    return decodedMessage;
}

// decode the encrypted message given the key
const KEY = "SUPERSPY";
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

console.log(decodeMessage(ENCRYPTED_MESSAGE, KEY));