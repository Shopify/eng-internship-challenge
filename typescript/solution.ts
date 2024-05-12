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

function handleSameRow(index1: LetterIndex, index2: LetterIndex) {
  decryptedMessage +=
    matrix[index1.row][
      index1.column - 1 >= 0 ? index1.column - 1 : index1.column + 4
    ] +
    matrix[index2.row][
      index2.column - 1 >= 0 ? index2.column - 1 : index2.column + 4
    ];
}

function handleSamecolumn(index1: LetterIndex, index2: LetterIndex) {
  decryptedMessage +=
    matrix[index1.row - 1 >= 0 ? index1.row : index1.row + 4][index1.column] +
    matrix[index2.row - 1 >= 0 ? index2.row : index2.row + 4][index2.column];
}

pairs.forEach((pair) => {
  const indexOfL1 = lookup[pair[0]];
  const indexOfL2 = lookup[pair[1]];

  if (indexOfL1.row === indexOfL2.row) {
    handleSameRow(indexOfL1, indexOfL2);
    return;
  }

  if (indexOfL1.column === indexOfL2.column) {
    handleSamecolumn(indexOfL1, indexOfL2);
    return;
  }

  decryptedMessage +=
    matrix[indexOfL1.row][indexOfL2.column] +
    matrix[indexOfL2.row][indexOfL1.column];
});

function sanitizeMessage(message: string) {
  const sanitizedMessage = message.toUpperCase().replace(/[\sX\xX\W_]/g, "");
  return sanitizedMessage;
}
console.log(sanitizeMessage(decryptedMessage));
