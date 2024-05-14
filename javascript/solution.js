/* 
- Create 5 x 5 matrix 
  - Use key "SUPERSPY"
  - Remove duplicate letters, special characters, and numbers
  - Contains all letters except letter J (merged with letter I)

- Find position (row and column) of a given charater in the matrix (need to create function for this)
- Decrypt the cipher
  - Decrpit the cipher by finding the position of each pair of characters in the matrix
  - If the characters are in the same row, replace them with the characters to their immediate right
  - If the characters are in the same column, replace them with the characters immediately below
  
- Read encrypted message and print final results
  - Your decrypted string must by entirely UPPER CASE
  - DON'T include spaces, the letter "X", or special characters. 
  - Ensure you meet all these conditions before outputting the result.
  - ONLY output the decrypted Playfair Cipher string (ex. "BANANAS" and not "the message is BANANAS")

*/

// Create 5 x 5 matrix
// Uppercase letters only, remove special characters/numbers, replace J with I

function generateMatrix(key) {
  key = key
    .toUpperCase()
    .replace(/J/g, "I")
    .replace(/[^A-Z]/g, "")

  const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  let usedChar = new Set()
  let matrix = []

  // Add characters from the key to the matrix
  for (let char of key) {
    if (!usedChar.has(char)) {
      matrix.push(char)
      usedChar.add(char)
    }
  }

  // Add remaining alphabet characters (not including J) to the matrix
  for (let char of alphabet) {
    if (!usedChar.has(char)) {
      matrix.push(char)
      usedChar.add(char)
    }
  }

  // Convert the array into a 5 x 5 matrix
  let playfairMatrix = []

  for (let i = 0; i < 5; i++) {
    playfairMatrix.push(matrix.slice(i * 5, i * 5 + 5))
  }
  return playfairMatrix
}

// Find the position (row and column) of a given character in the matrix
function findCharPosition(matrix, char) {
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (matrix[i][j] === char) {
        return [i, j]
      }
    }
  }
  return null
}

// Decrypt the pairs of characters in the matrix
function decryptCipherPairs(pair, matrix) {
  let [char1, char2] = pair
  let [row1, col1] = findCharPosition(matrix, char1)
  let [row2, col2] = findCharPosition(matrix, char2)

  if (row1 === row2) {
    // Same row, shift left
    return matrix[row1][(col1 + 4) % 5] + matrix[row2][(col2 + 4) % 5]
  } else if (col1 === col2) {
    //same column, shift up
    return matrix[(row1 + 4) % 5][col1] + matrix[(row2 + 4) % 5][col2]
  } else {
    // Rectangle swap
    return matrix[row1][col2] + matrix[row2][col1]
  }
}

// Decrypt the cipher message using the key
function decryptCipher(cipherMessage, key) {
  let matrix = generateMatrix(key)
  let solution = ""

  for (let i = 0; i < cipherMessage.length; i += 2) {
    let char1 = cipherMessage[i]
    let char2 = i + 1 < cipherMessage.length ? cipherMessage[i + 1] : "X"

    // If duplicate letter, add an "X"
    if (char1 === char2) {
      char2 = "X"
      i--
    }
    solution += decryptCipherPairs([char1, char2], matrix)
  }
  // Remove the "X" characters from the final solution
  console.log(solution.replace(/X/g, ""))
  return solution.replace(/X/g, "")
}

// Read encrypted message
const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
const key = "SUPERSPY"
const decryptedMessage = decryptCipher(encryptedMessage, key)
