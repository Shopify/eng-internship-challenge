// Alternate version of the solution using a hardcoded matrix


// Hardcoded matrix using the key "SUPERSPY"
const matrix = [
    ['S', 'U', 'P', 'E', 'R'],
    ['Y', 'A', 'B', 'C', 'D'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'Q'],
    ['T', 'V', 'W', 'X', 'Z']
];

function playfairDecrypt(encryptedText) {
    let decryptedText = "";

    for (let i = 0; i < encryptedText.length; i += 2) {
        let pair1 = encryptedText[i];
        let pair2 = encryptedText[i + 1];

        let [x1, y1] = findPosition(pair1);
        let [x2, y2] = findPosition(pair2);

        if (x1 === x2) {
            decryptedText += matrix[x1][(y1 + 4) % 5];
            decryptedText += matrix[x2][(y2 + 4) % 5];
        } else if (y1 === y2) {
            decryptedText += matrix[(x1 + 4) % 5][y1];
            decryptedText += matrix[(x2 + 4) % 5][y2];
        } else {
            decryptedText += matrix[x1][y2];
            decryptedText += matrix[x2][y1];
        }
    }

    // removes non-uppercase letters, spaces, or 'X'
    decryptedText = decryptedText.replace(/[^A-Z]/g, "").replace(/X/g, "");

    return decryptedText;
}

// func to find position of letter
function findPosition(letter) {
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === letter) {
                return [i, j];
            }
        }
    }
}

const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
console.log(playfairDecrypt(encryptedText));
// Output: HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA