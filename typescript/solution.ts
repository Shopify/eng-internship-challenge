const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const cipherKey = "SUPERSPY";
const alphabetsWithoutJ = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // excluded 'J' because 'J' is usually removed or used interchangeably with 'I' in PlayFair Cipher
const pairs = encryptedMessage.match(/[A-Z]{1,2}/g) || []; // dividing the encrypted message into pairs of characters using regex
const lookup: Record<string, LetterIndex> = {};
let decryptedMessage = "";

// interface to represent the location of the letter in the matrix
interface LetterIndex {
  row: number;
  column: number;
}

// function to generate the 5x5 matrix needed for the cipher
function generateMatrix(): string[][] {
  const matrix: string[][] = [];

  // removing duplicate letters from the cipher key and the alphabets
  // creating an array of characters with the cipher key characters at the front of the alphabets
  const lettersWithoutDuplicates = Array.from(
    new Set(cipherKey + alphabetsWithoutJ)
  );
  let index = 0;

  // dynamically inserting the characters into the 5x5 matrix
  for (let char of lettersWithoutDuplicates) {
    let rowIndex = Math.floor(index / 5);
    let colIndex = index % 5;
    if (matrix.length <= rowIndex) {
      matrix.push([]);
    }
    matrix[rowIndex][colIndex] = char;
    // adding the characters into the lookup table so index retrieval becomes fast and efficient
    lookup[char] = { row: rowIndex, column: colIndex };
    index++;
  }

  return matrix;
}

const matrix = generateMatrix();

// function to handle the case where 2 letters are in the same row
// if this is the case, the letter immediately to the left of the letters are added to the decrypted message
// if the letter is the first in the row, it uses the last letter of the row as the decryption letter
function handleSameRow(
  firstLetterIndex: LetterIndex,
  secondLetterIndex: LetterIndex
) {
  decryptedMessage +=
    matrix[firstLetterIndex.row][(firstLetterIndex.column + 4) % 5] +
    matrix[secondLetterIndex.row][(secondLetterIndex.column + 4) % 5];
}

// function to handle the case where 2 letters are in the same column
// if this is the case, the letter immediately above the letters are added to the decrypted message
// if the letter is the first in the column, it uses the last letter of the column as the decryption letter
function handleSamecolumn(
  firstLetterIndex: LetterIndex,
  secondLetterIndex: LetterIndex
) {
  decryptedMessage +=
    matrix[(firstLetterIndex.row + 4) % 5][firstLetterIndex.column] +
    matrix[(secondLetterIndex.row + 4) % 5][secondLetterIndex.column];
}

// function to find and return the index of a letter
function findIndexOfLetter(letter: string): LetterIndex {
  const index = lookup[letter];
  if (!index) {
    throw new Error(`Character '${letter}' not found in lookup table.`);
  }
  return index;
}

// loop over each pair of letters, find their index in the matrix and update the decrpted message according to their position
pairs.forEach((pair) => {
  const firstLetterIndex = findIndexOfLetter(pair[0]);
  const secondLetterIndex = findIndexOfLetter(pair[1]);

  if (pair.length !== 2) {
    throw new Error(
      `Invalid pair '${pair}' encountered in the encrypted message.`
    );
  }

  if (firstLetterIndex.row === secondLetterIndex.row) {
    handleSameRow(firstLetterIndex, secondLetterIndex);
  } else if (firstLetterIndex.column === secondLetterIndex.column) {
    handleSamecolumn(firstLetterIndex, secondLetterIndex);
  } else {
    decryptedMessage +=
      matrix[firstLetterIndex.row][secondLetterIndex.column] +
      matrix[secondLetterIndex.row][firstLetterIndex.column];
  }
});

// make sure the decrypted message is all UPPERCASE with no special characters, letter 'X' or whitespaces.
const sanitizedMessage = decryptedMessage
  .toUpperCase()
  .replace(/[\sX\xX\W_]/g, "");

console.log(sanitizedMessage);
