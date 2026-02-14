function playFairCipher(encryptedString) {

    //Hard coded the grid our key is constant and the rest of the alphabet is constant
    let cipherGrid = [
        ['S', 'U', 'P', 'E', 'R'],
        ['Y', 'A', 'B', 'C', 'D'],
        ['F', 'G', 'H', 'I', 'K'],
        ['L', 'M', 'N', 'O', 'Q'],
        ['T', 'V', 'W', 'X', 'Z']
    ];
    
    //Storing the manipluated string
    let stringResult = '';

    //Seperating decrypted string into groups of 2
    let groupedString = encryptedString.match(/.{1,2}/g);

    //We are iterating through each pairing
    groupedString.forEach(pair => {
        // Splitting the pair into two seperate characters
        let [char1, char2] = pair.split(''); 

        let pos1 = findCharPosition(char1, cipherGrid); // Find position of first character
        let pos2 = findCharPosition(char2, cipherGrid); // Find position of second character

        //Check if there is either no positon for character 1 or character 2
        if (!pos1 || !pos2) {
            stringResult += 'X'; // Handle characters not found in the cipherGrid
            return; // Skip to the next iteration
        }

        let [row1, col1] = pos1;
        let [row2, col2] = pos2;

        //Store thr decrypted pair from the iteration in this variable
        let decryptedPair = '';

        // First Rule : characters in the same row
        if (row1 === row2) {
            decryptedPair += cipherGrid[row1][(col1 + 4) % 5]; 
            decryptedPair += cipherGrid[row2][(col2 + 4) % 5]; 
        }
        // Second Rule : characters in the same column
        else if (col1 === col2) {
            decryptedPair += cipherGrid[(row1 + 4) % 5][col1]; 
            decryptedPair += cipherGrid[(row2 + 4) % 5][col2];
        }
        // Third Rule : characters form a rectangle
        else {
            decryptedPair += cipherGrid[row1][col2]; 
            decryptedPair += cipherGrid[row2][col1]; 
        }

        stringResult += decryptedPair;
    });

    // Remove the X's inorder to find the decrypted word
    let result = stringResult.split("").filter(char => char !== 'X').join("")

    return result;
}

//This function will find the charaters position in the grid and retrn null if not found
function findCharPosition(char, grid) {
    for (let row = 0; row < grid.length; row++) {
        for (let col = 0; col < grid[row].length; col++) {
            if (grid[row][col] === char) {
                return [row, col];
            }
        }
    }
    return null; 
}

// Example usage:

const decryptedMessage = playFairCipher("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV");
console.log(decryptedMessage); 

