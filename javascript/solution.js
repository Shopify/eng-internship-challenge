const ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";
const plaintext = decipher(ciphertext, key);
console.log(plaintext);

function decipher(ciphertext, key) {
    const matrix = createMatrix(key);
    const letters = {};
    // store all letters' position in matrix
    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            letters[matrix[i][j]] = [i, j];
        }
    }
        
    let plaintext = "";
    // valid ciphertext should have even length, traverse ciphertext pair by pair to decrypt it
    for (let i = 0; i + 1 < ciphertext.length; i+=2) {
        const letterA = ciphertext[i];
        const letterB = ciphertext[i + 1];
        const [row1, col1] = letters[letterA];
        const [row2, col2] = letters[letterB];
        if(row1 === row2){
            // in the same row, move left to decipher
            plaintext += matrix[row1][(col1 - 1 + 5) % 5];
            plaintext += matrix[row2][(col2 - 1 + 5) % 5];
        }else if(col1 === col2){
            // in the same col, move up to decipher
            plaintext += matrix[(row1 - 1 + 5) % 5][col1];
            plaintext += matrix[(row2 - 1 + 5) % 5][col2];
        }else{
            // shape a rectangle, use self row and another letter's col to change back
            plaintext += matrix[row1][col2];
            plaintext += matrix[row2][col1];
        }
    }
    plaintext = plaintext.replaceAll("X", "");
    return plaintext;    
}

// create a 5*5 matrix using key
// note I and J are interchangeble
function createMatrix(key) {
    const matrix = [];
    const letters = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    const set = new Set();
    let index = 0;
    // replace J in the key with I to make sure this matrix contains all letters but J.
    key = key.replaceAll('J', 'I');
    
    // add key into matrix first
    for (const letter of key) {
        if(set.has(letter)) continue;
        const row = Math.floor(index / 5);
        if(index % 5 === 0) matrix[row] = [];        
        matrix[row].push(letter);
        set.add(letter);
        index++;       
    }
    // add rest letters into matrix
    for (const letter of letters) {
        if(set.has(letter)) continue;
        const row = Math.floor(index / 5);
        if(index % 5 === 0) matrix[row] = [];        
        matrix[row].push(letter);
        set.add(letter);
        index++;
    }
    return matrix;
}