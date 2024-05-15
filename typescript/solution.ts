const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";

// Initialize a 5x5 matrix with empty values
let charMatrix: string[][] = Array.from({ length: 5 }, () => Array(5).fill(""));

// Function to search for a character in the matrix
function searchMatrix(matrix: string[][], char: string): boolean {
  return matrix.some((row) => row.includes(char));
}

// Function to insert characters of a string into the matrix
function insertCharintoMatrix(matrix: string[][], c: string): void {
  if (searchMatrix(matrix, c)) {
    return;
  }
  let row = 0;
  for (let i = 0; i < 5; i++) {
    if (matrix[i][4] == "") {
      row = i;
      break;
    }
  }
  for (let j = 0; j < 5; j++) {
    if (matrix[row][j] == "") {
      matrix[row][j] = c;
      break;
    }
  }
}

// insert key into matrix
for (let i = 0; i < key.length; i++) {
  insertCharintoMatrix(charMatrix, key[i]);
}

// insert alphabet into matrix except for letter j
for (let i = 65; i <= 90; i++) {
  if (i == 74) {
    continue;
  }
  insertCharintoMatrix(charMatrix, String.fromCharCode(i));
}

// function to return the row and column of a character in the matrix
function findChar(matrix: string[][], c: string): number[] {
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (matrix[i][j] == c) {
        return [i, j];
      }
    }
  }
  return [-1, -1];
}

// function to decrypt the message
function decryptMessage(matrix: string[][], message: string): string {
  let decryptedMessage = "";
  for (let i = 0; i < message.length - 1; i += 2) {
    // get the two characters to decrypt
    let char1 = message[i];
    let char2 = message[i + 1];
    let [row1, col1] = findChar(matrix, char1);
    let [row2, col2] = findChar(matrix, char2);
    // if on the same row, replace with the letter to the left, with the first element replaced with the last element
    if (row1 == row2) {
      decryptedMessage +=
        matrix[row1][col1 == 0 ? 4 : col1 - 1] +
        matrix[row2][col2 == 0 ? 4 : col2 - 1];
      // if on the same col, replace with the letter above, with the first element replaced with the last element
    } else if (col1 == col2) {
      decryptedMessage +=
        matrix[row1 == 0 ? 4 : row1 - 1][col1] +
        matrix[row1 == 0 ? 4 : row1 - 1][col2];
      // otherwise construct a rectangle with the two letters and replace with the opposite corners
    } else {
      decryptedMessage += matrix[row1][col2] + matrix[row2][col1];
    }
  }

  // remove any extra characters that were added to the message
  decryptedMessage = decryptedMessage.replace(/X/g, "");
  // remove any spaces that were added to the message
  decryptedMessage = decryptedMessage.replace(/Z/g, " ");
  return decryptedMessage;
}

let decryptedMessage: string = decryptMessage(charMatrix, message);
console.log(decryptedMessage);