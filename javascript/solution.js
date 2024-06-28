function createPlayfairGrid(key) {
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

    //Replace all J with I
    key = key.replace(/J/g, "I");

    //Remove duplicates from key
    let keyGrid = [...new Set(key.split(''))];

    //Iterate through alphabet for letters not already in the key
    for (let char of alphabet) {
        if (!keyGrid.includes(char)) {
            keyGrid.push(char);
        }
    }

    //Create a 5x5 grid with the keyGrid
    let grid = [];
    for (let i = 0; i < 25; i += 5) { //Iterate by 5 to create subarrays of 5
        grid.push(keyGrid.slice(i, i + 5));
    }
    return grid;
}

function findPosition(grid, letter) {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (grid[row][col] === letter) {
                return [row, col];
            }
        }
    }
    return null;
}

function decryptDigraph(grid, digraph) {
    //Search grid for the individual letters to get their row and column
    let [a, b] = digraph.split('');
    let [rowA, colA] = findPosition(grid, a);
    let [rowB, colB] = findPosition(grid, b);

    //If same row, shift left by one
    if (rowA === rowB) {
        colA = (colA - 1 + 5) % 5;
        colB = (colB - 1 + 5) % 5;
    //If same column, shift up by one
    } else if (colA === colB) {
        rowA = (rowA - 1 + 5) % 5;
        rowB = (rowB - 1 + 5) % 5;
    //If row and column do not match, swap columns
    } else {
        [colA, colB] = [colB, colA];
    }

    //Return the two decrypted letters
    return grid[rowA][colA] + grid[rowB][colB];
}

function decryptPlayfairCipher(ciphertext, key) {
    //Ensure that ciphertext and key are uppercase
    let cleanedKey = key.toUpperCase();
    let cleanedCiphertext = ciphertext.toUpperCase();

    let grid = createPlayfairGrid(cleanedKey);
    let plaintext = "";

    for (let i = 0; i < cleanedCiphertext.length; i += 2) { //Increment by 2 to check for pairs of letters
        let digraph = cleanedCiphertext.slice(i, i + 2);
        plaintext += decryptDigraph(grid, digraph);
    }

    //Strip the plaintext of X since they are meaningless
    return plaintext.replace(/[x]/ig, '');
}

let key = "SUPERSPY";
let ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
let plaintext = decryptPlayfairCipher(ciphertext, key);

console.log(plaintext);