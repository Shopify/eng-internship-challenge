function Solution (playfairKey, playfairCodedMessage) {

    let key = playfairKey.toUpperCase().split("").filter((letter, index, self) => self.indexOf(letter) === index).join("").split(" ").join("");
    let codedMessage = playfairCodedMessage.toUpperCase().split(" ").join("");

    let keyTable = generateKeyTable(key);

    let decodedMessage = "";
    for (let i = 0; i < codedMessage.length; i += 2) {
        let pair = codedMessage.substr(i, 2);
        let decodedPair = decodePairs(pair[0], pair[1], keyTable);
        decodedMessage += decodedPair;
    }

    decodedMessage = decodedMessage.replace(/X/g, '');

    console.log(decodedMessage)
    return

}

// helper functions below:

// this function generates the 5x5 key table
function generateKeyTable(key) {
    // remove duplicate letters in key
    // create empty array to store 2d array
    // create variable to keep track of the key string
    // loop through each cell of 2d array
    // fill the table using the key & the alphabet (omit letter J)
    // make sure to never use a letter twice in the table 

    // let cleanKey = key.split('').filter((letter, index, self) => self.indexOf(letter) === index).join('');

    let keyTable = [];
    let keyIndex = 0;
    let keyLetters = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

    for (let i = 0; i < 5; i++) {
        let tableRow = [];
        for (let j = 0; j < 5; j++) {
            if (key[keyIndex]) {
                tableRow.push(key[keyIndex]);
                keyLetters = keyLetters.replace(key[keyIndex], "");
                keyIndex++;
            } else {
                let newLetter = keyLetters.charAt(0);
                tableRow.push(newLetter);
                keyLetters = keyLetters.substring(1);
            }
        }
        keyTable.push(tableRow);
    }

    return keyTable;
}

// this function decodes the pairs of letters in the coded message
function decodePairs(pair1, pair2, keyTable) {

    let pair1Row, pair1Col, pair2Row, pair2Col;

    for (let i = 0; i < 5; i++) {
        for (let j = 0; j < 5; j++) {
            if (keyTable[i][j] === pair1) {
                pair1Row = i;
                pair1Col = j;
            }
            if (keyTable[i][j] === pair2) {
                pair2Row = i;
                pair2Col = j;
            }
        }
    }

    let decodedPair = "";

    if (pair1Row === pair2Row) {
        decodedPair += keyTable[pair1Row][(pair1Col - 1 + 5) % 5];
        decodedPair += keyTable[pair2Row][(pair2Col - 1 + 5) % 5];
    } else if (pair1Col === pair2Col) { 
        decodedPair += keyTable[(pair1Row - 1 + 5) % 5][pair1Col];
        decodedPair += keyTable[(pair2Row - 1 + 5) % 5][pair2Col];
    } else {
        decodedPair += keyTable[pair1Row][pair2Col];
        decodedPair += keyTable[pair2Row][pair1Col];
    }

    return decodedPair;

}

Solution("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")

"HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
"HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"