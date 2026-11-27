

/*
    @Param: message: string - Fairplay Cipher encrypted input
    Given a fairplay cipher in the form of a string as entirely UPPERCASE, the purpose of the function is to
    decrypt the input and return the decrypted message.
    The key used to create the grid for decrypting the message is SUPERSPY
*/
function decrypt(message:string): string {
    let result: string = "";

    //Map is used to utilize key uniqueness for ensuring no duplicate letters
    //The [number,number] value is used for tracking the position of that letter (key) found in the grid
    let letterSet: Map<string,[number,number]> = new Map();
    
    //create grid necessary for decrypting using the given key SUPERSPY
    let grid = createGrid("SUPERSPY",letterSet);
    //split the given message into an array of bigrams
    let bigramMessage: string[] = splitMessage(message);

    //for each bigram, translate it and append to the result string
    bigramMessage.forEach((element) => {
        let bigram: string[] = element.split("");
        result += translateBigram(bigram,grid,letterSet);
        
    })
    
    // remove ALL X found in the resulting string
    result = result.replace(/X/g,"");
    return result;
}

/*
    @Param: bigram: string[] - a bigram in the form of a string array
            grid: string[][] - a two dimensional string array used for decrypting the bigram
            letterSet:: Map<string,[number,number] - a Map with a string Key representing a letter and an array of two numbers representing the position in the grid

    The purpose is to translate the given bigram using the given grid and letterSet values. 
    The function returns the decrypted pair of letters in the form of a string
*/
function translateBigram(bigram:string[], grid: string[][], letterSet: Map<string,[number,number]>): string {
    let result: string = "";

    let pos0 = letterSet.get(bigram[0]);
    let pos1 = letterSet.get(bigram[1]);

    if (pos0 != undefined && pos1 != undefined) {
        
        if (pos0[0] == pos1[0]) { //same row, take left letter or wrap around to right side of grid if 0

            //Guards for wrapping around
            let columnIndexPos0 = pos0[1] - 1;
            let columnIndexPos1 = pos1[1] - 1;
            if (columnIndexPos0 < 0) {
                columnIndexPos0 = 4;
            }
            if (columnIndexPos1 < 0) {
                columnIndexPos1 = 4;
            }
            result = result.concat(result,grid[pos0[0]][columnIndexPos0],grid[pos1[0]][columnIndexPos1]);

        } else if (pos0[1] == pos1[1]) { // same column, take above letter or wrap around to bottom of grid if 0

            //Guards for wrapping around
            let rowIndexPos0 = pos0[0] + 1;
            let rowIndexPos1 = pos1[0] + 1;
            if (rowIndexPos0 > 4) {
                rowIndexPos0 = 0;
            }
            if (rowIndexPos1 > 4) {
                rowIndexPos1 = 0;
            }
            result = result.concat(result,grid[rowIndexPos0][pos0[1]],grid[rowIndexPos1][pos1[1]]);

        } else { //forms rectangle
            // uses the same row but the other's column
            result = result.concat(result,grid[pos0[0]][pos1[1]],grid[pos1[0]][pos0[1]]);

        }
    }
    

    return result;
}

// @Param: message: string - a string of the encrypted message
// The purpose of this function is to split the given message into bigrams and return the result as a string array
function splitMessage(message:string):string[] {
    let result: string[] = [];
    for (let i = 0; i < message.length; i += 2) {
        result.push(message.substring(i,i+2));
    }
    return result;
}



/*
    @Param key: string - a key word/string used for creating the grid needed for decryption
           letterSet: Map<string,[number,number] - a Map of string -> number pair where the key represents a letter and the number pair as the position in the grid

    The purpose is to create a grid given a key as a string and updating the mapping between a string and two numbers.
    the function returns a 2D string array representing a 5x5 grid that will be used for decryption where grid[i][j], i represents the row and j represents the column.

*/
// create the playfair grid in the form [[a,b,c,d,e],[f,g,h,i,j],[k,l,m,n,o],[p,q,r,s,t],[u,v,w,x,y]]
function createGrid(key: string,letterSet: Map<string,[number,number]>): string[][] {
    let j: number = 0; // j - keep track of row to fill
    let k: number = 0; // k - keep track of column to fill

    let playFairGrid:string[][] = [[],[],[],[],[]]; // resulting grid to return
    //insert unique letters in key into set
    for (let i = 0; i < key.length; i++) {
        // if letter set does not have character yet
        if (letterSet.has(key[i])) {
            // duplicate letter
        } else {

            
            letterSet.set(key[i],[j,k]);

            //Guards for special case I interchangable with J
            if (letterSet.has("I") && !letterSet.has("J")) {
                letterSet.set("J",[0,0]);
            }

            if (letterSet.has("J") && !letterSet.has("I")) {
                letterSet.set("I",[0,0]);
            }

            playFairGrid[j][k] = key[i];
            k++; //increment column to fill

            // if row contains 5, increment row and reset column number
            if (k > 4) {
                k = 0;
                j++;
                if (j > 4) {
                    return playFairGrid;
                }
            }
        }
    }
    
    let alphabet:string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    for (let i = 0; i < alphabet.length; i++) {
        if (letterSet.has(alphabet[i])) {
            // duplicate letter
        } else {
            letterSet.set(alphabet[i],[j,k]);
            //Guards for I == J interchange
            if (letterSet.has("I") && !letterSet.has("J")) {
                letterSet.set("J",[0,0]);
            }
            if (letterSet.has("J") && !letterSet.has("I")) {
                letterSet.set("I",[0,0]);
            }
            playFairGrid[j][k] = alphabet[i];
            k++;
            if (k > 4) {
                k = 0;
                j++;
                if (j > 4) {
                    return playFairGrid;
                }
            }
        }
    }
    return playFairGrid;
}

console.log(decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"));
