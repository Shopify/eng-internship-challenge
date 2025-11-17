// HELPER FUNCTIONS:
function getLetterRowCol(letter, keyTable) {
  for (row = 0; row < keyTable.length; row++) {
    for (col = 0; col < keyTable[row].length; col++) {
      if (keyTable[row][col] === letter) {
        return [row, col];
      }
    }
  }
  return [null, null];
}

// PART 1: GENERATE THE 5*5 KEYTABLE
const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

function generateKeyTable(key) {
  // ensure key is all uppercase and contains only unique letter characters
  //  note: see Pull Request descrition for "alternate key generation methods"
  //  QUESTION: if 'X' is used to pad digrams, should it be usable in the key?
  key = [...new Set(key.toUpperCase().replace(/[^A-Z]/g, ""))].join("");

  // ensure the table is completed with remaining unique letters (not in the key)
  let remainingUniqueLetters = alphabet;
  for (let i = 0; i < key.length; i++) {
    remainingUniqueLetters = remainingUniqueLetters.replace(key[i], "");
  }

  // remove one more letter (for a total of 25 letters)
  const removableLetters = ["J", "Q", "I"];
  for (let letter of removableLetters) {
    if (remainingUniqueLetters.includes(letter)) {
      remainingUniqueLetters = remainingUniqueLetters.replace(letter, "");
      break;
    }
  }

  // populate the 5x5 keytable (2D array) with key and remainingUniqueLetters
  // [0, 1, 2, 3, 4, 5, ... , 23, 24] ==>
  // [ [0, 1, 2, 3, 4],
  //   [5, 6, 7, 8, 9],
  //   [10, 11, 12, 13, 14],
  //   [15, 16, 17, 18, 19],
  //   [20, 21, 22, 23, 24] ];
  let temporaryKeyTable = key
    .split("")
    .concat(remainingUniqueLetters.split(""));
  let keyTable = [];
  for (let i = 0; i < temporaryKeyTable.length; i += 5) {
    keyTable.push(temporaryKeyTable.slice(i, i + 5));
  }

  return keyTable;
}

// PART 2: DECRYPT THE CIPHERTEXT USING THE KEYTABLE
function decryptCipherText(cipherText, key) {
  cipherText = cipherText.toUpperCase();
  const keyTable = generateKeyTable(key);
  let plainText = "";

  // note: the cipherText will always have an even number of letters dy design
  for (let digramIndex = 0; digramIndex < cipherText.length; digramIndex += 2) {
    let letter1 = cipherText[digramIndex];
    let letter2 = cipherText[digramIndex + 1];

    let [row1, col1] = getLetterRowCol(letter1, keyTable);
    let [row2, col2] = getLetterRowCol(letter2, keyTable);

    // apply the decryption procedure as described in the PR description
    if (col1 === col2) {
      plainText += keyTable[(row1 + 4) % 5][col1];
      plainText += keyTable[(row2 + 4) % 5][col2];
    } else if (row1 === row2) {
      plainText += keyTable[row1][(col1 + 4) % 5];
      plainText += keyTable[row2][(col2 + 4) % 5];
    } else {
      plainText += keyTable[row1][col2];
      plainText += keyTable[row2][col1];
    }
  }

  // ensure decrypted string is: all uppercase & contains only letter characters & excludes 'X'
  plainText = plainText.toUpperCase().replace(/[^A-Z]|X/g, "");

  return plainText;
}

// RUNNING THE ALGORITHM!
const cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const key = "SUPERSPY";
const plainText = decryptCipherText(cipherText, key);
console.log(plainText);

// ADDITIONAL SAMPLE TEST CASES:
// console.log(generateKeyTable("monarchy"));
// console.log(generateKeyTable("playfair example"));

// console.log(decryptCipherText("gatlmzclrqtx", "SUPERSPY"));
// console.log(decryptCipherText("gatlmzclrqtx", "monarchy"));
