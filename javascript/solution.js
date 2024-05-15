/**
 * Playfair's Cipher Decryption
 * Author: Cui Shen Yi https://www.linkedin.com/in/shenyicui/
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 * n is defined as the length of the text
 */

// Constants
const key = "SUPERSPY";
const text = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // Alphabet without J
const positions = {}; // Positions of the characters in the matrix

// Step 1: Create the matrix
// [Constant time operation O(1)] [Constant space operation O(1)]
const matrix = [];
const keySet = new Set(key.split(""));
for (let char of alphabet) {
  if (!keySet.has(char)) {
    keySet.add(char);
  }
}
const keyArr = Array.from(keySet);
for (let i = 0; i < 5; i++) {
  matrix.push(keyArr.slice(i * 5, i * 5 + 5));
}

// Store the positions of the characters in the matrix
// [Constant time operation O(1)] [Constant space operation O(1)]
for (let i = 0; i < 5; i++) {
  for (let j = 0; j < 5; j++) {
    positions[matrix[i][j]] = [i, j];
  }
}

// Step 2: Create the pairs
// [Linear time operation O(n)] [Linear space operation O(n)]
const pairs = [];
const textArr = text.split(""); // More efficient than using text.slice(0, 2) in the loop
for (let i = 0; i < textArr.length; i += 2) {
  if (i === textArr.length - 1) {
    pairs.push([textArr[i], "X"]);
  } else if (textArr[i] === textArr[i + 1]) {
    pairs.push([textArr[i], "X"]);
    i--;
  } else {
    pairs.push([textArr[i], textArr[i + 1]]);
  }
}

// Step 3: Decrypt the text
// [Linear time operation O(n)] [Linear space operation O(n)]
let decryptedText = [];
for (let pair of pairs) {
  let [first, second] = pair;
  let [row1, col1] = positions[first];
  let [row2, col2] = positions[second];
  if (row1 === row2) {
    decryptedText.push(
      matrix[row1][(col1 + 4) % 5],
      matrix[row2][(col2 + 4) % 5]
    );
  } else if (col1 === col2) {
    decryptedText.push(
      matrix[(row1 + 4) % 5][col1],
      matrix[(row2 + 4) % 5][col2]
    );
  } else {
    decryptedText.push(matrix[row1][col2], matrix[row2][col1]);
  }
}

// Step 4: Remove the Xs using filter
// [Linear time operation O(n)] [Linear space operation O(n)]
decryptedText = decryptedText.filter((char) => char !== "X");

// Step 5: Join the characters to form the decrypted text
// [Linear time operation O(n)] [Linear space operation O(n)]
decryptedText = decryptedText.join("");
console.log(decryptedText);
