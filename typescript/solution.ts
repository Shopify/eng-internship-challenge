const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const cipherKey = "SUPERSPY";
const alphabetsWithoutJ = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
const pairs = encryptedMessage.match(/[A-Z]{1,2}/g) || [];
let decryptedMessage = "";
const lookup: Record<string, LetterIndex> = {};

interface LetterIndex {
  row: number;
  column: number;
}

function generateMatrix(): string[][] {
  const matrix: string[][] = [];
  const lettersWithoutDuplicates = Array.from(
    new Set(cipherKey + alphabetsWithoutJ)
  );
  let index = 0;

  for (let char of lettersWithoutDuplicates) {
    let rowIndex = Math.floor(index / 5);
    let colIndex = index % 5;
    if (matrix.length <= rowIndex) {
      matrix.push([]);
    }
    matrix[rowIndex][colIndex] = char;
    lookup[char] = { row: rowIndex, column: colIndex };
    index++;
  }

  return matrix;
}

const matrix = generateMatrix();

function handleSameRow(
  firstLetterIndex: LetterIndex,
  secondLetterIndex: LetterIndex
) {
  decryptedMessage +=
    matrix[firstLetterIndex.row][(firstLetterIndex.column + 4) % 5] +
    matrix[secondLetterIndex.row][(secondLetterIndex.column + 4) % 5];
}

function handleSamecolumn(
  firstLetterIndex: LetterIndex,
  secondLetterIndex: LetterIndex
) {
  decryptedMessage +=
    matrix[(firstLetterIndex.row + 4) % 5][firstLetterIndex.column] +
    matrix[(secondLetterIndex.row + 4) % 5][secondLetterIndex.column];
}

function findIndexOfLetter(letter: string): LetterIndex {
  const index = lookup[letter];
  if (!index) {
    throw new Error(`Character '${letter}' not found in lookup table.`);
  }
  return lookup[letter];
}

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

const sanitizedMessage = decryptedMessage
  .toUpperCase()
  .replace(/[\sX\xX\W_]/g, "");

console.log(sanitizedMessage);
