/*
  1 - Generate a 5 x 5 matrix
      - Use key "SUPERSPY"
      - Organize in 5 x 5 matrix using key and the alphabet letters from 'A' to 'Z' except 'J', as it is merged with 'I'
  2 - Find location of the key letter in the matrix
  3 - Decrypt the cipher
      - If both letters are the same (or only one letter is left), add an "X" after the first letter. Encrypt the new pair and continue.
      - If the letters appear on the same row of your table, replace them with the letters to their immediate right respectively.
      - If the letters appear on the same column of your table, replace them with the letters immediately below respectively.
      - If the letters are not on the same row or column, replace them with the letters on the same row respectively but at the other pair of corners of the rectangle.
  4 - Read the messasges and print it out
      - Decrypted string must by entirely **UPPER CASE**
      - Do not include `spaces`, the letter `"X"`, or `special characters`.
      - Ensure you meet all these conditions before outputting the result.
*/


// Generate a 5 x 5 matrix
function generateMatrix(key) {
  key = key.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '')
  const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ';
  const rawMatrix = [];
  let usedChar = new Set();

  // Add key to the raw list (unorganized)
  for (let char of key) {
    if (!usedChar.has(char)){
      rawMatrix.push(char);
      usedChar.add(char);
    }
  }

  // Add the rest of the alphabet to the raw list (unorganized)
  for (let char of alphabet){
    if (!usedChar.has(char)){
      rawMatrix.push(char);
      usedChar.add(char);
    }
  }

  // Organize/Split the raw list into 5 x 5 organized matrix
  const playfairCipherMatrix = [];
  for (let i = 0; i < 5; i ++){
    playfairCipherMatrix.push(rawMatrix.slice(i * 5, i * 5 + 5));
  }
  return playfairCipherMatrix;
}


// Find the location of the key letter in the matrix
function findLocation(matrix, letter){
  for (let i = 0; i < 5; i ++){
    for (let j = 0; j < 5; j ++) {
      if (matrix[i][j] === letter){
        return [i, j];
      }
    }
  }
  return null;
}

// Decrypt the pair of letters in the cipher matrix
function decryptPair(pair, matrix){
  let [a, b] = pair;
  let [arow, acol] = findLocation(matrix, a);
  let [brow, bcol] = findLocation(matrix, b);

  if (arow === brow) {
    // Shift letters left
    return matrix[arow][(acol + 4) % 5] + matrix[brow][(bcol + 4) % 5]
  }
  else if (acol === bcol) {
    // same column, shift letters up
    return matrix[(arow + 4) / 5][acol] + matrix[(brow + 4) / 5][bcol];
  }
  else {
    // swap corners
    return matrix[arow][bcol] + matrix[brow][acol];
  }
}

// Read the messages and print it out
function decryptCipherMsgs(cipherMessage, key) {
  const matrix = generateMatrix(key);
  let decryptedMsg = '';

  for (let i = 0; i < cipherMessage.length; i += 2) {
    let char1 = cipherMessage[i]; 
    // if there is no char2 left
    let char2 = i + 1 < cipherMessage.length ? cipherMessage[i + 1]: 'X';

    // if duplicate letters, add a 'X' after char1 and release char2 by minus 1
    if (char1 === char2) {
      char2 = 'X';
      i --;
    }
    decryptedMsg += decryptPair([char1, char2], matrix);
  }

  // remove 'X' from the decrypted message, print out and return
  console.log(decryptedMsg.replace(/X/g, ''));
  return decryptedMsg.replace(/X/g, '');
}

const encryptedMsgs = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
const key = 'SUPERSPY';
const decryptedMsgs = decryptCipherMsgs(encryptedMsgs, key);