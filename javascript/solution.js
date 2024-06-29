/**
 * Creates a 5x5 Playfair cipher matrix based on a keyword.
 * @param {string} keyword - The keyword to base the matrix on.
 * @returns {Array} The Playfair cipher matrix.
 */
const createPlayfairMatrix = (keyword) => {
  const matrix = [];
  const seen = new Set();
  const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'; // 'J' is not included

  //Add keyword to matrix
  for (let char of keyword) {
    if (!seen.has(char)) {
      matrix.push(char);
      seen.add(char);
    }
  }

  //Add remaining characters to matrix
  for (let char of alphabet) {
    if (!seen.has(char)) {
      matrix.push(char);
      seen.add(char);
    }
  }
  return matrix;
};

/**
 * Gets the position of a character in the Playfair cipher matrix.
 * @param {string} char - The character to find.
 * @param {Array} matrix - The Playfair cipher matrix.
 * @returns {Array} The [row, column] position of the character.
 */
const getCharposition = (char, matrix) => {
  const index = matrix.indexOf(char);
  return [Math.floor(index / 5), index % 5];
};

/**
 * Decrypts a pair of characters using the Playfair cipher rules.
 * @param {string} pair - The pair of characters to decrypt.
 * @param {Array} matrix - The Playfair cipher matrix.
 * @returns {string} The decrypted pair of characters.
 */
const decryptPair = (pair, matrix) => {
  const [firstChar, secondChar] = pair;
  const [row1, col1] = getCharposition(firstChar, matrix);
  const [row2, col2] = getCharposition(secondChar, matrix);

  let decryptedPair = '';

  //if two characters are in the same row
  if (row1 === row2) {
    decryptedPair += matrix[row1 * 5 + ((col1 + 4) % 5)];
    decryptedPair += matrix[row2 * 5 + ((col2 + 4) % 5)];
  }
  //if two characters are in the same column
  else if (col1 === col2) {
    decryptedPair += matrix[((row1 + 4) % 5) * 5 + col1];
    decryptedPair += matrix[((row2 + 4) % 5) * 5 + col2];
  }
  //if two characters are in a rectangle position
  else {
    decryptedPair += matrix[row1 * 5 + col2];
    decryptedPair += matrix[row2 * 5 + col1];
  }
  return decryptedPair;
};

/**
 * Decrypts a Playfair cipher text using a given keyword.
 * @param {string} text - The encrypted text.
 * @param {string} keyword - The keyword used to create the Playfair cipher matrix.
 * @returns {string} The decrypted text.
 */
const decryptPlayfairCipher = (text, keyword) => {
  const matrix = createPlayfairMatrix(keyword);

  let decryptedText = '';

  for (let i = 0; i < text.length; i += 2) {
    const pair = text.substring(i, i + 2);
    decryptedText += decryptPair(pair, matrix);
  }
  return decryptedText.replace(/X/g, ''); //removing padding 'X'
};

/**
 * Main function to decrypt the given ciphertext using the Playfair cipher.
 */
function main() {
  const ciphertext = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
  const keyword = 'SUPERSPY';

  const decryptedText = decryptPlayfairCipher(ciphertext, keyword);

  console.log(decryptedText);
}

main();
