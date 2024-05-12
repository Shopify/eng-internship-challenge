/* Author: Rohullah Noory
   Description: This file implements decryption logic for PlayFair Cipher in Typescript
*/

interface LetterIndexInMatrix {
  row: number;
  column: number;
}

class DecryptCipher {
  private encryptedMessage: string;
  private cipherKey: string;
  private lookup: Record<string, LetterIndexInMatrix>;
  private decryptedMessage: string;
  private matrix: string[][];

  constructor(message: string, key: string) {
    this.encryptedMessage = message;
    this.cipherKey = key;
    this.lookup = {};
    this.decryptedMessage = "";
    this.matrix = [];
  }

  /*Function: generateMatrix()
  Description: Used to generate the 5x5 matrix needed for the cipher
  Parameters: none
  Returns: none */
  private generateMatrix(): void {
    const alphabetsWithoutJ = "ABCDEFGHIKLMNOPQRSTUVWXYZ"; // excluded 'J' because 'J' is usually removed or used interchangeably with 'I' in PlayFair Cipher
    const lettersWithoutDuplicates = Array.from(
      new Set(this.cipherKey + alphabetsWithoutJ)
    );
    let index = 0;

    for (let char of lettersWithoutDuplicates) {
      const rowIndex = Math.floor(index / 5);
      let colIndex = index % 5;
      if (this.matrix.length <= rowIndex) {
        this.matrix.push([]);
      }
      this.matrix[rowIndex][colIndex] = char;
      this.lookup[char] = { row: rowIndex, column: colIndex };
      index++;
    }
  }

  /* Function: findIndexOfLetter()
  Description: Used to find the index of a letter in the matrix
  Parameters: letter - the letter that needs to be found
  Returns: an object of type LetterIndexInMatrix, containing the row and column of the letter */
  private findIndexOfLetter(letter: string): LetterIndexInMatrix {
    const index = this.lookup[letter];
    if (!index) {
      throw new Error(`Character '${letter}' not found in lookup table.`);
    }
    return index;
  }

  /* Function: handleSameRow()
  Description: Used to handle the case where 2 letters are in the same row. 
                If this is the case, the letter immediately to the left of the letters are added to the decrypted message.
                If the letter is the first in the row, it uses the last letter of the row as the decryption letter.
  Parameters: index of first letter, index of second letter in the pair
  Returns: none */
  private handleSameRow(
    firstLetterIndex: LetterIndexInMatrix,
    secondLetterIndex: LetterIndexInMatrix
  ): void {
    this.decryptedMessage +=
      this.matrix[firstLetterIndex.row][(firstLetterIndex.column + 4) % 5] +
      this.matrix[secondLetterIndex.row][(secondLetterIndex.column + 4) % 5];
  }

  /* Function: handleSameColumn()
  Description: Used to handle the case where 2 letters are in the same column. 
              If this is the case, the letter immediately above the letters are added to the decrypted message.
              If the letter is the first in the column, it uses the last letter of the column as the decryption letter.
  Parameters: index of first letter, index of second letter in the pair
  Returns: none */
  private handleSamecolumn(
    firstLetterIndex: LetterIndexInMatrix,
    secondLetterIndex: LetterIndexInMatrix
  ): void {
    this.decryptedMessage +=
      this.matrix[(firstLetterIndex.row + 4) % 5][firstLetterIndex.column] +
      this.matrix[(secondLetterIndex.row + 4) % 5][secondLetterIndex.column];
  }

  /* Function: decryptMessage()
  Description: Used to decrypt a ciphered text by applying matrix-based decryption rules, 
              ensuring that each character pair from the encrypted message is correctly 
              processed and transformed back into its original form.
  Parameters: none
  Returns: none */
  private decryptMessage(): void {
    const pairs = encryptedMessage.match(/[A-Z]{1,2}/g) || [];
    pairs.forEach((pair) => {
      const firstLetterIndex = this.findIndexOfLetter(pair[0]);
      const secondLetterIndex = this.findIndexOfLetter(pair[1]);

      if (pair.length !== 2) {
        throw new Error(
          `Invalid pair '${pair}' encountered in the encrypted message.`
        );
      }

      if (firstLetterIndex.row === secondLetterIndex.row) {
        this.handleSameRow(firstLetterIndex, secondLetterIndex);
      } else if (firstLetterIndex.column === secondLetterIndex.column) {
        this.handleSamecolumn(firstLetterIndex, secondLetterIndex);
      } else {
        // handle the case where the letters are not in the same row or column
        this.decryptedMessage +=
          this.matrix[firstLetterIndex.row][secondLetterIndex.column] +
          this.matrix[secondLetterIndex.row][firstLetterIndex.column];
      }
    });
  }

  /* Function: getSanitizedDecryptedMessage()
  Description: Used to return the decrypted message
  Parameters: none
  Returns: the decrypted message */
  public getSanitizedDecryptedMessage(): string {
    this.generateMatrix();
    this.decryptMessage();

    return this.decryptedMessage.toUpperCase().replace(/[\sX\xX\W_]/g, "");
  }
}

const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const cipherKey = "SUPERSPY";
const decryptCipher = new DecryptCipher(encryptedMessage, cipherKey);
const decryptMessage = decryptCipher.getSanitizedDecryptedMessage();
console.log(decryptMessage);
