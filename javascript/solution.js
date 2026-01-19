// Playfair Cipher Solver

// Function to generate the Playfair cipher key matrix
function generateKeyMatrix(key) {
  key = key.toUpperCase().replace(/[^A-Z]/g, ""); // Ensure key is uppercase and remove non-alphabetic characters
  key = key.replace(/J/g, "I"); // Replace J with I as per Playfair cipher rules

  let matrix = [];
  let alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
  let used = new Set();

  // Fill matrix with key characters
  for (let char of key) {
    if (!used.has(char)) {
      matrix.push(char);
      used.add(char);
    }
  }

  // Fill remaining matrix with other letters
  for (let char of alphabet) {
    if (!used.has(char)) {
      matrix.push(char);
      used.add(char);
    }
  }

  // Convert flat array to 5x5 matrix
  let keyMatrix = [];
  for (let i = 0; i < 25; i += 5) {
    keyMatrix.push(matrix.slice(i, i + 5));
  }

  return keyMatrix;
}

// Function to find the position of a character in the key matrix
function findPosition(matrix, char) {
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 5; col++) {
      if (matrix[row][col] === char) {
        return { row, col };
      }
    }
  }
}

// Function to decrypt the Playfair cipher text
function decryptPlayfair(cipherText, keyMatrix) {
  let decryptedText = "";

  for (let i = 0; i < cipherText.length; i += 2) {
    let char1 = cipherText[i];
    let char2 = cipherText[i + 1];

    let pos1 = findPosition(keyMatrix, char1);
    let pos2 = findPosition(keyMatrix, char2);

    if (pos1.row === pos2.row) {
      // Same row
      decryptedText += keyMatrix[pos1.row][(pos1.col + 4) % 5];
      decryptedText += keyMatrix[pos2.row][(pos2.col + 4) % 5];
    } else if (pos1.col === pos2.col) {
      // Same column
      decryptedText += keyMatrix[(pos1.row + 4) % 5][pos1.col];
      decryptedText += keyMatrix[(pos2.row + 4) % 5][pos2.col];
    } else {
      // Rectangle
      decryptedText += keyMatrix[pos1.row][pos2.col];
      decryptedText += keyMatrix[pos2.row][pos1.col];
    }
  }

  return decryptedText;
}

// Main function to run the decryption
function main() {
  const cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
  const key = "SUPERSPY";

  const keyMatrix = generateKeyMatrix(key);
  const decryptedText = decryptPlayfair(cipherText, keyMatrix);

  // Output the decrypted text in uppercase and without special characters
  console.log(decryptedText.replace(/[^A-Z]/g, ""));
}

// Execute the main function
main();
