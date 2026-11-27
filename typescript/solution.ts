const encrypted: string = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"; 
const key: string = "SUPERYABCDFGHIKLMNOQTVWXZ"; 

// Function to convert the key to a 5x5 matrix
function strToMatrix(key: string): string[][] {
    const n: number = Math.sqrt(key.length);
    const matrix: string[][] = [];

    // Loop over the characters in the key and create a 5x5 matrix
    for (let i = 0; i < n; i++) {
        const row: string[] = [];
        for (let j = 0; j < n; j++) {
            const index: number = i * n + j;
            row.push(key[index]);
        }
        matrix.push(row);
    }

    return matrix;
}

// Function to decrypt the encrypted text
function decrypt(encrypted: string, key: string): string {

    //first we need to convert the key to a 5x5 matrix so we can perform the decryption
    const keyMatrix: string[][] = strToMatrix(key);
    let decrypted: string = "";

    // Loop over the encrypted text in pairs
    // Since we are given the encrypted text, we want to perform the reverse operation of the encryption to return to the original message
    // So when the letters are in the same Row - we move them one to the left
    // When the letters are in the same Column - we move them one up
    // When the letters are in a rectangle - we swap the letters by taking the row of the first letter and the column of the second letter, and vice versa
    for(let i = 0; i < encrypted.length; i += 2) {
        const letter1: string = encrypted[i];
        const letter2: string = encrypted[i + 1];

        // Find the position of the letters in the key matrix
        const position1: number[] = findPosition(keyMatrix, letter1);
        const position2: number[] = findPosition(keyMatrix, letter2);

        // If the letters are in the same row
        if (position1[0] === position2[0]) {
            // Using the modulo operator to account for the edge case where the letter is at the end of the row we move all letters one to the left
            decrypted += keyMatrix[position1[0]][(position1[1] + 4) % 5];
            decrypted += keyMatrix[position2[0]][(position2[1] + 4) % 5];
        } else if(position1[1] === position2[1]) {
            // Again using the modulo operator to account for the edge case where the letter is at the end of the column we move all letters one down
            decrypted += keyMatrix[(position1[0] + 4) % 5][position1[1]];
            decrypted += keyMatrix[(position2[0] + 4) % 5][position2[1]];
        }else{
            // Lastly if the letters are positioned in a rectangle, we swap the letters by taking the row of the first letter and the column of the second letter, and vice versa
            decrypted += keyMatrix[position1[0]][position2[1]];
            decrypted += keyMatrix[position2[0]][position1[1]];
        }
    }
    // Return the decrypted text
    return decrypted; 
}


// Function to find the position of a given letter in the matrix
function findPosition(matrix: string[][], letter: string): number[] {
    // Loop over the matrix and find the position of the given letter
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[i].length; j++) {
            if (matrix[i][j] === letter) {
                return [i, j];
            }
        }
    }
    return [-1, -1];
}


// Function to remove the X's from the text, since X is used as a filler character when adjacent letters are duplicates
function removeXfromString(text: string): string {
    let result = "";
    // We loop over the given text and if the letter is not an X we add it to the result
    for(let i = 0; i < text.length; i++){
        if(text[i] !== "X"){
            result += text[i];
        }
    }
    return result;
}


// Decrypt the encrypted text and remove the X's from the decrypted text
const decrypted: string = decrypt(encrypted, key);
console.log(removeXfromString(decrypted)); 