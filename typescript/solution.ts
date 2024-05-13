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

function main() {
    const key = "SUPERSPY";
    const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

    const matrix = createMatrix(key);
}