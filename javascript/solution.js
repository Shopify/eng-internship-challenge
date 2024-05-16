// Constants for encrypted message and key
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const KEY = "SUPERSPY";

// Function to create the table with Playfair Cipher inputs
function createPlayfairTable(key) {
    let alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // excluding 'J'
    let table = [];

    // Initialize table with key
    for (let char of key) {
        if (!table.includes(char) && char !== 'J') {
            table.push(char);
            alphabet = alphabet.replace(char, '');
        }
    }
    // Fill the rest of the table with remaining alphabet
    for (let char of alphabet) {
        table.push(char);
    }
    return table;
}

// Function to create the Playfair Cipher matrix
function createPlayfairMatrix(table) {
    let matrix = [];
    for (let i = 0; i < 5; i++) {
        let row = [];
        for (let j = 0; j < 5; j++) {
            row.push(table[i * 5 + j]);
        }
        matrix.push(row);
    }
    return matrix;
}

// Function to find the position of a character in the cipher matrix
function findPosition(matrix, char) {
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (matrix[i][j] === char) {
                return { row: i, col: j };
            }
        }
    }
    return null;
}

// Function to decrypt using Playfair Cipher
function decrypt(text, key) {
    const table = createPlayfairTable(key);
    const matrix = createPlayfairMatrix(table);
    let message = '';
    for (let i = 0; i < text.length; i += 2) {
        let char1 = text[i];
        let char2 = text[i + 1];

        let pos1 = findPosition(matrix, char1);
        let pos2 = findPosition(matrix, char2);

        // Both letters are on the same row in the matrix
        if (pos1.row === pos2.row) { 
            message += matrix[pos1.row][(pos1.col - 1 + 5) % 5];
            message += matrix[pos2.row][(pos2.col - 1 + 5) % 5];
        // Both letters are in the same column in the matrix
        } else if (pos1.col === pos2.col) {
            message += matrix[(pos1.row - 1 + 5) % 5][pos1.col];
            message += matrix[(pos2.row - 1 + 5) % 5][pos2.col];
        // Both letters are neither in the same row nor the same column
        } else {
            message += matrix[pos1.row][pos2.col];
            message += matrix[pos2.row][pos1.col];
        }
    }

    // Remove all 'X' from message
    message = message.split('X').join('');

    return message;
}

// Function to solve a Playfair Cipher
function solvePlayfairCipher(message, key) {

    // Decrypt the message
    const decryptedMessage = decrypt(message.toUpperCase(), key.toUpperCase());

    // Output the decrypted message
    console.log(decryptedMessage);
}

// Function to run the solution
solvePlayfairCipher(ENCRYPTED_MESSAGE, KEY);


