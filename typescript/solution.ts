const PLAYFAIR_TABLE_SIZE: number = 5;
const ALPHABET: string = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // J is removed
const encryptedMessage: string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const cipher: string = "SUPERSPY";

// Generate Playfair key square from the key
function generateKeySquare(key: string): string[][] {
  const upperKey = key.toUpperCase().replace(/[^A-Z]/g, '').replace('J', 'I');
  const seen = new Set<string>();
  const keySquare: string[][] = [];
  const combined: string = upperKey + ALPHABET;

  for (let char of combined) {
    if (!seen.has(char)) {
      seen.add(char);
    }
  }

  let square = Array.from(seen);
  // Separate the characters into a 5x5 grid 
  for (let i = 0; i < PLAYFAIR_TABLE_SIZE; i++) {
    keySquare.push(square.slice(i * PLAYFAIR_TABLE_SIZE, (i + 1) * PLAYFAIR_TABLE_SIZE));
  }

  return keySquare;
}

// Function to find the position of a character in the key square
function findPosition(char: string, keySquare: string[][]): [number, number] {
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      if (keySquare[i][j] === char) {
        return [i, j];
      }
    }
  }
  throw new Error(`Character ${char} not found`);
}

// Parent function to decrypt the ciphertext
function decryptPlayfair(cipherText: string, key: string): string {
    let keySquare = generateKeySquare(key);

    // Tokenize message
    let tokenizedMessage: string[] = []
    for (let i = 0; i < cipherText.length; i += 2) {
      tokenizedMessage.push(cipherText.substring(i, i + 2))
    }

    let result: string[] = [];
    for (const token of tokenizedMessage) {
      let newLetters: string = "";
      // Find the positions of the two characters in the key square
      let [row1, col1] = findPosition(token[0], keySquare);
      let [row2, col2] = findPosition(token[1], keySquare);

      if (row1 === row2) {
        newLetters = keySquare[row1][(col1 + PLAYFAIR_TABLE_SIZE - 1) % 5]
                   + keySquare[row2][(col2 + PLAYFAIR_TABLE_SIZE - 1) % 5];
      } else if (col1 === col2) {
        newLetters = keySquare[(row1 + PLAYFAIR_TABLE_SIZE - 1) % 5][col1]
                   + keySquare[(row2 + PLAYFAIR_TABLE_SIZE - 1) % 5][col2];
      } else {
        newLetters = keySquare[row1][col2] + keySquare[row2][col1];
      }

      result.push(newLetters);
    }

    return result.join("").replace(/X/g, '');
}

// Decrypt the message and output the result
const decryptedMessage = decryptPlayfair(encryptedMessage, cipher);
console.log(decryptedMessage);
