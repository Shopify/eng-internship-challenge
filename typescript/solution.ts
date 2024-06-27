/**
 * A simple program for decrypting Playfair Ciphers. See the below Wiki article
 * for more information.
 *
 * https://en.wikipedia.org/wiki/Playfair_cipher
 *
 * Author: Callum Kipin
 */

type TablePattern = "LEFT_TO_RIGHT"; // Spiral is another possible pattern, see the Wiki
type Length5Array = [string, string, string, string, string];
type PlayfairTable = [
  Length5Array,
  Length5Array,
  Length5Array,
  Length5Array,
  Length5Array
];

/**
 * Generates the require table to encrypt and decrypt Playfair ciphers.
 *
 * @param key The key word used to generate the table
 * @param missingLetter The letter to exclude from the Playfair table
 * @param pattern The fill order of letters in the table
 * @returns A 5x5 table of uppercase characters including all letters except
 * the missing letter provided
 */
function generateTable(
  key: string,
  missingLetter: string = "J", // by default, Playfair tables don't include J (treated the same as I)
  pattern: TablePattern = "LEFT_TO_RIGHT" // standard Playfair uses Left to Right fill
): PlayfairTable {
  let table: PlayfairTable = [
    // there's likely a cleaner way to do this using Array.fill(), but the typing makes it difficult
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
  ];
  let remainingLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("").reverse(); // alphabet

  // Ensure the input is all valid
  if (!key.match(/^[A-Z]+$/)) {
    throw new Error("Playfair key must be made of uppercase letters.");
  } else if (!missingLetter.match(/^[A-Z]$/)) {
    throw new Error("Missing letter must be a single uppercase letter.");
  }

  // Remove the missing letter from the letters to be used in the table
  remainingLetters = remainingLetters.filter((val) => val !== missingLetter);

  // Insert the unique letters from the keyphrase into the table
  let curTablePos = 0;
  for (const letter of key) {
    let letterIndex = remainingLetters.indexOf(letter);

    // If the letter was already added to the table, ignore it
    if (letterIndex < 0) {
      continue;
    }

    // Otherwise, add the letter to the correct spot and remove it from the letters remaining
    table[Math.floor(curTablePos / 5)][curTablePos % 5] = letter;
    remainingLetters.splice(letterIndex, 1);
    curTablePos++;
  }

  // Insert the remaining letters into the table that weren't in the key, in alphabetical order
  while (remainingLetters.length > 0) {
    let letter = remainingLetters.pop();

    // Satisfy TypeScript
    if (typeof letter !== "undefined") {
      table[Math.floor(curTablePos / 5)][curTablePos % 5] = letter;
      curTablePos++;
    }
  }

  return table;
}

function decodePlayfair(msg: string, table: PlayfairTable): string {
  let decodedMsg = "";

  // Ensure the input is valid
  if (msg.length % 2 !== 0 || !msg.match(/^[A-Z]+$/)) {
    throw new Error(
      "Encoded message must be even length and made of uppercase letters."
    );
  }

  // Decode each pair of letters based on the Playfair rules
  for (let i = 0; i < msg.length; i += 2) {
    // Find where the characters are in the table
    let char1Indexes = findCharInTable(msg[i], table);
    let char2Indexes = findCharInTable(msg[i + 1], table);

    // Should not occur, but satisfies TypeScript
    if (typeof char1Indexes === "undefined") {
      throw new Error(
        `Character ${msg[i]} in encoded message does not exist in table.`
      );
    } else if (typeof char2Indexes === "undefined") {
      throw new Error(
        `Character ${msg[i + 1]} in encoded message does not exist in table.`
      );
    }

    // Based on their position, decode each pair
    if (
      char1Indexes.row === char2Indexes.row &&
      char1Indexes.col === char2Indexes.col
    ) {
      throw new Error(
        "Invalid encoded Wayfair message, cannot have a pair of duplicate characters."
      );
    } else if (char1Indexes.row === char2Indexes.row) {
      // If the characters are in the same row, shift left one to decode (with wrap-around)
      decodedMsg +=
        table[char1Indexes.row][(char1Indexes.col + 4) % 5] +
        table[char2Indexes.row][(char2Indexes.col + 4) % 5];
    } else if (char1Indexes.col === char2Indexes.col) {
      // If the characters are in the same col, shift up one to decode (with wrap-around)
      decodedMsg +=
        table[(char1Indexes.row + 4) % 5][char1Indexes.col] +
        table[(char2Indexes.row + 4) % 5][char2Indexes.col];
    } else {
      // Otherwise, the characters form a rectangle - exchange each letter with the letter on the
      // opposite side of the same row
      decodedMsg +=
        table[char1Indexes.row][char2Indexes.col] +
        table[char2Indexes.row][char1Indexes.col];
    }
  }

  // Remove all of the "X" characters from the decoded message
  decodedMsg = decodedMsg.replace(/X/g, "");

  return decodedMsg;
}

/**
 * Returns the row and col of the char given if it exists in the table, otherwise
 * returns undefined.
 *
 * @param char The character to search for
 * @param table The 2D table to search
 * @returns The row and col of the character (if it exists), undefined otherwise
 */
function findCharInTable(
  char: string,
  table: PlayfairTable
): { row: number; col: number } | undefined {
  for (let row = 0; row < table.length; row++) {
    for (let col = 0; col < table[row].length; col++) {
      if (char === table[row][col]) {
        return { row, col };
      }
    }
  }

  return undefined;
}

// Test code to decode the "super secret message"
const SECRET_KEY = "SUPERSPY";
const ENCRYPTED_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

const table = generateTable(SECRET_KEY);
const decodedMsg = decodePlayfair(ENCRYPTED_MSG, table);

console.log(decodedMsg);
