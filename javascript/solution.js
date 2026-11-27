function generateMatrix(key) {
    let matrix = [];
    let used = new Array(26).fill(false);
    used['J'.charCodeAt(0) - 'A'.charCodeAt(0)] = true;  // 'J' is merged with 'I'

    // Insert the key into the matrix
    for (let char of key.toUpperCase()) {
        if (!used[char.charCodeAt(0) - 'A'.charCodeAt(0)] && char !== 'J') {
            matrix.push(char);
            used[char.charCodeAt(0) - 'A'.charCodeAt(0)] = true;
        }
    }

    // Fill the matrix with the rest of the letters
    for (let i = 0; i < 26; i++) {
        let char = String.fromCharCode(i + 'A'.charCodeAt(0));
        if (!used[i] && char !== 'J') {
            matrix.push(char);
        }
    }

    return matrix;
}

function decryptPlayfair(matrix, text) {
    let decryptedText = '';
    for (let i = 0; i < text.length; i += 2) {
        let pair1 = matrix.indexOf(text[i]);
        let pair2 = matrix.indexOf(text[i + 1]);
        let row1 = Math.floor(pair1 / 5)
        let col1 = pair1 % 5;
        let row2 = Math.floor(pair2 / 5)
        let col2 = pair2 % 5;

        if (row1 === row2) {
            col1 = (col1 + 4) % 5;
            col2 = (col2 + 4) % 5;
        } else if (col1 === col2) {
            row1 = (row1 + 4) % 5;
            row2 = (row2 + 4) % 5;
        } else {
            [col1, col2] = [col2, col1];
        }

        decryptedText += matrix[row1 * 5 + col1] + matrix[row2 * 5 + col2];
    }
    // Remove any 'X' and spaces, convert to uppercase
    return decryptedText.replace(/X/g, '');
}

function playfairDecrypt(key, encryptedMessage) {
    let matrix = generateMatrix(key);
    return decryptPlayfair(matrix, encryptedMessage);
}

const key = "SUPERSPY";
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const decryptedMessage = playfairDecrypt(key, encryptedMessage);

console.log(decryptedMessage);
