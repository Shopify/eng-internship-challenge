// J removed from Alphabet
const ALPHABET = `ABCDEFGHIKLMNOPQRSTUVWXYZ`;
// Standard Playfair cipher dimension
const CIPHER_DIMENSION = 5;

/**
 * Builds a Playfair cipher using the given keyword and the alphabet with the letter "J" removed.
 * @param {String} key The keyword used to build the cipher
 * @returns {Array<Array<String>>}    A Playfair cipher (A 5x5 array of letters)
 */
function buildPlayfairCipher(key) {
  const unique_letters_key = removeDuplicateLetters(key);

  // Combine the cipher with the alphabet, then remove duplicate letters to maintain a length of 25
  const cipherList = removeDuplicateLetters(
    unique_letters_key + ALPHABET
  ).split("");

  // Separate the list into 5 lists of 5 letters
  // Potential optimization: Build the coordinate map here - left it out for separation of concerns. Would probably make more sense in a class-based approach with state.
  let cipher = [];
  for (let i = 0; i < ALPHABET.length; i += 5) {
    let row = [];
    for (j = 0; j < 5; j++) {
      row.push(cipherList[i + j]);
    }
    cipher.push(row);
  }

  return cipher;
}

/**
 * Passes a given message through a given cipher according to the [Playfair cipher rules](https://en.wikipedia.org/wiki/Playfair_cipher).
 * @param {Array<Array<String>>}  cipher  A 5x5 Playfair cipher (5x5 array of letters)
 * @param {String} message A string of letters containig no whitespaces
 * @returns {String}       The decrypted string
 */
function decryptPlayfairMessage(cipher, message) {
  let msgList = message.split("");

  // Map each letter in the cipher to its coordinates in the cipher
  const coordMap = mapCipherLettersToCoordinates(cipher);

  //   Iterate over digrams
  for (let i = 0; i < msgList.length - 1; i += 2) {
    const letter1Coords = coordMap.get(msgList[i]);
    const letter2Coords = coordMap.get(msgList[i + 1]);
    // Letters are on the same row of the cipher
    // Shift letters left
    if (letter1Coords.row == letter2Coords.row) {
      const newLetter1 =
        cipher[letter1Coords.row][
          (letter1Coords.col - 1 + CIPHER_DIMENSION) % CIPHER_DIMENSION
        ];
      const newLetter2 =
        cipher[letter2Coords.row][
          (letter2Coords.col - 1 + CIPHER_DIMENSION) % CIPHER_DIMENSION
        ];

      msgList[i] = newLetter1;
      msgList[i + 1] = newLetter2;
    }

    // Letters are on the same column of the cipher
    // Shift letters up
    else if (letter1Coords.col == letter2Coords.col) {
      const newLetter1 =
        cipher[(letter1Coords.row - 1 + CIPHER_DIMENSION) % CIPHER_DIMENSION][
          letter1Coords.col
        ];
      const newLetter2 =
        cipher[(letter2Coords.row - 1 + CIPHER_DIMENSION) % CIPHER_DIMENSION][
          letter2Coords.col
        ];

      msgList[i] = newLetter1;
      msgList[i + 1] = newLetter2;
    }
    // Letters form a rectangle
    // Swap corners along row
    else {
      const newLetter1 = cipher[letter1Coords.row][letter2Coords.col];
      const newLetter2 = cipher[letter2Coords.row][letter1Coords.col];

      msgList[i] = newLetter1;
      msgList[i + 1] = newLetter2;
    }
  }
  // Filter out Xs
  return msgList.filter((letter) => letter != "X").join("");
}

/**
 * Maps each letter in the cipher to its coordinates in said cipher, allowing for more efficient lookup during decryption.
 * @param {Array<Array<String>>} cipher A 5x5 Playfair cipher (5x5 array of letters)
 * @returns {Map<String, {col: Number, row: Number}}        A Map relating each letter in the cipher to its coordinates
 */
function mapCipherLettersToCoordinates(cipher) {
  let coordMap = new Map();
  for (let i = 0; i < cipher.length; i++) {
    for (let j = 0; j < cipher[i].length; j++) {
      const letter = cipher[i][j];
      coordMap.set(letter, { row: i, col: j });
    }
  }

  return coordMap;
}

/**
 *  Removes duplicate letters in a string, leaving only the first occurence of each letter.
 *  @param {String} word A string - assumed to contain no whitespaces.
 *
 *  @return {String}     The new string with no duplicate letters.
 */
function removeDuplicateLetters(word) {
  const letters = word.split("");
  const letterSet = new Set();
  //Check for the existance of a letter in the set before adding it
  for (let i = 0; i < letters.length; i++) {
    if (letterSet.has(letters[i])) {
      // Replace duplicate letters with empty space to be filtered out
      letters[i] = " ";
    } else {
      letterSet.add(letters[i]);
    }
  }

  // Filter out the whitespaces
  return letters.filter((letter) => letter != " ").join("");
}

function main() {
  const key = "SUPERSPY";
  const message = `IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV`;
  const cipher = buildPlayfairCipher(key);

  const decryptedMessage = decryptPlayfairMessage(cipher, message);

  console.log(decryptedMessage);
}

main();
