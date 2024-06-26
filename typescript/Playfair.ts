/*
  Overall Runtime: O(n)

  Runtime Analysis: The actual process of constructing the key matrix and the respective hashmap is O(1).
  This is because the key matrix is always a 5x5 matrix and the hashmap is always a 1-1 mapping of the key matrix.
  The hashmap, although it takes space, also allows us to perform lookups in O(1) time. Actual decryption takes O(n)
  times, since we have to iterate through the entire ciphertext.

  Space Complexity: O(1)

  Space Complexity Analysis: The space complexity is O(1) because the key matrix and the hashmap are always of 
  fixed size. The memory used is independent of the inputs.
*/

export default class Playfair {
  private KeyText_: string; //the key text used to generate the keyMatrix

  private KeyMatrix_: string[][];
  private MatrixHashMap_: Map<string, [number, number]>; //tracks the row and column of each character in the keyMatrix

  //key matrix dimensions (certain implementations use a 6x6 matrix so it's configurable here)
  private MatrixRows_ = 5;
  private MatrixCols_ = 5;

  constructor(KeyText: string) {
    //Pre condition: Keytext's length must not be greater than the matrix's size
    if (KeyText.length > this.MatrixRows_ * this.MatrixCols_) {
      throw new Error(
        `Key text is too long. Required Length: ${this.MatrixRows_ * this.MatrixCols_} Current key text length: ${
          KeyText.length
        }`
      );
    }

    this.KeyText_ = KeyText;
    this.KeyMatrix_ = this.CreateKeyMatrix(this.KeyText_);
    this.MatrixHashMap_ = this.CreateMatrixHashMap(this.KeyMatrix_);
  }

  //getters - used for testing (but may also be useful for other developers)
  public get KeyText(): string {
    return this.KeyText_;
  }

  public get KeyMatrix(): string[][] {
    return this.KeyMatrix_;
  }

  public get MatrixHashMap(): Map<string, [number, number]> {
    return this.MatrixHashMap_;
  }

  //methods
  /**
   * @param { string } Key - key parameter
   * @returns { string[][] } - returns a key matrix for PLAYFAIR cipher
   *  @description - This function creates a key matrix for the Playfair cipher. As per convention, this 5x5 matrix omits 'J' by replacing it with 'I'
   */
  private CreateKeyMatrix(Key: string): string[][] {
    Key = Key.replace(/ /g, ""); //remove spaces

    const usedChars = new Set<string>(); //characters currently in the keyMatrix
    const keyMatrix = new Array<Array<string>>();

    let keyIndex = 0; //keeps track of where in the key we are
    let currentAlpha = "A"; //keeps track of the current letter we are on

    for (let i = 0; i < this.MatrixRows_; i++) {
      keyMatrix.push(new Array<string>());
      for (let j = 0; j < this.MatrixCols_; j++) {
        let char: string;

        //Add chars from key text until all are consumed. Then add letters from A-Z that haven't already been used.
        if (keyIndex < Key.length) {
          char = Key[keyIndex].toUpperCase();
          keyIndex++;

          if (char === "J") char = "I";

          if (usedChars.has(char)) {
            j--;
            continue;
          }
        } else {
          while (usedChars.has(currentAlpha) || currentAlpha === "J") {
            currentAlpha = String.fromCharCode(currentAlpha.charCodeAt(0) + 1);
          }
          char = currentAlpha;
        }

        //Add the character to keyMatrix
        keyMatrix[i].push(char);
        usedChars.add(char);
      }
    }

    return keyMatrix;
  }

  /**
   * @param { string[][] } KeyMatrix - key matrix for PLAYFAIR cipher
   * @returns { Map<string, [number, number]> } - returns a hashmap that maps each character in the key matrix to its row and column
   * @description Generates a hashmap for quick lookup for rows and columns in `KeyMatrix`
   */
  private CreateMatrixHashMap(KeyMatrix: string[][]): Map<string, [number, number]> {
    const matrixHashMap = new Map<string, [number, number]>();

    for (let i = 0; i < KeyMatrix.length; i++) {
      for (let j = 0; j < KeyMatrix[i].length; j++) {
        matrixHashMap.set(KeyMatrix[i][j], [i, j]);
      }
    }

    return matrixHashMap;
  }

  /**
   * @param { number } Operand1 - first operand
   * @param { number } Operand2 - second operand
   * @returns { number } - returns the positive modulo of `Operand1` and `Operand
   */
  private GetPositiveMod(Operand1: number, Operand2: number) {
    return ((Operand1 % Operand2) + Operand2) % Operand2;
  }

  /**
   * @param { string } Char1 - first character in the digraph
   * @param { string } Char2 - second character in the digraph
   * @param { string[][] } KeyMatrix - key matrix for PLAYFAIR cipher
   * @returns { string } - returns the decrypted digraph
   * @description Decrypts a digraph using the key matrix
   */
  private DecryptDigraph(Char1: string, Char2: string, KeyMatrix: string[][]): string {
    const [row1, col1] = this.MatrixHashMap_.get(Char1) || [-1, -1];
    const [row2, col2] = this.MatrixHashMap_.get(Char2) || [-1, -1];

    if (row1 === -1 || row2 === -1) {
      throw new Error("Invalid character in digraph");
    }

    if (col1 === col2) {
      //CASE 1: same column
      return (
        KeyMatrix[this.GetPositiveMod(row1 - 1, this.MatrixRows_)][col1] +
        KeyMatrix[this.GetPositiveMod(row2 - 1, this.MatrixRows_)][col2]
      );
    } else if (row1 === row2) {
      //CASE 2: same row
      return (
        KeyMatrix[row1][this.GetPositiveMod(col1 - 1, this.MatrixCols_)] +
        KeyMatrix[row2][this.GetPositiveMod(col2 - 1, this.MatrixCols_)]
      );
    } else {
      //CASE 3: different row and column
      return KeyMatrix[row1][col2] + KeyMatrix[row2][col1];
    }
  }

  /**
   * @param { string } CipherText - cipher text to decrypt
   * @returns { string } - returns the decrypted text
   */
  public DecryptPlayFair(CipherText: string): string {
    //Pre condition 1: CipherText must have an even length
    if (CipherText.length % 2 !== 0) {
      throw new Error(`Cipher Text must have an even length. Current Length: ${CipherText.length}`);
    }

    //Pre condition 2: CipherText must not contain any characters other than A-Z
    if (!/[A-Za-z]/.test(CipherText)) {
      throw new Error("Cipher Text must only contain characters A-Z");
    }

    //Pre condition 3: CipherText must be in full uppercase (could also be replaced with an error depending on context-specific development practices)
    CipherText = CipherText.toUpperCase();

    //Deccrypt the digraphs
    let decryptedText = "";
    CipherText.match(/.{1,2}/g)?.forEach(
      (pair) => (decryptedText += this.DecryptDigraph(pair[0].toUpperCase(), pair[1].toUpperCase(), this.KeyMatrix_))
    );

    //Post condition 1: Remove spaces
    decryptedText = decryptedText.replace(/ /g, "");

    //Post condition 2: Ensure that the result is in full uppercase
    decryptedText = decryptedText.toUpperCase();

    //Post condition 3: Ensure that the result is in full uppercase
    decryptedText = decryptedText.replace(/X/g, "");

    return decryptedText.replace(/ /g, "").toUpperCase(); //ensuring that the result is in full uppercase (redunant but just in case a developer later makes a mistake)
  }
}
