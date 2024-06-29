//encrypted message
const ENCRYPTED_MESSAGE = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

//cipher key
const CIPHER_KEY = "SUPERSPY";

/**
 *
 * @param {Array} cipherKey An cipher keyphrase to use as the basis of a Playfair cipher matrix
 * @param {Number} squareSize The intended size of the matrix
 * @returns {Array} An array of squareSize * squareSize dimensions made from the cipher keyphrase given to it
 */
function generateCipherMatrix(cipherKey, squareSize) {
  //establish a Set of letters starting with the cipher key,
  const letterSet = new Set(cipherKey.split(""));

  //add the remaining alphabet letters that have not been used yet, omitting J so that there are 25 letters in total
  const ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  ALPHABET.split("").forEach((letter) => {
    letterSet.add(letter);
  });

  //turn set into an array to facilitate removing one letter at a time
  const letterArray = Array.from(letterSet);

  const matrix = [];
  for (let row = 0; row < squareSize; row++) {
    matrix.push([]);

    for (let col = 0; col < squareSize; col++) {
      matrix[row].push(letterArray.shift());
    }
  }
  return matrix;
}

/**
 *
 * @param {Array} matrix A nested array representing a matrix of values
 * @returns {Array} A nested array where the top level items are now arrays representing the columns of the given matrix rather than the rows
 */
function generateColumnsFromMatrix(matrix) {
  columnSet = [];
  for (let col = 0; col < matrix[0].length; col++) {
    columnSet.push([]);

    for (let row = 0; row < matrix[0].length; row++) {
      columnSet[col].push(matrix[row][col]);
    }
  }
  return columnSet;
}

/**
 *
 * @param {String} encryptedMessage A string made of text that was encrypted using the Playfair cipher, which will have an even number of letters if properly created
 * @returns {Array} An array where each element is a two-letter pair of the encrypted message
 */
function generateLetterPairs(encryptedMessage) {
  const encryptedArray = encryptedMessage.split("");
  const letterPairs = [];
  for (let i = 0; i < encryptedArray.length; i += 2) {
    letterPairs.push([encryptedArray[i], encryptedArray[i + 1]]);
  }
  return letterPairs;
}

/**
 * 
 * @param {String} encrypted A set of text encrypted by a Playfair cipher method
 * @param {String} key The keyphrase meant to be used to decrypt the message
 * @returns {String} The decrypted message, set to uppercase, where spaces, the letter X, and special characters are removed
 */
