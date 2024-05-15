// Generate Key Table, ommiting 'J' and duplicate characters
const keyTable = [
    'S', 'U', 'P', 'E', 'R',
    'Y', 'A', 'B', 'C', 'D',
    'F', 'G', 'H', 'I', 'K',
    'L', 'M', 'N', 'O', 'Q',
    'T', 'V', 'W', 'X', 'Z'
];

message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
let pairs = [];


// Split message into pairs of characters
for (let i = 0; i < message.length; i+=2) {
    let first = message[i];
    let second;
    // Handle odd length message
    if (i === message.length - 1) {
        second = 'X';
    } else {
        second = message[i + 1];
    }
    // If both characters are the same, replace the second character with 'X', and decrement i
    if (first === second) {
        second = 'X';
        i--;
    }
    pairs.push([first, second]);
}


// Function to find the position of a character in the keyTable
function findPosition(char) {
    for (let row = 0; row < 5; row++) {
        for (let col = 0; col < 5; col++) {
            if (keyTable[row * 5 + col] === char) {
                return [row, col];
            }
        }
    }
}

// Find the row and column positions of each pair of characters
positions = [];
for (let i = 0; i < pairs.length; i++) {
    const pos1 = findPosition(pairs[i][0]);
    const pos2 = findPosition(pairs[i][1]);
    positions.push([pos1, pos2]);
}

answer = '';
for (let i = 0; i < positions.length; i++) {
    let decryptedString = '';
    
    const pos1 = positions[i][0];
    const pos2 = positions[i][1];
    
    if (pos1[0] === pos2[0]) { // Same row, replace each character with the one on its left
        decryptedString += keyTable[pos1[0] * 5 + (pos1[1] + 4) % 5];
        decryptedString += keyTable[pos2[0] * 5 + (pos2[1] + 4) % 5];
    } else if (pos1[1] === pos2[1]) { // Same column, replace each character with the one above it
        decryptedString += keyTable[((pos1[0] + 4) % 5) * 5 + pos1[1]];
        decryptedString += keyTable[((pos2[0] + 4) % 5) * 5 + pos2[1]];
    } else { // Replace each character with the same row but diff column
        decryptedString += keyTable[pos1[0] * 5 + pos2[1]];
        decryptedString += keyTable[pos2[0] * 5 + pos1[1]];
    }

    answer += decryptedString;
}

// Remove any 'X' characters to clean up the message
answer = answer.replace(/X/g, ''); 

console.log(answer);
