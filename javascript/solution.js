function createGrid(key) {
    // Create 5x5 key square
    const keyTable = [];
    const seen = new Set();
    const alphabet = 'abcdefghiklmnopqrstuvwxyz'; // 'j' is excluded

    // Process the key
    key.toLowerCase().replace(/[^a-z]/g, '').split('').forEach(char => {
        if (char !== 'j' && !seen.has(char)) {
            seen.add(char);
            keyTable.push(char);
        }
    });

    // Fill the rest of the table with the remaining letters
    for (let char of alphabet) {
        if (!seen.has(char)) {
            keyTable.push(char);
        }
    }

    // Convert the flat array into a 2D array
    return Array.from({ length: 5 }, (_, i) => keyTable.slice(i * 5, i * 5 + 5));
}

function search(keyTable, a, b) {
    // Search for the characters of a digraph in the key square and return their positions
    if (a === 'j') a = 'i';
    if (b === 'j') b = 'i';

    const pos = [];
    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (keyTable[i][j] === a) pos[0] = [i, j];
            if (keyTable[i][j] === b) pos[1] = [i, j];
        }
    }

    return pos;
}

function mod5(x) {
    return (x + 5) % 5;
}

function decrypt(str, keyTable) {
    // Decrypt the string using the key table
    let result = '';

    for (let i = 0; i < str.length; i += 2) {
        let [aPos, bPos] = search(keyTable, str[i], str[i + 1]);

        if (aPos[0] === bPos[0]) {
            // Same row
            result += keyTable[aPos[0]][mod5(aPos[1] - 1)];
            result += keyTable[bPos[0]][mod5(bPos[1] - 1)];
        } else if (aPos[1] === bPos[1]) {
            // Same column
            result += keyTable[mod5(aPos[0] - 1)][aPos[1]];
            result += keyTable[mod5(bPos[0] - 1)][bPos[1]];
        } else {
            // Rectangle
            result += keyTable[aPos[0]][bPos[1]];
            result += keyTable[bPos[0]][aPos[1]];
        }
    }

    return result.toUpperCase().replace(/[^A-Z]/g, '').replace(/X/g, '');
}

function decryptPlayfairCipher(str, key) {
    // Prepare the key and ciphertext
    key = key.toLowerCase().replace(/[^a-z]/g, '');
    str = str.toLowerCase().replace(/[^a-z]/g, '');

    // Create the key table
    const keyTable = createGrid(key);

    // Decrypt the ciphertext
    return decrypt(str, keyTable);
}

const str = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";

// Decrypt using Playfair Cipher
const plainText = decryptPlayfairCipher(str, key);

// Decrypted text
console.log(plainText);
