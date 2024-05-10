const encryptedText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const answerText = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA";
const cipherKey = "SUPERSPY";

// Original keyTable Matrix
// const keyTable = [
//     ["S", "U", "P", "E", "R"],
//     ["Y", "A", "B", "C", "D"],
//     ["F", "G", "H", "I", "K"],
//     ["L", "M", "N", "O", "Q"],
//     ["T", "V", "W", "X", "Z"]
// ];

/**
 * Transposed keyTable for coordinate system to be in format: [x][y].
 * Otherwise, coordinates are flipped.
 */
const keyTable = [
    ["S", "Y", "F", "L", "T"],
    ["U", "A", "G", "M", "V"],
    ["P", "B", "H", "N", "W"],
    ["E", "C", "I", "O", "X"],
    ["R", "D", "K", "Q", "Z"]
];

/**
 * Represents the key table where letters are mapped to
 * coordinates on 5x5 grid. Origin is top-left:
 *      S U P E R
 *      Y A B C D
 *      F G H I K
 *      L M N O Q
 *      T V W X Z
 */
const keyTableMap = {
    "S": [0, 0],
    "U": [1, 0],
    "P": [2, 0],
    "E": [3, 0],
    "R": [4, 0],
    "Y": [0, 1],
    "A": [1, 1],
    "B": [2, 1],
    "C": [3, 1],
    "D": [4, 1],
    "F": [0, 2],
    "G": [1, 2],
    "H": [2, 2],
    "I": [3, 2],
    "K": [4, 2],
    "L": [0, 3],
    "M": [1, 3],
    "N": [2, 3],
    "O": [3, 3],
    "Q": [4, 3],
    "T": [0, 4],
    "V": [1, 4],
    "W": [2, 4],
    "X": [3, 4],
    "Z": [4, 4]
};

/**
 * Decrypts playfair cipher encrypted text.
 * @param {String} encryptedText 
 * @returns String - decrypted text
 */
function playfairDecryptor(encryptedText) {
    const splitTextArr = splitEncText(encryptedText);
    const decryptedText = decrypt(splitTextArr).toUpperCase();
    const decryptedTextNoX = decryptedText.replace(/X/g, "");
    console.log(decryptedTextNoX);
}

/**
 * Splits encrypted text into pairs of letters.
 * @param {String} text 
 * @returns String[]
 */
function splitEncText(text) {
    const pairs = [];

    // Encrypted text should always have even length.
    for (let i = 0; i < text.length; i += 2) {
        pairs.push(text.substring(i, i + 2));
    }

    return pairs;
}


/**
 * Decrypts encrypted text represented as pairs of letters.
 * @param {String[]} encTxtArr
 * @returns String - decrypted string
 */
function decrypt(encTextArr) {
    let decryptedText = "";

    for (const pair of encTextArr) {
        let decryptedPair = "";

        const letterPair = pair.split("");
        const firstCoords = keyTableMap[letterPair[0]];
        const secondCoords = keyTableMap[letterPair[1]];

        if (firstCoords[0] === secondCoords[0]) {
            // handle column case
            decryptedPair = decryptColumnRule(letterPair[0], letterPair[1]);
        } else if (firstCoords[1] === secondCoords[1]) {
            // handle row case
            decryptedPair = decryptRowRule(letterPair[0], letterPair[1]);
        } else {
            // handle rectangle case
            decryptedPair = decryptRectRule(letterPair[0], letterPair[1]);
        }

        decryptedText += decryptedPair;
    }

    return decryptedText;
}

/**
 * Returns letters located 1 unit above the given letters in the key
 * table. Wraps around if table limits are exceeded.
 * @returns String - decoded letter pair
 */
function decryptColumnRule(l1, l2) {
    const firstCoords = keyTableMap[l1];
    const secondCoords = keyTableMap[l2];
    let newFirstCoords = [firstCoords[0], firstCoords[1] - 1];
    let newSecondCoords = [secondCoords[0], secondCoords[1] - 1];

    // Wrap around
    if (newFirstCoords[1] < 0) {
        newFirstCoords[1] = 4;
        newSecondCoords[1] = 4;
    }

    const decFirstLetter = keyTable[newFirstCoords[0]][newFirstCoords[1]];
    const decSecondLetter = keyTable[newSecondCoords[0]][newSecondCoords[1]];
    
    return decFirstLetter + decSecondLetter;
}

/**
 * Returns letters located 1 unit to the left of the given letters in
 * the key table. Wraps around if table limits are exceeded.
 * @returns String - decoded letter pair
 */
function decryptRowRule(l1, l2) {
    const firstCoords = keyTableMap[l1];
    const secondCoords = keyTableMap[l2];
    let newFirstCoords = [firstCoords[0] - 1, firstCoords[1]];
    let newSecondCoords = [secondCoords[0] - 1, secondCoords[1]];

    // Wrap around
    if (newFirstCoords[0] < 0) {
        newFirstCoords[0] = 4;
        newSecondCoords[0] = 4;
    }

    const decFirstLetter = keyTable[newFirstCoords[0]][newFirstCoords[1]];
    const decSecondLetter = keyTable[newSecondCoords[0]][newSecondCoords[1]];
    
    return decFirstLetter + decSecondLetter;
}

/**
 * Switches the x-coordinates of given coordinates.
 * @returns String - decoded letter pair
 */
function decryptRectRule(l1, l2) {
    const firstCoords = keyTableMap[l1];
    const secondCoords = keyTableMap[l2];

    // Flip x-coordinates
    let newFirstCoords = [secondCoords[0], firstCoords[1]];
    let newSecondCoords = [firstCoords[0], secondCoords[1]];

    const decFirstLetter = keyTable[newFirstCoords[0]][newFirstCoords[1]];
    const decSecondLetter = keyTable[newSecondCoords[0]][newSecondCoords[1]];
    
    return decFirstLetter + decSecondLetter;
}

playfairDecryptor(encryptedText);