const PASSWORD: string = "SUPERSPY";
const CHAR_TO_SKIP: string = "J";
const TABLE_DIMENSION: number = 5;
const ENCRYPTED_MESSAGE: string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const ERROR_MESSAGE: string = "Encrypted Message Is Invalid!";

/**
 * Constructs a Playfair cipher table from a given password, skipping a specified character.
 *
 * @param password - The password to use for constructing the table.
 * @param charToSkip - The character to exclude from the table.
 * @returns A 2D array of characters representing the Playfair cipher table.
 */
const constructTableFromPassword = (
  password: string,
  charToSkip: string
): string[][] => {
  // For time efficiency, a set is used instead of an array.
  const allUppercaseCharsSet: Set<string> = new Set(
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("")
  );
  allUppercaseCharsSet.delete(charToSkip);

  // Any string passed as the password can help construct the table.
  // Any alphabetic characters, upper or lower, can change the order of table characters.
  const uppercasePassword: string = password.toUpperCase();
  const table: string[][] = [[]];

  // Nested helper function to add a character to the table
  const addToTable = (char: string) => {
    if (table[table.length - 1].length < TABLE_DIMENSION) {
      table[table.length - 1].push(char);
    } else {
      table[table.length] = [char];
    }
  };

  // Add valid characters from the password to the table, ensuring no duplicates
  for (const char of uppercasePassword) {
    if (allUppercaseCharsSet.has(char)) {
      addToTable(char);
      allUppercaseCharsSet.delete(char);
    }
  }

  // Add remaining characters from the set to the table in order.
  Array.from(allUppercaseCharsSet)
    .sort()
    .forEach((char: string) => addToTable(char));

  return table;
};

// Construct the Playfair cipher table
const table = constructTableFromPassword(PASSWORD, CHAR_TO_SKIP);

// For time efficiency, a map is used instead of the actual table to obtain indices quickly.
const tableIndicesMap: Map<string, number[]> = new Map();
table.forEach((row: string[], i: number) => {
  row.forEach((char: string, j: number) => {
    tableIndicesMap.set(char, [i, j]);
  });
});

/**
 * Decrements a number in a modular arithmetic manner based on the table dimension.
 *
 * @param num - The number to decrement.
 * @returns The decremented number.
 */
const modularDecrement = (num: number): number =>
  (num + TABLE_DIMENSION - 1) % TABLE_DIMENSION;

/**
 * Skips the character 'X' in the result.
 *
 * @param char - The character to check.
 * @returns The character itself or an empty string if the character is 'X'.
 */
const skipX = (char: string): string => (char === "X" ? "" : char);

/**
 * Decrypts an encrypted message using the Playfair cipher.
 *
 * @param encryptedMessage - The encrypted message to decrypt.
 * @returns The decrypted message.
 * @throws Error if the encrypted message is invalid.
 */
const decrypt = (encryptedMessage: string): string => {
  // Throws an error if length of the encrypted message is odd or it includes
  // the skipped character or it includes any character other than uppercase letters.
  if (
    encryptedMessage.length % 2 ||
    encryptedMessage.includes(CHAR_TO_SKIP) ||
    !/^[A-Z]*$/.test(encryptedMessage)
  ) {
    throw new Error(ERROR_MESSAGE);
  }

  const result: string[] = [];

  // Process the encrypted message two characters at a time
  for (let i = 0; i < encryptedMessage.length; i += 2) {
    // Throws an error if the pair in the digram has the same character.
    if (encryptedMessage[i] === encryptedMessage[i + 1]) {
      throw new Error(ERROR_MESSAGE);
    }

    // Fast retrieval of 4 indices of the two characters
    const indices1: number[] = <number[]>(
      tableIndicesMap.get(encryptedMessage[i])
    );
    const indices2: number[] = <number[]>(
      tableIndicesMap.get(encryptedMessage[i + 1])
    );

    // Simple row and col names are used for simplicity.
    const row1: number = indices1[0];
    const col1: number = indices1[1];
    const row2: number = indices2[0];
    const col2: number = indices2[1];

    if (row1 === row2) {
      // Same row, shift left to decrypt
      result.push(skipX(table[row1][modularDecrement(col1)]));
      result.push(skipX(table[row2][modularDecrement(col2)]));
    } else if (col1 === col2) {
      // Same column, shift up to decrypt
      result.push(skipX(table[modularDecrement(row1)][col1]));
      result.push(skipX(table[modularDecrement(row2)][col2]));
    } else {
      // Rectangular swap columns to decrypt
      result.push(skipX(table[row1][col2]));
      result.push(skipX(table[row2][col1]));
    }
  }
  return result.join("");
};

try {
  console.log(decrypt(ENCRYPTED_MESSAGE));
} catch (err) {
  console.error("Error:", (<Error>err).message);
}
