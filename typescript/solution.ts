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

const SECRET_KEY = "SUPERSPY";
const ENCRYPTED_MSG = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

console.log(generateTable(SECRET_KEY));
