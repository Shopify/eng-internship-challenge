var message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
var key = "SUPERSPY";
// Initialize a 5x5 matrix with default values (e.g., empty strings)
var charMatrix = Array.from({ length: 5 }, function () { return Array(5).fill(''); });
// Function to search for a character in the matrix
function searchMatrix(matrix, char) {
    return matrix.some(function (row) { return row.includes(char); });
}
// Function to insert characters of a string into the matrix
function insertCharintoMatrix(matrix, c) {
    if (searchMatrix(matrix, c)) {
        return;
    }
    var row = 0;
    for (var i = 0; i < 5; i++) {
        if (matrix[i][4] == '') {
            row = i;
            break;
        }
    }
    for (var j = 0; j < 5; j++) {
        if (matrix[row][j] == '') {
            matrix[row][j] = c;
            break;
        }
    }
}
// insert key into matrix
for (var i = 0; i < key.length; i++) {
    insertCharintoMatrix(charMatrix, key[i]);
}
// insert alphabet into matrix except for letter j
for (var i = 65; i <= 90; i++) {
    if (i == 74) {
        continue;
    }
    insertCharintoMatrix(charMatrix, String.fromCharCode(i));
}
// function to return the row and column of a character in the matrix
function findChar(matrix, c) {
    for (var i = 0; i < 5; i++) {
        for (var j = 0; j < 5; j++) {
            if (matrix[i][j] == c) {
                return [i, j];
            }
        }
    }
    return [-1, -1];
}
// function to decrypt the message
function decryptMessage(matrix, message) {
    var decryptedMessage = '';
    for (var i = 0; i < message.length - 1; i += 2) {
        // get the two characters to decrypt
        var char1 = message[i];
        var char2 = message[i + 1];
        var _a = findChar(matrix, char1), row1 = _a[0], col1 = _a[1];
        var _b = findChar(matrix, char2), row2 = _b[0], col2 = _b[1];
        // if on the same row, replace with the letter to the left, with the first element replaced with the last element
        if (row1 == row2) {
            decryptedMessage += matrix[row1][col1 == 0 ? 4 : col1 - 1] + matrix[row2][col2 == 0 ? 4 : col2 - 1];
            // if on the same col, replace with the letter above, with the first element replaced with the last element
        }
        else if (col1 == col2) {
            decryptedMessage += matrix[row1 == 0 ? 4 : row1 - 1][col1] + matrix[row1 == 0 ? 4 : row1 - 1][col2];
            // otherwise construct a rectangle with the two letters and replace with the opposite corners
        }
        else {
            decryptedMessage += matrix[row1][col2] + matrix[row2][col1];
        }
    }
    // remove any extra characters that were added to the message
    decryptedMessage = decryptedMessage.replace(/X/g, '');
    // remove any spaces that were added to the message
    decryptedMessage = decryptedMessage.replace(/Z/g, ' ');
    return decryptedMessage;
}
var decryptedMessage = decryptMessage(charMatrix, message);
console.log(decryptedMessage);
