const MATRIX_SIZE = 5; // Size of the cipher matrix (5x5)

function createCipherMatrix(key) {
  const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'; // alphabet without 'J'
  let matrix = []; // array to store the cipher matrix
  let keyTable = {}; // object to store the key table

  // Prepare key: convert to upper case, replace 'J' with 'I', and remove non-alphabet characters
  key = key.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');

  // Remove duplicates from key and combine with alphabet
  let fullKey = [...new Set(key + alphabet)].join('');

  // Populate cipher matrix and create lookup table
  for (let i = 0, max = MATRIX_SIZE * MATRIX_SIZE; i < max; i++) {
    let row = Math.floor(i / MATRIX_SIZE);
    let col = i % MATRIX_SIZE;
    let char = fullKey[i];
    if (!matrix[row]) {
      matrix[row] = [];
    }
    matrix[row][col] = char;
    keyTable[char] = { row, col };
  }

  return { matrix, keyTable };
}

function decryptPlayfairCipher(key, message) {
  // Create the cipher matrix and key lookup table
  let { matrix, keyTable } = createCipherMatrix(key);
  
  let decryptedMessage = '';
  // Prepare cipher text: uppercase and replace 'J' with 'I'
  message = message.toUpperCase().replace(/J/g, 'I').replace(/[^A-Z]/g, '');

  // Check if the encrypted message length is even
  if (message.length % 2 !== 0) {
    throw new Error('Encrypted message length should be even.');
  }

  // Decrypt message by processing digraphs
  for (let i = 0; i < message.length; i += 2) {
    let pair1 = keyTable[message[i]];
    let pair2 = keyTable[message[i + 1]];

    let row1 = pair1.row, col1 = pair1.col;
    let row2 = pair2.row, col2 = pair2.col;

    if (row1 === row2) {
      // If pairs are in the same row, shift columns left
      decryptedMessage += matrix[row1][(col1 + MATRIX_SIZE - 1) % MATRIX_SIZE];
      decryptedMessage += matrix[row2][(col2 + MATRIX_SIZE - 1) % MATRIX_SIZE];
    } else if (col1 === col2) {
      // If pairs are in the same column, shift rows up
      decryptedMessage += matrix[(row1 + MATRIX_SIZE - 1) % MATRIX_SIZE][col1];
      decryptedMessage += matrix[(row2 + MATRIX_SIZE - 1) % MATRIX_SIZE][col2];
    } else {
      // Otherwise, swap columns between pairs
      decryptedMessage += matrix[row1][col2];
      decryptedMessage += matrix[row2][col1];
    }
  }

  // Remove 'X' before returning decrypted message
  decryptedMessage = decryptedMessage.replace(/X/g, '');
  return decryptedMessage;
}

const decryptedMessage = decryptPlayfairCipher('SUPERSPY', 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV');
console.log(decryptedMessage);