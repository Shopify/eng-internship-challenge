/*
Defining the constants that will be used throughout the program.
All strings in this program will be defined in UPPER CASE as per the spec.
*/
const encrypted_message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const encrypted_pairs = [];
const decrypted_pairs = [];

/*
Creating the 5x5 matrix with the cipher key inserted first (removing duplicates)
followed by the remaining letters in the alphabet (in order). The letter "J" is
neglected so that we have a round 25 numbers to make the matrix.
*/
const matrix = [
    ["S", "U", "P", "E", "R"],
    ["Y", "A", "B", "C", "D"],
    ["F", "G", "H", "I", "K"],
    ["L", "M", "N", "O", "Q"],
    ["T", "V", "W", "X", "Z"],
]

/*
Loop through the encrypted message and split all the characters up into pairs.
There are no duplicate characters next to each other in the encrypted message so there is no need to add X's.
The length of the encrypted message is even so there is no need to add X's at the end.
*/
for (let i = 0 ; i < encrypted_message.length - 1; i = i + 2) {
    let pair = [encrypted_message[i], encrypted_message[i+1]];
    encrypted_pairs.push(pair);
}

/*
Check whether or not the 2 letters in a pair reside in the same column of the matrix.
Loops through all the rows (1 column at a time) and checks if both letters are found. As this happens,
all the characters in the current column being looked at are appended to an array. This array is returned if
both letters are in the corresponding column. This allows us to avoid doing a duplicate search later on.
*/
const isSameColumn = (letter1, letter2) => {
    for (let col = 0; col < 5; col++) {
        let foundLetter1 = false;
        let foundLetter2 = false;
        let columnChars = [];

        for (let row = 0; row < 5; row++) {
            columnChars.push(matrix[row][col]);
            if (matrix[row][col] === letter1) {
                foundLetter1 = true;
            }
            if (matrix[row][col] === letter2) {
                foundLetter2 = true;
            }
        }

        if (foundLetter1 && foundLetter2) {
            return columnChars;
        }
    }
    return null;
};

/*
This function checks whether or not the 2 letters in a pair reside in the same row of the matrix.
It checks each row and if any of them include both of the letters then that row is returned.
Again, this allows us to avoid doing a duplicate search later on.
*/
const isSameRow = (letter1, letter2) => {
    for (let row of matrix) {
        if (row.includes(letter1) && row.includes(letter2)) {
            return row;
        }
    }
    return null;
};

/*
This function applies to pairs whose letters are either in the same column or row.
It can work for either since both functions above (isSameColumn, isSameRow) return arays
upon a successful search. Since we know the array is a length of 5, we can easily handle
the overflow case (letter is at index 0 so we change it to the letter at the end of array).
In all other cases, we just decrement the array index of the original letter. The array (pair)
of new letters will be returned.
*/
const rowColumnConvert = (letter1, letter2, arr) => {
    let new_letter1;
    let new_letter2;

    if (arr.indexOf(letter1) === 0) {
        new_letter1 = arr[4];
    } else {
        new_letter1 = arr[arr.indexOf(letter1) - 1];
    }

    if (arr.indexOf(letter2) === 0) {
        new_letter2 = arr[4];
    } else {
        new_letter2 = arr[arr.indexOf(letter2) - 1];
    }

    return [new_letter1, new_letter2]
}

/*
This is a helper function for the rectangleConvert function below.
Given a letter, it will find its (row, column) coordinates in the matrix.
*/
const findCoordinates = (letter) => {
    for (let row = 0; row < matrix.length; row++) {
        for (let col = 0; col < matrix[row].length; col++) {
            if (matrix[row][col] === letter) {
                return [row, col];
            }
        }
    }
    return null;
};

/*
This function will be called when a pair of letters are not in the same row or column.
It begins by finding the coordinates for each of the inputted letters and then defining
variables with each letter's respective row and column. For the new letters, the rows will
remain the same but the columns will be swapped to simulate moving to the opposite end of the
rectangle (as part of the rules for a Playfair Cipher). The array of new letters is returned.
*/
const rectangleConvert = (letter1, letter2) => {
    const coord1 = findCoordinates(letter1);
    const coord2 = findCoordinates(letter2);

    if (!coord1 || !coord2) {
        return null;
    }

    const row1 = coord1[0];
    const col1 = coord1[1];
    const row2 = coord2[0];
    const col2 = coord2[1];

    const new_letter1 = matrix[row1][col2];
    const new_letter2 = matrix[row2][col1];

    return [new_letter1, new_letter2];
};

/*
Looping through all the encrypted message pairs and checking whether or not the pair
of letters are in the same column or row. If they are, then we will use the rowColumnConvert
function to generate the new letters. Otherwise, the recentalgeConvert function is used. The
new pair of letters is then appeneded to the decrypted_pairs array.
*/
for (let pair of encrypted_pairs) {
    if (isSameColumn(pair[0], pair[1]) !== null ) {
        let col = isSameColumn(pair[0], pair[1]);
        let new_pair = rowColumnConvert(pair[0], pair[1], col);
        decrypted_pairs.push(new_pair);
    }
    else if (isSameRow(pair[0], pair[1]) !== null) {
        let row = isSameRow(pair[0], pair[1]);
        let new_pair = rowColumnConvert(pair[0], pair[1], row);
        decrypted_pairs.push(new_pair);
    }
    else {
        let new_pair = rectangleConvert(pair[0], pair[1]);
        decrypted_pairs.push(new_pair);
    }
}

// flattening the decrypted pairs array
let decrypted_message = decrypted_pairs.reduce((acc, curr) => acc.concat(curr), []);

// filtering out all instances of "X" from the decrypted message and then converting the array to a string 
decrypted_message = decrypted_message.filter(letter => letter !== "X").join('');

// printing out the decrypted message
console.log(decrypted_message)