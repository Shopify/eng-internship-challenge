// Function to generate Playfair matrix
function generateMatrix(key) {
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // excludes 'J'
    const keyNoDuplicates = Array.from(new Set(key.toUpperCase())).join("");
    const keyAdjusted = keyNoDuplicates + alphabet.replace(new RegExp(`[${keyNoDuplicates}]`,'g'),  "");
    const matrix = [];

    for (let i = 0; i < 5; i++) {
        matrix.push(keyAdjusted.slice(i * 5, (i + 1) * 5).split("")); // splits the string into 5
    }

    return matrix;
}

// Function to decrypt using Playfair Cipher
function playfairDecrypt(encryptedText, key) {
    const matrix = generateMatrix(key);
    let decryptedText = "";

    for (let i = 0; i < encryptedText.length; i += 2) {
        let pair1 = encryptedText[i]; // first character of the pair
        let pair2 = encryptedText[i + 1]; // second character of the pair

        let [x1, y1] = findPosition(matrix, pair1); 
        let [x2, y2] = findPosition(matrix, pair2);

        if (x1 === x2) { // both characters are in the same row
            decryptedText += matrix[x1][(y1 + 4) % 5];
            decryptedText += matrix[x2][(y2 + 4) % 5];
        } else if (y1 === y2) { // characters are in the same column
            decryptedText += matrix[(x1 + 4) % 5][y1];
            decryptedText += matrix[(x2 + 4) % 5][y2];
        } else { // characters are in different rows and columns
            decryptedText += matrix[x1][y2];
            decryptedText += matrix[x2][y1];
        }
    }

    // removes any non-uppercase letters, spaces, or 'X'
    decryptedText = decryptedText.replace(/[^A-Z]/g, "").replace(/X/g, "");

    return decryptedText;
}

function solvePlayfairCipher(encryptedText, key) {
    console.log(playfairDecrypt(encryptedText, key));
}

// Finds the position of letter in the matrix
function findPosition(matrix, letter) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === letter) {
                return [i, j]; // returns the row and column position of the letter
            }
        }
    }
}

const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";
solvePlayfairCipher(encryptedText, key);

// Output: HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA

// At first, I doubted my solution, thinking there's no way this could be a word! But lo and behold, it turned out to be a lengthy one, describing "the phobia or fear of long words". Shopify always keeps me entertained with these interview questions!