const message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
const key = "SUPERSPY"
const grid = []

const getIndexOfLetter = (letter) => {
    for (let i = 0; i < grid.length; i++) {
        let index = grid[i].indexOf(letter)

        // only return if letter is found in current row
        if(index > -1) {
            return [i, index]
        }
    }
}

const fillGrid = (key) => {
    // Alphabet without J 
    const alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    // combine key and alphabet while removing duplicates, special characters and any spaces that may have been in the key
    const gridChars = [...new Set((key + alphabet).replace(/[^a-zA-Z ]/g, "").split("").map(letter => letter.toUpperCase()).filter(letter => !(letter === " " || letter === "J")))]


    // keep track of letter to add to grid
    let count = 0
    for (let i = 0; i < 5; i++) {
        const row = []
        for (let j = 0; j < 5; j++) {
            // populate row
            row.push(gridChars[count])
            count += 1
        }
        // add a new row to the grid
        grid.push(row)
    }
}

const sameRow = (firstIndexes, secondIndexes) => {
    let text = ""

    
    if (firstIndexes[1] === 0) {
        // if the letter is first in its row wrap around to end of the row
        text += grid[firstIndexes[0]][4]
    } else {
        // otherwise move one spot to the left in the row
        text += grid[firstIndexes[0]][firstIndexes[1] - 1]
    }

    if (secondIndexes[1] === 0) {
        // if the letter is first in its row wrap around to end of the row
        text += grid[secondIndexes[0]][4]
    } else {
        // otherwise move one spot to the left in the row
        text += grid[secondIndexes[0]][secondIndexes[1] - 1]
    }

    return text
}

const sameCol = (firstIndexes, secondIndexes) => {
    let text = ""

    if (firstIndexes[0] === 0) {
        // if the letter is first in its column wrap around to bottom of the column
        text += grid[4][firstIndexes[1]]
    } else {
        // otherwise move one spot up in the column
        text += grid[firstIndexes[0] - 1][firstIndexes[1] ]
    }

    if (secondIndexes[0] === 0) {
        // if the letter is first in its column wrap around to bottom of the column
        text += grid[4][secondIndexes[1]]
    } else {
         // otherwise move one spot up in the column
        text += grid[secondIndexes[0] - 1][secondIndexes[1]]
    }

    return text
}

const swapPos = (firstIndexes, secondIndexes) => {
    let text = ""

    // create a box with the two letters being the corners and swap the letters with the corner in the same row
    text += grid[firstIndexes[0]][secondIndexes[1]]
    text += grid[secondIndexes[0]][firstIndexes[1]]

    return text
}

const removeXs = (text) => {
    const newText = text.split("").filter(letter => letter !== "X")

    return newText.join("").toString()
}

const decrypt = (message, key) => {
    let decrypted = ""
    // Fill grid using the key
    fillGrid(key)

    // remove any spaces or special characters from the message and convert to uppercase
    message = message.split("").filter(letter => letter !== " ").map(letter => letter.toUpperCase()).join("").toString().replace(/[^a-zA-Z ]/g, "")
    // loop through to split letters into pairs
    for (let i = 0; i < message.length / 2; i++) {
        let index = 0
        // multiply index by 2 since we check two indexes at once
        if (i > 0) {
            index = i * 2
        }

        // Get indexes for the first letter in the pair
        let firstIndexes = getIndexOfLetter(message.charAt(index))
        // Get indexes for the second letter in the pair
        let secondIndexes = getIndexOfLetter(message.charAt(index+1))


        if (firstIndexes[0] === secondIndexes[0]) {
            // if pair of letters are in the same row
            decrypted += sameRow(firstIndexes, secondIndexes)
        } else if (firstIndexes[1] === secondIndexes[1]) {
            // if pair of letters are in the same column
            decrypted += sameCol(firstIndexes, secondIndexes)
        } else {
            // if pair of letters are not in the same row or column
            decrypted += swapPos(firstIndexes, secondIndexes) 
        }
    }

    // return the decrypted text without any Xs
    return(removeXs(decrypted))
}

console.log(decrypt(message, key))
