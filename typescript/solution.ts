function createMatrix(key: string): string[][] {
    const alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    let matrixKey = "";
    let seen = new Set<string>();

    // add characters from key to matrixKey with no duplicates
    for (let char of key.toUpperCase()) {
        if (!seen.has(char) && alpha.includes(char)) {
            seen.add(char);
            matrixKey += char;
        }
    }

    // add remaining characters of the alphabet
    for (let char of alpha) {
        if (!seen.has(char)) {
            matrixKey += char;
        }
    }

    let matrix: string[][] = [];

    // create 5x5 matrix
    for (let i = 0; i < 5; i++) {
        matrix.push(matrixKey.slice(i * 5, (i + 1) * 5).split(''));
    }

    return matrix;
}

function decrypt(matrix: string[][], message: string): string {
    let decryptedMessage = '';
    let pairs: string[] = [];

    for (let i = 0; i < message.length; i += 2) {
        pairs.push(message.substring(i, i + 2));
    }

    pairs.forEach(pair => {
        let [first, second] = pair.split('');
        let firstPos = findPosition(matrix, first);
        let secondPos = findPosition(matrix, second);

        if (firstPos.row === secondPos.row) {
            // same row, go left
            first = matrix[firstPos.row][(firstPos.col + 4) % 5];
            second = matrix[secondPos.row][(secondPos.col + 4) % 5];
        } else if (firstPos.col === secondPos.col) {
            // same column, go up
            first = matrix[(firstPos.row + 4) % 5][firstPos.col];
            second = matrix[(secondPos.row + 4) % 5][secondPos.col];
        } else {
            // rectangle, go opposite corner
            first = matrix[firstPos.row][secondPos.col];
            second = matrix[secondPos.row][firstPos.col];
        }

        decryptedMessage += first + second;
    });

    // clean decrypted message before returning
    return decryptedMessage.replace(/X|[^A-Z]/g, '');
}

function findPosition(matrix: string[][], letter: string): { row: number; col: number } {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (matrix[row][col] === letter) {
                return { row, col };
            }
        }
    }

    // error, should never reach here
    return { row: -1, col: -1 };
}

function main() {
    const key = "SUPERSPY";
    const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

    const matrix = createMatrix(key);
    const decryptedText = decrypt(matrix, message);
    console.log(decryptedText);
}

main();