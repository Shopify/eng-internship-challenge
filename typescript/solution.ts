class solution{ //defined a class to perform the decryption
    private size: number = 5; //defined the size of the table which is 5x5
    private table: string [][] = []; //declared an empty table to store the grid

    //constructor to initialize the cipher with a keyword
    constructor(private keyword: string) {
        this.table = this.createTable(this.keyword); //create the cipher table using the keyword and calling the createTable method
    }

    //method to create the table for the grid
    private createTable(keyword: string): string[][]{
        const table: string[][] = []; //empty local variable to store table 
        const set = new Set<string>(); //using a set for data structure to preserve order and avoid duplicates
        const newKeyword = keyword.replace(/j/ig, 'i').toUpperCase(); //change the keyword to replace 'J' with 'I' and convert to uppercase
        //the i after '/j/' means it will search for j ignoring its case and g makes it so it will be global replacing all occurences of j

        //now we add all adjusted letters from the keyword to the set without duplicates
        for(const char of newKeyword){
            if(!set.has(char) && char.match(/[a-i]|[k-z]/i)){ //checks duplicates and matches letters excluding j while being case-insensitive
                set.add(char); //given the conditions are fulfilled, adds char to the set
            }
        }

        //now we fill the set with the rest of the letters of the alphabet
        for(let char = 65; char<=90; char++){ //traversing through letters
            const letter = String.fromCharCode(char); //converting ASCII to letter
            if(!set.has(letter) && letter !== 'J'){ //check if its not J and set does not have it already
                set.add(letter);
            }
        }

        //we convert the set to an array and start filling our empty table row by row
        const rowTable = Array.from(set); //array stored in rowTable
        for(let i = 0; i < this.size; i++){
            table.push(rowTable.slice(i*this.size, (i+1)*this.size)); //we use the size variable which was 5 to create slices of the array 5 at a time and push them to the grid table
        }

        return table; //we return the grid for further decryption
    }

    //we now define a method to find positions of letters in the grid table
    private findLetterPosition(letter: string): [number, number]{
        //iterating through each row and column of the table
        for(let row = 0; row<this.size; row++){
            for(let col = 0; col<this.size; col++){ //double loop iterating through both row and column
                if(this.table[row][col] === letter){ //checking if the current call has the letter
                    return [row, col]; //return the row and col value that make the position
                }
            }
        }
        
        return [-1, -1]; //default return if letter not found which ideally should not happen
    }

    //method to decrypt the encyrpted cipher message using the 3 different cases
    public decryption(encryptedText: string): string{
        const pairs = this.prepareText(encryptedText.toUpperCase().replace(/j/ig, 'i')); //call preparetext method and conver to uppercase while replacing j with i
        let decryptedText = '';

        //we process the encrypted text pair by pair
        for(const [first, second] of pairs){
            const [row1, col1] = this.findLetterPosition(first); //finding letter position of the first one in the pair
            const [row2, col2] = this.findLetterPosition(second); //finding letter position of the second one in the pair

            //decrypt based on relative positions using the 3 cases possible
            if(row1 === row2){
                //if row is same, shift each letter one position to the left, wrapping around to the end when needed
                decryptedText += this.table[row1][(col1 + this.size - 1) % this.size];
                decryptedText += this.table[row2][(col2 + this.size - 1) % this.size];
            }
            else if(col1 === col2){
                //if column is same, shift each letter one position up, wrapping around the bottom when needed
                decryptedText += this.table[(row1 + this.size - 1) % this.size][col1];
                decryptedText += this.table[(row2 + this.size - 1) % this.size][col2];
            }
            else{
                // Rectangle swap: swap the columns of the two letters if first two cases are not present
                decryptedText += this.table[row1][col2];
                decryptedText += this.table[row2][col1];
            }
        }

        return decryptedText.replace(/X/g, ''); //return the decrypted text omitting X
    }

    //helper method to prepare the text and pair them for decryption
    private prepareText(text: string): [string, string][]{
        const newText = text.replace(/[^A-IK-Z]/ig, ''); //removing non-letter characters and convert J to I
        const pairs: [string, string][] = []; //empty variable pairs to store pairs

        //creating pairs using the newText
        for(let i = 0; i < newText.length; i+=2){
            const first = newText[i]; //first letter of the pair
            const second = i + 1 < newText.length ? newText[i+1] : 'X'; //second letter of the pair or X if none is available as per cipher rules
            
            pairs.push([first, second]); // add the pair to the list pairs
        }

        return pairs; //we return the list of adjusted pairs for decryption
    }
}

const cipher = new solution('SUPERSPY');
const encryptedMessage = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
const decryptedMessage = cipher.decryption(encryptedMessage);

console.log(decryptedMessage);