function decryptMessage(encrypted, key) {
  //take the cipher key and use it to make a 5x5 matrix
  const cipherMatrix = generateCipherMatrix(key, 5);

  //the cipherMatrix rows are easily accessible, now build a collection of its columns for similar ease of iteration below
  const cipherColumns = generateColumnsFromMatrix(cipherMatrix);

  //break the encrypted message into letter pairs
  const encryptedLetterPairs = generateLetterPairs(encrypted);

  //iterate through letter pairings to check for decrypting conditions
  let decryptedMessage = "";

  encryptedLetterPairs.forEach((letterPair) => {

    let lettersAreInRow;
    let lettersAreInColumn;

    //check letter pair to see if they are in the same row of the matrix
    for (let row = 0; row < cipherMatrix.length; row++) {
      const thisRow = cipherMatrix[row];
      lettersAreInRow =
        thisRow.includes(letterPair[0]) && thisRow.includes(letterPair[1]);

      if (lettersAreInRow) {
        //add decrypted letters to decryptedMessage by
        //getting index of letterPair[0] and letterPair[1] and taking one index to the left, wrapping around as needed
        const encryptedLetter1RowIndex = thisRow.indexOf(letterPair[0]);
        const encryptedLetter2RowIndex = thisRow.indexOf(letterPair[1]);

        //if moving one cell to the left creates a negative index number, wrap around to the rightmost cell by adding 4 to the index
        const decryptedLetter1RowIndex =
          encryptedLetter1RowIndex - 1 >= 0
            ? encryptedLetter1RowIndex - 1
            : encryptedLetter1RowIndex + 4;

        const decryptedLetter2RowIndex =
          encryptedLetter2RowIndex - 1 >= 0
            ? encryptedLetter2RowIndex - 1
            : encryptedLetter2RowIndex + 4;

        decryptedMessage +=
          thisRow[decryptedLetter1RowIndex] + thisRow[decryptedLetter2RowIndex];

        //if the letters have been found in the same row, the rest of the search for columns can be skipped for this pair
        break;
      }
    }

    if (lettersAreInRow) return;

    //if not in the same row, then check letter pair to see if they are in the same column of the matrix
    for (let col = 0; col < cipherColumns.length; col++) {
      const thisColumn = cipherColumns[col];
      lettersAreInCol =
        thisColumn.includes(letterPair[0]) && thisColumn.includes(letterPair[1]);

      if (lettersAreInCol) {
        //add decrypted letters to decryptedMessage by
        //getting index of letterPair[0] and letterPair[1] and taking one index higher up the column, wrapping around as needed
        const encryptedLetter1ColIndex = thisColumn.indexOf(letterPair[0]);
        const encryptedLetter2ColIndex = thisColumn.indexOf(letterPair[1]);

        //if moving one cell up in the column creates a negative number, wrap around to the bottom of the column by adding 4 to the index
        const decryptedLetter1ColIndex =
          encryptedLetter1ColIndex - 1 >= 0
            ? encryptedLetter1ColIndex - 1
            : encryptedLetter1ColIndex + 4;

        const decryptedLetter2ColIndex =
          encryptedLetter2ColIndex - 1 >= 0
            ? encryptedLetter2ColIndex - 1
            : encryptedLetter2ColIndex + 4;

        decryptedMessage +=
          thisCol[decryptedLetter1ColIndex] + thisCol[decryptedLetter2ColIndex];

        //if the letters have been found in the same columnn, the rest of the search for boxes can be skipped for this pair
        break;
      }
    }

    if (lettersAreInColumn) return;
    //if not in same row or column, establish the box between these letters as the corner points and get the other corners as the decrypted letters
    
    //the decrypted letter will exist on the same row as the encrypted letter,
    //and while the letters may appear in different order in the box,
    //the letters when decrypted must still be added in the same order in which the encrypted letters were places

    //check through all the rows to see which row co-ordinate the first letter is at
    let firstLetterRow;
    for (
      firstLetterRow = 0;
      firstLetterRow < cipherMatrix.length;
      firstLetterRow++
    ) {
      if (cipherMatrix[firstLetterRow].includes(letterPair[0])) break;
    }

    //get column index of first letter
    let firstLetterCol = cipherMatrix[firstLetterRow].indexOf(letterPair[0]);

    //check through all the rows to see which row co-ordinate the second letter is at
    let secondLetterRow;
    for (
      secondLetterRow = 0;
      secondLetterRow < cipherMatrix.length;
      secondLetterRow++
    ) {
      if (cipherMatrix[secondLetterRow].includes(letterPair[1])) break;
    }
    //get column index of second letter
    let secondLetterCol = cipherMatrix[secondLetterRow].indexOf(letterPair[1]);

    //get the first letter's row, at the column index of the second letter, to decrypt first letter
    decryptedMessage += cipherMatrix[firstLetterRow][secondLetterCol];

    //get the second letter's row, at the column index of the first letter, to decrypt second letter
    decryptedMessage += cipherMatrix[secondLetterRow][firstLetterCol];
  });

  //output must be in upper case, not include spaces, the letter X, or special characters
  return decryptedMessage
    .toUpperCase()
    .replaceAll("X", "")
    .replace(/[^A-Z]/g, "");
}

//decrypted message
const DECRYPTED_MESSAGE = decryptMessage(ENCRYPTED_MESSAGE, CIPHER_KEY);

//output decrypted message
console.log(DECRYPTED_MESSAGE);
