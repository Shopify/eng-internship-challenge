const decrypt = (message, key) => {
    message = formatMessage(message);
    key = key.replace(/J/g, 'I').toUpperCase().replace(/[^A-Z]/g, '');
    let [matrix, dictionary] = buildMatrix(key);
    let decryptedMessage = decipher(message, key, matrix, dictionary);
    return decryptedMessage;
}

const decipher = (message, key, matrix, dictionary) => {

    let decryptedMessage = "";
    for (let i = 0; i < message.length; i += 2) {
        let pair = message.substr(i, 2);

        let firstChar = pair[0];
        let secondChar = pair[1];
        let firstPos = dictionary.get(firstChar);
        let secondPos = dictionary.get(secondChar);

        if (firstPos[0] == secondPos[0]) { // same row
            // In JS, negative modulo returns negative number, to revent this I added n (5) to each shifted coordinate
            decryptedMessage += matrix[firstPos[0]][((firstPos[1] - 1) + 5) % 5];
            decryptedMessage += matrix[secondPos[0]][((secondPos[1] - 1) + 5) % 5];
        }
        else if (firstPos[1] == secondPos[1]) {  // same column
            decryptedMessage += matrix[((firstPos[0] - 1) + 5) % 5][firstPos[1]];
            decryptedMessage += matrix[((secondPos[0] - 1) + 5) % 5][secondPos[1]];
        }
        else { // forming a rectangle
            decryptedMessage += matrix[firstPos[0]][secondPos[1]];
            decryptedMessage += matrix[secondPos[0]][firstPos[1]];
        }
    }
    decryptedMessage = decryptedMessage.replace(/X/g, '') // remove all the X's
    return decryptedMessage;
}

const buildMatrix = (key) => {
    let alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // Omitting J as suggested by the Wiki
    let matrixChar = buildKeyString(key + alphabet);
    let matrix = [];
    let dictionary = new Map(); // creating a dictionary to record each alphabet's coordinate in the matrix to reduce algorithmic complexity
    let count = 0;
    for (let i = 0; i < 5; ++i) {
        let currRow = [];
        for (let j = 0; j < 5; ++j) {
            currRow.push(matrixChar.charAt(count));
            dictionary.set(matrixChar.charAt(count++), [i, j]);
        }
        matrix.push(currRow);
    }
    return [matrix, dictionary];
}

const formatMessage = (message) => {
    // since we are omitting J in the matrix, we will replace J with I in our inputs
    message = message.replace(/J/g, 'I').toUpperCase().replace(/[^A-Z]/g, ''); // input validation to remove non alphabets
    let formatedMessage = "";
    let messageLen = message.length;
    let i = 0;
    while (i < messageLen) {
        if (i != messageLen - 1 && message.charAt(i) != message.charAt(i + 1)) { // if the pair are not the same, we add it to formatedMessage
            formatedMessage += message.charAt(i) + message.charAt(i + 1);
            i += 2;
        } else {
            formatedMessage += message.charAt(i++) + "X"; // if they are we inset an "X" after the first letter
        }
    }
    if (formatedMessage.length % 2 != 0) formatedMessage += "X"; // if the formatedMessage is odd length, append an "X" at the end
    return formatedMessage;
}

const buildKeyString = (input) => {
    let seen = [];
    let res = "";
    input.split("").forEach((char) => {
        if (!seen.includes(char)) { // if we haven't seen the character, concat to result and add to seen
            res += char;
            seen.push(char);
        }
    })
    return res;
}
let a = decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY");
console.log(a);
let b = decrypt("gatlmzclrqt", "mo0234*(#$na   rchy");
console.log(b);
let c = decrypt("GRVOIFAYFPPCHV", "PLAYFAIRCIPHER");
console.log(c);