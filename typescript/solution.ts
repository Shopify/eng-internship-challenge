// Represents a mapping of characters to their coordinates (row and column) in a key square.
type KeySquareMap = {
    [key: string]: Coordinates
}
type Coordinates = { 
    row: number, col: number 
}
type KeySquare = string[][];

class PlayFairCipher {
    private key: string;
    private keySquare: KeySquare = [[]];
    private keySquareMap: KeySquareMap = {};

    /**
     * Constructs a PlayFairCipher object with a given key.
     * @param key The key used for encryption and decryption.
     */
    public constructor(key: string) {
        // Convert the key to upper case to avoid duplicates when building the key square matrix.
        this.key = key.toUpperCase();
        this.generateKeySquare();
    }

    /** 
     * Generates the key square matrix based on the given key.
    */
    private generateKeySquare(): void {
        const { keySquareMap, row } = this.addStringToKeySquare(this.key);
        
        // Add the remaining characters to complete the key square.
        this.addStringToKeySquare('ABCDEFGHIKLMNOPQRSTUVWXYZ', row, keySquareMap);
        this.keySquareMap = keySquareMap;
    }

    /**
     * Adds a string to the key square matrix.
     * @param str The string to add.
     * @param row The row to start adding characters.
     * @param keySquareMap The key square map to update. Used to avoid duplicates
     * @returns The updated key square map and the current row.
     */
    private addStringToKeySquare( str: string, row: number = 0, keySquareMap: KeySquareMap = {} ) {
        for (let char of str) {
            // Skip if the character is already in the key square map.
            if (char in keySquareMap)    
                continue;
            
            // Replace 'J' with 'I' to handle Playfair Cipher rules.
            if (char === 'J')
                char = 'I';
            
            // Add the character to the key square and update the key square map.
            keySquareMap[char] = { row: row, col: this.keySquare[row].length };
            this.keySquare[row].push(char);
            
            // If the row is filled, move to the next row.
            if(this.keySquare[row].length === 5 && this.keySquare.length < 5){
                this.keySquare.push([]);
                row++
            }
        }
        return { keySquareMap, row };
    }

    /**
     * Decrypts an encoded message using Playfair Cipher.
     * @param message The encoded message to decrypt.
     * @returns The decrypted message.
     */
    decrypt(message: string): Array<string> {
        // Convert message to upper case for consistency.
        message = message.toUpperCase();
        
        // Get digrams from the message.
        const digrams: Array<string> = this.getDigrams(message),
              decryptedMsg: Array<string> = [];

        digrams.forEach((digram: string) => {
            const char1 = digram[0] === 'J' ? 'I' : digram[0],
                  char2 = digram[1] === 'J' ? 'I' : digram[1];
            
            if (this.keySquareMap[char1].row === this.keySquareMap[char2].row){
                // Decrypt characters in the same row.
                decryptedMsg.push(this.decryptSameRow(char1));
                decryptedMsg.push(this.decryptSameRow(char2));
            }else if (this.keySquareMap[char1].col === this.keySquareMap[char2].col){
                // Decrypt characters in the same column.
                decryptedMsg.push( this.decryptSameCol(char1) );
                decryptedMsg.push( this.decryptSameCol(char2) );
            }else {
                // Decrypt characters forming a square in the key square.
                const { newChar1, newChar2 } = this.decryptSquare(char1 + char2);
                decryptedMsg.push(newChar1);
                decryptedMsg.push(newChar2);
            }
        });
        return decryptedMsg;
    }

    /**
     * Splits the message into digrams.
     * We are garenteed an even number of characters in the string when decrypting
     * @param message The message to split.
     * @returns An array of digrams.
     */
    private getDigrams(message: string): Array<string> {
        const digrams: Array<string> = [];
        for (let i = 0; i < message.length; i += 2)
            digrams.push(message[i] + message[i + 1]);
        
        return digrams;
    }

    /**
     * Decrypts characters in the same row of the key square.
     * @param char The character to decrypt.
     * @returns The decrypted character.
     */
    private decryptSameRow(char: string): string{
        const coordinates: Coordinates = this.keySquareMap[char];
        
        if (coordinates.col === 0)
            return this.keySquare[coordinates.row][4];
        return this.keySquare[coordinates.row][coordinates.col - 1];   
    }

    /**
     * Decrypts characters in the same column of the key square.
     * @param char The character to decrypt.
     * @returns The decrypted character.
     */
    private decryptSameCol(char: string): string{
        const coordinates: Coordinates = this.keySquareMap[char];
        
        if (coordinates.row === 0)
            return this.keySquare[4][coordinates.col];
        return this.keySquare[coordinates.row - 1][coordinates.col];   
    }

    /**
     * Decrypts characters forming a square in the key square.
     * @param digram The digram to decrypt.
     * @returns An object containing the decrypted characters.
     */
    private decryptSquare(digram: string): { newChar1: string, newChar2: string } {
        const coordinatesNewChar1: Coordinates = { row: this.keySquareMap[digram[0]].row, col: this.keySquareMap[digram[1]].col },
              coordinatesNewChar2: Coordinates = { row: this.keySquareMap[digram[1]].row, col: this.keySquareMap[digram[0]].col }
        
        const newChar1 = this.keySquare[coordinatesNewChar1.row][coordinatesNewChar1.col],
              newChar2 = this.keySquare[coordinatesNewChar2.row][coordinatesNewChar2.col];

        return { newChar1, newChar2 };
    }

}

// Create a new PlayFairCipher object with the key 'SUPERSPY'.
const playFairCipher = new PlayFairCipher('SUPERSPY');
// Define an encoded message.
const encodedMsg: string = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';

/**
 * For this particular decoded string, it seems probable that the 2 'X' characters were added during encryption.
 * The first 'X' was added to prevent consecutive repeating characters ('P') and the second 'X' was added to make the last character a digram.
 * Therefore, we can remove all 'X' characters using the 'filter' method.
 */
const decodedMsg: string = playFairCipher.decrypt(encodedMsg).filter(char => char !== 'X').join('');
console.log(decodedMsg);