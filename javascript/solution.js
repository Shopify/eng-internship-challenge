const key = "SUPERSPY";
const encryptedString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

console.log(createPlayfairCipher(key, encryptedString));

// Function to create the Playfair cipher
function createPlayfairCipher(key, encryptedString){
    // Converting key and encrypted string to uppercase
    key = key.toUpperCase();
    encryptedString = encryptedString.toUpperCase();
    // Removing duplicate characters from the key
    var keyArray = key.split("").filter(char => /[A-Z]/.test(char));
    let uniqueKey = [...new Set(keyArray)];
    key = uniqueKey.join('');

    // Creating the Playfair matrix
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
    key += alphabet;
    var keyArraySplitted = key.split('');
    let uniqueKeySplitted = [...new Set(keyArraySplitted)];
    key = uniqueKeySplitted.join('');
    var matrix = createMatrix(key);

    // Decrypting the encrypted string using the matrix
    var decryptedString = decryptPlayfair(encryptedString, matrix);
    decryptedString = decryptedString.replace(/[^\w\s]|X/g, '');
    return decryptedString;
}

// Function to create the Playfair matrix
function createMatrix(key){
    var matrix = [];
    var row = [];
    for(var i = 0; i <= key.length; i++){
        if(row.length == 5){
            matrix.push(row);
            row = [];
        }
        row.push(key[i]);
    }
    return matrix;
}

// Function to decrypt the encrypted string
function decryptPlayfair(encryptedString, matrix){
    // Divide the encrypted string into pairs of two characters
    let pairs = [];
    let decryptedText = "";
    for(var i = 0; i < encryptedString.length; i+=2){
        let pair = encryptedString.slice(i, i + 2);
        pairs.push(pair);
    }

    // Decrypting each pair of characters
    for(let pair of pairs){
        var char1 = pair[0];
        var char2 = pair[1];

        var char1Position = findPosition(char1, matrix);
        var char2Position = findPosition(char2, matrix);
        if(char1Position && char2Position){
            if(char1Position.row === char2Position.row){
                decryptedText += matrix[char1Position.row][(char1Position.col + 4) % 5];
                decryptedText += matrix[char2Position.row][(char2Position.col + 4) % 5];
            }
            else if(char1Position.col === char2Position.col){
                decryptedText += matrix[(char1Position.row + 4) % 5][char1Position.col];
                decryptedText += matrix[(char2Position.row + 4) % 5][char2Position.col];
            }
            else{
                decryptedText += matrix[char1Position.row][char2Position.col];
                decryptedText += matrix[char2Position.row][char1Position.col];
            }
        }
        else{
            decryptedText += " ";
        }
    }
    return decryptedText;
}

// Function to find the position of a character in the Playfair matrix
function findPosition(char, matrix){
    for (var i = 0; i < matrix.length; i++) {
        for (var j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === char) {
                return {row: i, col: j};
            }
        }
    }
    return null;
}
