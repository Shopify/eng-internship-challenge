// Matthew Jiao
// May 12, 2024

// Function to create a 5x5 matrix based on a given key
const createMatrix = (key) => {
  let matrix = [];
  let seen = new Set(); // Set to track seen characters to avoid duplicates

  // Normalize the key by converting to uppercase, replacing 'J' with 'I', and removing duplicates
  key
    .toUpperCase()
    .replace(/J/g, "I") // Replace 'J' with 'I' in the key
    .split("")
    .forEach((char) => {
      if (!seen.has(char)) {
        seen.add(char);
        matrix.push(char); // Add unique character to the matrix
      }
    });

  // Fill matrix with remaining letters not in the key. Skip 'J'.
  "ABCDEFGHIKLMNOPQRSTUVWXYZ".split("").forEach((char) => {
    if (!seen.has(char)) {
      matrix.push(char); // Add remaining characters to fill the matrix
    }
  });

  return matrix;
};

// Function to decrypt the encryptedText using the matrix
const decrypt = (matrix, encryptedText) => {
  let decryptedText = "";
  // Process the encrypted text two characters at a time
  for (let i = 0; i < encryptedText.length; i += 2) {
    let a = matrix.indexOf(encryptedText[i]);
    let b = matrix.indexOf(encryptedText[i + 1]);

    // Get the row and column of the character using modular arithmetic
    let rowA = Math.floor(a / 5);
    let colA = a % 5;
    let rowB = Math.floor(b / 5);
    let colB = b % 5;

    // Same row - shift characters to the left
    if (rowA === rowB) {
      decryptedText += matrix[a - 1 < rowA * 5 ? a + 4 : a - 1];
      decryptedText += matrix[b - 1 < rowB * 5 ? b + 4 : b - 1];
    }
    // Same column - shift characters up
    else if (colA === colB) {
      decryptedText += matrix[a - 5 < 0 ? a + 20 : a - 5];
      decryptedText += matrix[b - 5 < 0 ? b + 20 : b - 5];
    }
    // Rectangle swap - swap first and second character's columns
    else {
      decryptedText += matrix[rowA * 5 + colB];
      decryptedText += matrix[rowB * 5 + colA];
    }
  }

  return decryptedText;
};

// Main function to decrypt the encryptedText using Playfair cipher
const playfairDecrypt = (key, encryptedText) => {
  const matrix = createMatrix(key); // Step 1: Create matrix from the key
  const decryptedText = decrypt(matrix, encryptedText); // Step 2: Decrypt the text using the matrix
  const finalText = decryptedText.replace(/X/g, ""); // Step 3: Remove 'X's added for padding during encryption

  return finalText;
};

// Example usage:
const testKey = "SUPERSPY";
const testEncryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"; // Fear of long words ...
console.log(playfairDecrypt(testKey, testEncryptedText));
