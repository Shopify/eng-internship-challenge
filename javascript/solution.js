let key= "SUPERSPY"
let message = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"

function getSquareGrid(key){
    let keyGrid = new Array(5);
    for(let i = 0; i < 5; ++i)
        keyGrid[i] = new Array(5);


    //Get the key into uppercase;
    key.toUpperCase();

    //Create a dictionary to check if the letter is appeared or not
    let isAppeared = {};
    // Current position on the key
    let currentPosition = 0;

    let currentI = 0;
    let currentJ = 0;

    for(let i = 0; i < 5; ++i){
        //If we have already gone through the whole key
        if(currentPosition == key.length)
            break;
        for(let j = 0; j < 5; ++j){
            //Skip duplicate
            while(currentPosition < key.length && isAppeared[key[currentPosition]]){
                currentPosition++;
            }
            if(currentPosition == key.length){
                currentI = i;
                currentJ = j; 
                break;
            }
            if(currentPosition < key.length){
                isAppeared[key[currentPosition]] = true;
                keyGrid[i][j] = key[currentPosition];
                currentPosition++;
            }
        }
    }
    let currentAlphabet = 'A';
    for(let i = currentI; i < 5; ++i)
        //Start from the previous stop, when i == currentI or start from the begining of new rows in the next row
        for(let j = (i == currentI) ? currentJ : 0; j < 5; ++j){
            //Assume that I is equal to J
            while(isAppeared[currentAlphabet] || currentAlphabet == 'J')
                currentAlphabet = String.fromCharCode(currentAlphabet.charCodeAt(0) + 1);
            keyGrid[i][j] = currentAlphabet;
            currentAlphabet = String.fromCharCode(currentAlphabet.charCodeAt(0) + 1);
        }   
    return keyGrid;
}

//This function will get the position of the character in the keyGrid
function getPosition(keyGrid, character){
    for(let i = 0; i < 5; ++i)
        for(let j = 0; j < 5; ++j){
            if(character == keyGrid[i][j])
                return [i, j];
            if(character == 'J' && keyGrid == 'I')
                return [i, j];
        }
}

function decrypt(keyGrid, message){
    //filter the encrypted message, and transform them all into upper case
    message = message.toUpperCase();
    
    //Sanitize the input
    let sanitizedMessage = '';
    for(let i = 0; i < message.length; ++i)
        if(65 <= message.charCodeAt(i) && message.charCodeAt(i) <= 90)
            sanitizedMessage += message[i];
    message = sanitizedMessage;

    let returnMessage = '';
    for(let i = 0; i < message.length; i += 2){

        let [firstCharRow, firstCharColumn] = getPosition(keyGrid, message[i]); 
        let [secondCharRow, secondCharColumn] = getPosition(keyGrid, message[i + 1]);

        //If in the same row
        if(firstCharRow == secondCharRow){
            //Take remainder for wrap around case;
            returnMessage += keyGrid[firstCharRow][((firstCharColumn - 1) + 5) % 5];
            returnMessage += keyGrid[secondCharRow][((secondCharColumn - 1) + 5) % 5];
        }else if(firstCharColumn == secondCharColumn){
            //If they are in the same column
            returnMessage += keyGrid[(firstCharRow + 1) % 5][firstCharColumn];
            returnMessage += keyGrid[(secondCharRow + 1) % 5][secondCharColumn];
        }else{
            //If they form a rectangle, swap place
            returnMessage += keyGrid[firstCharRow][secondCharColumn];
            returnMessage += keyGrid[secondCharRow][firstCharColumn];
        }
    }

    //sanitize the return message, remove X
    returnMessage = returnMessage.split('X').join('');
    return returnMessage;
}


let keyGrid = getSquareGrid(key);

console.log(decrypt(keyGrid,message));