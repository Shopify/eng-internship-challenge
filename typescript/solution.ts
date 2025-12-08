interface Position {
    row: number;
    col: number;
}

function createMatrix(key: string): [string[][], Map<string, Position>] {
    const alpha = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    let matrixKey = "";
    let seen = new Set<string>();
    let positionMap = new Map<string, Position>();

    // add characters from key to matrixKey with no duplicates
    for (let char of key) {
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

    // create 5x5 matrix and populate position map
    for (let i = 0; i < 5; i++) {
        matrix.push(matrixKey.slice(i * 5, (i + 1) * 5).split(''));
        for (let j = 0; j < 5; j++) {
            positionMap.set(matrix[i][j], { row: i, col: j });
        }
    }

    return [matrix, positionMap];
}

function decrypt(matrix: string[][], positionMap: Map<string, Position>, message: string): string {
    let decryptedMessage = '';
    let pairs: string[] = [];

    for (let i = 0; i < message.length; i += 2) {
        pairs.push(message.substring(i, i + 2));
    }

    pairs.forEach(pair => {
        let [first, second] = pair.split('');
        let firstPos = positionMap.get(first);
        let secondPos = positionMap.get(second);

        if (!firstPos || !secondPos) {
            throw new Error(`\"${first}\" or \"${second}\" is not found in the position map`);
        }

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
    return decryptedMessage.replace(/X/g, '');
}

function preprocess(input: string): string {
    // replace J with I and remove special characters
    return input.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');
}

function main() {
    let key = "SUPERSPY";
    let message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

    key = preprocess(key);
    message = preprocess(message);

    const [matrix, positionMap] = createMatrix(key);
    try {
        const decryptedText = decrypt(matrix, positionMap, message);
        console.log(decryptedText);
    } catch (error) {
        console.error(error);
    }
}

main();