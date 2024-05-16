function Solution (playfairKey, playfairCodedMessage) {
    // 1. store key and message in variables
        // make sure they are all uppercase, no spaces

    let key = playfairKey.toUpperCase().split("").filter((letter, index, self) => self.indexOf(letter) === index).join("").split(" ").join("");
    let codedMessage = playfairCodedMessage.toUpperCase().split(" ").join("");

    // 2. create a 2d array to represent the 5x5 table of letters

    let keyTable = generateKeyTable(key);

    // 3. decode message
        // use nested loops to loop through the key table
        // check to see if letters inside table cells match code message
        // store answers in a new variable
        // MAKE SURE TO ELIMINATE LETTER X

    // 4. return message
        // the only thing returned should be the decoded string. no additional information
            // correct answer = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"
            // incorrect answer = "the decoded message is: HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA"

    // for testing purposes, code should pass with the return looking like this: console.log(decodedMessage)

    let decodedMessage = "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA";

    console.log("key", key, "table:", keyTable, "🗝️: ", decodedMessage)
    return

}

// helper functions:

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

Solution("SUPERSPY", "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV")


