// Playfair table
// S U P E R
// Y A B C D
// F G H I K
// L M N O Q
// T V W X Z
// Key word
// SUPERFLY
// Encripted message
// IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV

// Decripted message
// HI PX PO PO TO MO NS TR OS ES QU IP PE DA LI OP HO BI AX

// expected answer:
// HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA

// function to clean up text (remove non-alphabetic characters, convert to uppercase)
function cleanUpText(text) {
  return text.replace(/[^a-zA-Z]/g, "").toUpperCase();
}
// function to remove repeating letters (for the keyword)
function removeRepeatedLetters(key) {
  // this is where we store our unique letters
  let uniqueLetters = "";
  // This for loop will go over each letters to check for their uniqueness.
  key.split("").forEach((e, i) => {
    // if the letter doesn't exist in the uniqueLetters, then it will concatenate to the uniqueletters.
    if (uniqueLetters.includes(e) == false) {
      uniqueLetters += e;
    }
  });
  // return the unique letters
  return uniqueLetters;
}

// Function to create a Playfair cipher table based on a keyword
function createPlayfairTable(keyword) {
  // Generate the standard alphabet excluding 'J'
  let alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

  // Remove letters from the alphabet that appear in the keyword
  for (let char of keyword) {
    alphabet = alphabet.replace(char, "");
  }

  // Concatenate keyword with the modified alphabet to form the key square
  const keySquare = removeRepeatedLetters(keyword) + alphabet;
  // Create a 5x5 matrix (array of arrays) to represent the Playfair table
  let playfairTable = [];
  for (let i = 0; i < 5; i++) {
    playfairTable.push(keySquare.substring(i * 5, (i + 1) * 5).split(""));
  }
  return playfairTable;
}

// Function to decrypt a message using the Playfair cipher method and log the decoded message
function decryptAndLogPlayfair(encryptedMessage, key) {
  // Clean up input (remove non-alphabetic characters, convert to uppercase)
  encryptedMessage = cleanUpText(encryptedMessage);
  key = cleanUpText(key);

  // Generate the Playfair table based on the key
  const playfairTable = createPlayfairTable(key);

  if (!playfairTable) {
    console.error("Failed to generate Playfair table.");
    return;
  }

  // Prepare to store the decrypted message
  let decryptedMessage = "";

  // Process the encrypted message in pairs (digrams) of characters
  for (let i = 0; i < encryptedMessage.length; i += 2) {
    // store the digrams in 2 variables
    const char1 = encryptedMessage[i];
    const char2 = encryptedMessage[i + 1];

    // Find positions of the characters in the Playfair table (using deconstruction)
    const [row1, col1] = findPosition(playfairTable, char1);
    const [row2, col2] = findPosition(playfairTable, char2);

    if (row1 === -1 || col1 === -1) {
      console.error(`Character not found in Playfair table: ${char1}`);
      continue; // Skip to next iteration
    }

    if (row2 === -1 || col2 === -1) {
      console.error(`Character not found in Playfair table: ${char2}`);
      continue; // Skip to next iteration
    }

    let decryptedChar1, decryptedChar2;

    // Apply Playfair decryption rules based on character positions
    if (row1 === row2) {
      // Characters are in the same row: Shift left by one position (wrap around)
      decryptedChar1 = playfairTable[row1][(col1 + 4) % 5];
      decryptedChar2 = playfairTable[row2][(col2 + 4) % 5];
    } else if (col1 === col2) {
      // Characters are in the same column: Shift up by one position (wrap around)
      decryptedChar1 = playfairTable[(row1 + 4) % 5][col1];
      decryptedChar2 = playfairTable[(row2 + 4) % 5][col2];
    } else {
      // Characters form a rectangle: Replace with opposite corners
      decryptedChar1 = playfairTable[row1][col2];
      decryptedChar2 = playfairTable[row2][col1];
    }

    // Append decrypted characters to the decrypted message
    decryptedMessage += decryptedChar1 + decryptedChar2;
  }

  // If X is in the digram and the letter before and after the "X" is the same, then remove "X"
  for (let i = 0; i < decryptedMessage.length; i += 2) {
    if (
      decryptedMessage[i + 1] === "X" &&
      decryptedMessage[i] === decryptedMessage[i + 2]
    )
      decryptedMessage =
        decryptedMessage.substring(0, i + 1) +
        decryptedMessage.substring(i + 2);
  }
  // If the decrypted message length is odd adn the last letter is "X", remove "X"
  if (
    decryptedMessage.length % 2 !== 0 &&
    decryptedMessage[decryptedMessage.length - 1] === "X"
  ) {
    decryptedMessage = decryptedMessage.substring(
      0,
      decryptedMessage.length - 1
    );
  }
  // Output (log) the decrypted message to the console
  console.log(decryptedMessage);
}

// Function to find the position of a letters in the Playfair table
function findPosition(table, char) {
  for (let row = 0; row < 5; row++) {
    for (let col = 0; col < 5; col++) {
      if (table[row][col] === char) {
        return [row, col];
      }
    }
  }
  // If character is not found in the Playfair table
  return [-1, -1];
}

const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"; // Encrypted message to be decrypted
const decryptionKey = "SUPERSPY"; // Key used for decryption
// Decrypt the message using the decryption key and log the result
decryptAndLogPlayfair(encryptedMessage, decryptionKey);
