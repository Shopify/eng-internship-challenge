// Function to create the 5x5 grid or key square using the key that was provided for Playfair decryption
function generateKeySquare(key) {
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // The alphabet used in Playfair cipher, 'J' is excluded
    key = key.toUpperCase().replace(/J/g, "I"); // First convert given key to uppercase characters and replace 'J' with 'I'

    // Remove duplicate characters from a 'uniqueKey'
    let uniqueKey = "";
    for (let i = 0; i < key.length; i++) {
        if (!uniqueKey.includes(key[i])) {
            uniqueKey += key[i];
        }
    }

    // Add remaining alphabet characters to 'uniqueKey' to form the 'keySquare' that will be used 
    let keySquare = uniqueKey;
    for (let i = 0; i < alphabet.length; i++) {
        if (!keySquare.includes(alphabet[i])) {
            keySquare += alphabet[i];
        }
    }

    // Split the 'keySquare' into a 5x5 key square matrix
    let square = [];
    for (let i = 0; i < 25; i += 5) {
        square.push(keySquare.slice(i, i + 5).split('')); // Split each 5 characters into an array
    }
    return square; // Return the key square matrix
}

// Function to find the row and column of a given character in the key square
function findPosition(keySquare, char) {
    //iterate through each row and column of the key square
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keySquare[row][col] === char) {
                return [row, col]; // Return the position as [row, column] when the character is found 
            }
        }
    }
    return null; // Return null if character is not found (which shouldn't happen with a valid input)
}

// Function to decrypt a pair of characters using Playfair cipher rules 
function decryptPair(keySquare, char1, char2) {
    let pos1 = findPosition(keySquare, char1); // Get position of first character in the key square
    let pos2 = findPosition(keySquare, char2); // Get position of second character in the key square 

    let row1 = pos1[0], col1 = pos1[1];
    let row2 = pos2[0], col2 = pos2[1];

    if (row1 === row2) {
        // Rule 1: If both characters in a pair are in the same row of the key, move left by 1 
        //(i.e., replace them with the characters to their left - wrapping around the row if needed )
        return keySquare[row1][(col1 + 4) % 5] + keySquare[row2][(col2 + 4) % 5];
    } else if (col1 === col2) {
        // Rule 2: If both characters in a pair are in the same column, move up by 1
        //(i.e., replace them with characters immediatly above them - wrapping around the bottom if needed)
        return keySquare[(row1 + 4) % 5][col1] + keySquare[(row2 + 4) % 5][col2];
    } else {
        // Rule 3: If characters form a rectangle (i.e., they are not in the same row or column), swap columns 
        //(rather replace each character with the character in the same row but in the column of the other character)
        return keySquare[row1][col2] + keySquare[row2][col1];
    }
}

// Main function to decrypt the entire Playfair cipher text using Playfair cipher decryption method
function decryptPlayfair(cipherText, key) {
    cipherText = cipherText.toUpperCase().replace(/J/g, "I"); // Convert cipher text to uppercase and replace 'J' with 'I'

    let keySquare = generateKeySquare(key); // Generate the key square matrix using the key provided 
    let plainText = ""; // Initialize an empty string 'plainText' to hold the decrypted text

    // Process the cipher text in pairs of two characters at a time 
    for (let i = 0; i < cipherText.length; i += 2) {
        let char1 = cipherText[i]; // First character of the pair
        let char2 = cipherText[i + 1] || 'X'; // Second character of the pair, 'X' if there's no second character
        plainText += decryptPair(keySquare, char1, char2); // Decrypt the pair and add to plain text
    }

    return plainText; // Return the fully decrypted text
}

// Define the encrypted message and the key
let cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"; // The encrypted message
let key = "SUPERSPY"; // The key used to create the key square

// Decrypt the cipher text using the Playfair cipher decryption function
let decryptedText = decryptPlayfair(cipherText, key).replace(/X/g, ''); // Remove 'X' from the decrypted text
console.log(decryptedText); // Print the decrypted text