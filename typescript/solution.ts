// Generate the key square based on the key
function generateKeySquare(key: string): string[][] {
    const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
    key = key.toUpperCase().replace(/J/g, 'I');
    const keySet = new Set<string>();

    // Fill the key set with unique characters from the key and alphabet
    for (const char of key + alphabet) {
        if (alphabet.includes(char)) {
            keySet.add(char);
        }
    }

    // Convert the set to a 5x5 grid
    const keyString = Array.from(keySet).join('');
    return Array.from({ length: 5 }, (_, i) => keyString.slice(i * 5, i * 5 + 5).split(''));
}

// Find the position of a character in the key square
function findPosition(char: string, keySquare: string[][]): [number, number] {
    for (let row = 0; row < 5; row++) {
        const col = keySquare[row].indexOf(char);
        if (col !== -1) return [row, col];
    }
    throw new Error('Character not found in key square');
}

// Decode a pair of characters using the key square
function decodePair(pair: string, keySquare: string[][]): string {
    const [row1, col1] = findPosition(pair[0], keySquare);
    const [row2, col2] = findPosition(pair[1], keySquare);

    if (row1 === row2) {
        // Same row: take the character to the left of each one
        return keySquare[row1][(col1 + 4) % 5] + keySquare[row2][(col2 + 4) % 5];
    } else if (col1 === col2) {
        // Same column: take the character above each one
        return keySquare[(row1 + 4) % 5][col1] + keySquare[(row2 + 4) % 5][col2];
    } else {
        // Rectangle: swap columns
        return keySquare[row1][col2] + keySquare[row2][col1];
    }
}

// Decode the entire message using the key
function decodeMessage(message: string, key: string): string {
    const keySquare = generateKeySquare(key);
    message = message.toUpperCase().replace(/[^A-Z]/g, '').replace(/J/g, 'I');
    let decodedMessage = '';

    for (let i = 0; i < message.length; i += 2) {
        const pair = message.slice(i, i + 2);
        let decodedPair = decodePair(pair, keySquare);

        // Handle 'X' padding
        if (decodedPair[1] === 'X' && (i + 2 >= message.length || message[i + 2] !== 'X')) {
            decodedPair = decodedPair[0];
        }

        decodedMessage += decodedPair;
    }

    return decodedMessage;
}

const KEY = "SUPERSPY";
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
console.log(decodeMessage(ENCRYPTED_MESSAGE, KEY));
