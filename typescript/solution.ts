const KEY = "SUPERSPY";
const ENCRYPTED_TEXT = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

// J is replaced with I to fit into the 5x5 grid
const ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

// Not reuquired for this specific challenge, but needed for other cases.
// J is replaced with I to fit into the 5x5 grid
// reference https://arc.net/l/quote/zkxoetwh
function normalize(text: string): string {
  return text.toUpperCase().replace(/J/g, "I");
}

// Process from https://en.wikipedia.org/wiki/Playfair_cipher#Description
// Assumptions made:
// `I` and `J` may be interchanged
// The text consists of only letters from the alphabet
// The text has an even number of characters - else it's not a valid encrypted text
function decrypt(_text: string, _key: string): string {
  const key = normalize(_key);
  const encryptedText = normalize(_text);

  // Our 5x5 grid for the cipher
  const grid: string[][] = [];
  // Stores the positions of each letter in the grid, as [row, column]
  const positions = new Map<string, [number, number]>();

  // Sets in javascript preserve insertion order, so we can use it to create the grid
  const gridString = Array.from(new Set(key + ALPHABET));
  for (let i = 0; i < 5; i++) {
    // Append the i'th row to the grid
    const rowString = gridString.slice(i * 5, (i + 1) * 5);
    grid.push(rowString);

    // Add the positions of each letter to the map
    for (let j = 0; j < 5; j++) {
      positions.set(rowString[j], [i, j]);
    }
  }

  // We have now formed the grid, so we can start decrypting
  let decryptedText = "";
  // Iterate in pairs of 2
  for (let i = 0; i < encryptedText.length; i += 2) {
    const letterOne = encryptedText[i];
    const letterTwo = encryptedText[i + 1];

    // Get the positions of the letters in the grid
    const positionOne = positions.get(letterOne);
    const positionTwo = positions.get(letterTwo);

    if (!positionOne || !positionTwo) {
      throw new Error(
        `Position of ${letterOne} or ${letterTwo} not found, this should never happen`
      );
    }

    // If both letters are in the same row, replace them with the letter on the left.
    // Wrap around if needed.
    if (positionOne[0] === positionTwo[0]) {
      decryptedText += grid[positionOne[0]][(positionOne[1] + 4) % 5];
      decryptedText += grid[positionTwo[0]][(positionTwo[1] + 4) % 5];
      continue;
    }

    // If both letters are in the same column, replace them with the letter on the top.
    // Wrap around if needed.
    if (positionOne[1] === positionTwo[1]) {
      decryptedText += grid[(positionOne[0] + 4) % 5][positionOne[1]];
      decryptedText += grid[(positionTwo[0] + 4) % 5][positionTwo[1]];
      continue;
    }

    // If the letters aren't in the same row or column,
    // Create an imaginary rectangle with the two letters as corners.
    // Replace with the letter at the opposite corner of the rectangle.
    decryptedText += grid[positionOne[0]][positionTwo[1]];
    decryptedText += grid[positionTwo[0]][positionOne[1]];
  }

  // Remove the extra X's from the decrypted text
  return decryptedText.replace(/X/g, "");
}

console.log(decrypt(ENCRYPTED_TEXT, KEY));
