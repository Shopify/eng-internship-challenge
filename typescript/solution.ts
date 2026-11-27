// Playfair Cipher Decryption - TypeScript Solution (by gdcho)

// key = "SUPERSPY"
// encryption = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

// Playfair table (5x5 with key "SUPERSPY" and "J" as "I")
// S U P E R
// Y A B C D
// F G H I K
// L M N O Q
// T V W X Z

// Decryption Steps for Playfair Cipher:
// 1. Populate the 5x5 key table with key characters without duplicates and fill the remaining with the rest of the alphabet excluding "J"
// 2. Split the encryption text into pairs ("IK EW EN EN XL NQ LP ZS LE RU MR HE ER YB OF NE IN CH CV")
// 3. For each pair:
//    a. If both letters are in the same row, replace each letter with the letter to its left
//    b. If both letters are in the same column, replace each letter with the letter directly above it
//    c. If the letters are not on the same row or column, swap each letter with the letter on the same row but at the column of the other letter of the pair
// 4. Remove any 'X's or filler letters

type Table = string[][];

interface TableProps {
  key: string;
  table: Table;
}

const key = "SUPERSPY";
const encryptedStr = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";

// function to create a 5x5 table with the key and the rest of the alphabet
function createKeyTable({ key }: { key: string }): TableProps {
  // create a 5x5 table filled with empty strings
  const keyTable: Table = Array.from({ length: 5 }, () =>
    new Array(5).fill("")
  );
  const set = new Set<string>();
  // make key to uppercase, replace J with I, and remove non-alphabetic characters
  key = key
    .toUpperCase()
    .replace(/J/g, "I")
    .replace(/[^A-Z]/g, "");

  // populate the key table with characters from the
  let index = 0;
  for (const char of key) {
    // don't add duplicates
    if (!set.has(char)) {
      set.add(char);
      keyTable[Math.floor(index / 5)][index % 5] = char;
      index++;
    }
  }

  // fill the remaining key table with the rest of the alphabet excluding "J"
  for (let i = 0; i < 26; i++) {
    const char = String.fromCharCode(i + 65); // from ASCII 65 which is 'A'
    // Skip 'J' and duplicates
    if (char !== "J" && !set.has(char)) {
      set.add(char);
      // fill until 25 (5x5 table)
      if (index < 25) {
        keyTable[Math.floor(index / 5)][index % 5] = char;
        index++;
      }
    }
  }
  // return the key table with the filled key properties
  return { key, table: keyTable };
}

// function to find the position of a character in the key table
function findPosition(
  char: string,
  keyTable: Table
): [number, number] | undefined {
  char = char.toUpperCase();
  for (let i = 0; i < 5; i++) {
    for (let j = 0; j < 5; j++) {
      // if position equals to the character, return the position
      if (keyTable[i][j] === char) {
        return [i, j];
      }
    }
  }
  // not found
  return undefined;
}

// function to decrypt the encrypted string given encryption key
function ciperDecryption(str: string, key: string): string {
  // create a 5x5 key table using createKeyTable function
  const { table: keyTable } = createKeyTable({ key });
  // make the string uppercase and remove not alphabet characters
  str = str.toUpperCase().replace(/[^A-Z]/g, "");
  // result string to store the decrypted string
  let result = "";

  // within encrypted string, split into pairs and process each pair
  for (let i = 0; i < str.length; i += 2) {
    // find the positions of the characters in the key table
    const pos1 = findPosition(str[i], keyTable);
    const pos2 = findPosition(str[i + 1], keyTable);

    // if either position is not found, skip
    if (!pos1 || !pos2) {
      continue;
    }

    // get the row and column of each character at their position
    const [row1, column1] = pos1;
    const [row2, column2] = pos2;

    if (row1 === row2) {
      // if on the same row, shift each character to the left by one position
      result += keyTable[row1][(column1 + 4) % 5];
      result += keyTable[row2][(column2 + 4) % 5];
    } else if (column1 === column2) {
      // if on the same column, shift each character up by one position
      result += keyTable[(row1 + 4) % 5][column1];
      result += keyTable[(row2 + 4) % 5][column2];
    } else {
      // if not on the same row or column, swap the rectangle corners between the two characters
      result += keyTable[row1][column2];
      result += keyTable[row2][column1];
    }
  }

  // return decypred string and remove any 'X' or spaces
  return result.replace(/X/g, "");
}

(function main() {
  // output the decrypted string
  console.log(ciperDecryption(encryptedStr, key));
})();
