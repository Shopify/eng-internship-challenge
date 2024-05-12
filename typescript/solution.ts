// The key is SUPERSPY and the character X has been provided as 
// the character to be used for duplication or uneven length strings.
// It can be assumed that I = J.  

// The grid should therefor look like:
// S U P E R
// Y A B C D 
// F G H I K 
// L M N O Q 
// T V W X Z

// The encrypted message is said to be: IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV


class Solution {
    private solution: string = "";
    private grid: Array<string> = [];

    public constructor(private key: string, private encryptedMessage: string) {
        this.grid = this.createGrid(this.key);
    }
    
    private solve(){
        // Remove the spaces and/or special characters before solving to ensure the characters are not parsed. 
        let tempEncryptedMessage = this.cleanString(this.encryptedMessage);

        // Loop for solving each bigram until the end of the string.
        for (let i = 0; i < tempEncryptedMessage.length; i += 2) {
            const char1 = tempEncryptedMessage[i];
            const char2 = tempEncryptedMessage[i + 1];

            const index1 = this.grid.indexOf(char1);
            const index2 = this.grid.indexOf(char2);

            if (this.sameRow(index1, index2)) {
                this.moveOnSameRow(index1, index2);

            } else if (this.sameColumn(index1, index2)) {
                this.moveOnSameColumn(index1, index2);
            } else {
                this.moveOnDiagonal(index1, index2);
            }
        }
    }

    // Creates the grid required to decrypt the encryptedMessage. 
    private createGrid(key: string): Array<string> {
        let tempKey = this.cleanString(key);
        
        const returnArray = this.addKeyToGrid(tempKey);
        
        const alphabetArray = ["A", "B", "C", "D", "E", 
                               "F", "G", "H", "I", "K", 
                               "L", "M", "N", "O", "P", 
                               "Q", "R", "S", "T", "U", 
                               "V", "W", "X", "Y", "Z"];

        for (let i = 0; i < alphabetArray.length; i += 1) {
            if (!returnArray.includes(alphabetArray[i])) {
                returnArray.push(alphabetArray[i]);
            }
        }
        return returnArray;
    }

    // Adds the characters to the grid, ensuring there are no duplicates.
    private addKeyToGrid(key: string): Array<string> {
        const tempArray = key.split("");
        const returnArray: string[] = [];
        
        for (const item of tempArray) {
            if (!returnArray.includes(item)) {
                returnArray.push(item);
            }
        }
        return returnArray;
    }
    
    
    // Performs check to confirm that the characters are in the same row in the grid.
    // REQUIRES: parameters are in the same column in the grid and are integers between 0 to 24. 
    private sameRow(index1: number, index2: number): boolean {
        if (Math.trunc(index1 / 5)  == Math.trunc(index2 / 5)) {
            return true;
        } else {
            return false;
        }
    }

    // Performs check to confirm that the characters are in the same column in the grid.
    // REQUIRES: parameters are in the same column in the grid and are integers between 0 to 24. 
    private sameColumn(index1: number, index2: number): boolean {
        if ((index1 - index2) % 5 == 0) {
            return true;
        } else {
            return false;
        }
    }

    
    // Performs the horizontal (row) movement required to decrypt the encrypted message.
    // replaces the characters with those directly to the left. Loops to the right if at the end of the grid.
    // REQUIRES: parameters are in the same column in the grid and are integers between 0 to 24.
    private moveOnSameRow(index1: number, index2: number) {
        if (index1 % 5 == 0) {
            index1 = index1 + 5;
        }
        if (index2 % 5 == 0) {
            index2 = index2 + 5;
        }
        index1 = index1 - 1;
        index2 = index2 - 1;

        this.writeToSolution(this.grid[index1], this.grid[index2]);

    }

    // Performs the vertical (column) movement required to decrypt the encrypted message.
    // replaces the characters with those directly above. Loops to the bottom if at the top of the grid.
    // REQUIRES: parameters are in the same column in the grid and are integers between 0 to 24. 
    private moveOnSameColumn(index1: number, index2: number) {
        if (index1 - 5 < 0) {
            index1 = index1 + 25;
        }
        if (index2 - 5 < 0) {
            index2 = index2 + 25;
        }
        index1 = index1 - 5;
        index2 = index2 - 5;

        this.writeToSolution(this.grid[index1], this.grid[index2]);
    }

    // Performs the diagonal (rectangle) movement required to decrypt the encrypted message.
    // REQUIRES: parameters form square in grid and are integers between 0 to 24. 
    private moveOnDiagonal(index1: number, index2: number) {
        const lowestModulatedIndex = Math.min((index1 % 5), (index2 % 5));
        const highestModulatedIndex = Math.max((index1 % 5), (index2 % 5));
        const movementCount = Math.abs(lowestModulatedIndex - highestModulatedIndex);

        if ((index1 % 5) > (index2 % 5)) {
            index1 = index1 - movementCount;
            index2 = index2 + movementCount;
        } else {
            index1 = index1 + movementCount;
            index2 = index2 - movementCount;
        }

        this.writeToSolution(this.grid[index1], this.grid[index2]);
        
    }

    // Writes the characters to the solution.
    private writeToSolution(char1: string, char2: string) {
        this.solution = this.solution + (char1 + char2);
    }

    // Removes the character X in case they are in the solution and converts entire string touppercase.
    // REQUIRES: All special character and spaces are removed prior to solving for the solution. 
    private cleanSolution() {
        this.solution = this.solution.replace(/X/g, "");
        this.solution = this.solution.toUpperCase();

    }

    private cleanString(stringParam: string): string {
        let returnString = stringParam.replace(/\s/g, "");
        returnString = returnString.replace(/[^a-zA-Z ]/g, "")

        return returnString
    }

    // Provides the solution based on the instantiation of the class. 
    public getSolution(): string {
        this.solve();
        this.cleanSolution();
        return this.solution;
    }
}

const solution = new Solution("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV");
console.log(solution.getSolution());
// The hidden message is:  HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA

// Answer to this test is: PLEASEHIREME
// const solution2 = new Solution("SHOPIFY", "IKGYHDOSNKND")
// console.log(solution2.getSolution());
