function generateKeyMatrix(key) {
  //matrix needs to be 5x5
  const size = 5;
  let matrix = new Array(size).fill().map(() => new Array(size).fill(null));
  //convert to lowercase, ensure no special characters
  let keyString = key
    .toLowerCase()
    .replace(/[^a-z]/g, "")
    .replace(/j/g, "i");

  //create a new Set, ensures no duplicates
  let set = new Set();

  keyString.split("").forEach((c) => {
    set.add(c);
  });
  //exclude j from the alphabet
  "abcdefghiklmnopqrstuvwxyz".split("").forEach((c) => {
    if (!set.has(c)) {
      set.add(c);
    }
  });

  if (set.size !== 25) {
    throw new Error("Set does not contain 25 unique characters.");
  }

  //convert back to array in order to have access to index
  const characters = Array.from(set);
  let index = 0;
  for (let row = 0; row < size; row++) {
    for (let col = 0; col < size; col++) {
      matrix[row][col] = characters[index++];
    }
  }
  return matrix;
}

function findPosition(matrix, char) {
  char = char.toLowerCase();
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (matrix[row][col] === char) {
        return { row, col };
      }
    }
  }
  return null;
}

function decrypt(matrix, encryptedText) {
  encryptedText = encryptedText.replace(/j/g, "i").toLowerCase();
  let decryptedText = "";
  if (encryptedText.length % 2 !== 0) {
    encryptedText += "x"; // add an x if the text length is odd
  }

  for (let i = 0; i < encryptedText.length; i += 2) {
    let pair1 = encryptedText[i];
    let pair2 = encryptedText[i + 1];
    let pos1 = findPosition(matrix, pair1);
    let pos2 = findPosition(matrix, pair2);

    if (!pos1 || !pos2) {
      console.error("Position not found for pair:", pair1, pair2);
      continue;
    }

    // if the characters in the pair are in the same row
    if (pos1.row === pos2.row) {
      decryptedText += matrix[pos1.row][(pos1.col - 1 + 5) % 5];
      decryptedText += matrix[pos2.row][(pos2.col - 1 + 5) % 5];
    }
    // if the characters in the pair are in the same column
    else if (pos1.col === pos2.col) {
      decryptedText += matrix[(pos1.row - 1 + 5) % 5][pos1.col];
      decryptedText += matrix[(pos2.row - 1 + 5) % 5][pos2.col];
    }
    // Rectangle/box rule
    else {
      decryptedText += matrix[pos1.row][pos2.col];
      decryptedText += matrix[pos2.row][pos1.col];
    }
  }

  //output to be in uppercase, contain no x
  decryptedText = decryptedText
    .toUpperCase()
    .replace(/X/g, "")
    .replace(/[^A-Z]/g, "");
  return decryptedText;
}

let key = "SUPERSPY";
let encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
let keyMatrix = generateKeyMatrix(key);
let decryptedText = decrypt(keyMatrix, encryptedText);

console.log(decryptedText);
