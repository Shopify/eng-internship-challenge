
const testString = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const keyString = "SUPERSPY"

const generateKeyMatricesFromKey=(key)=>{
    // so the matrix should be 
    //   0 1 2 3 4 (x)
    // 0 S U P E R 
    // 1 Y A B C D 
    // 2 F G H I K 
    // 3 L M N O Q 
    // 4 T V W X Z
    //(y)
    
    //should I just make a simple dictionary or a 2D array? 
    //so the object can look like 
    //  {"S":[0,0],"U":[1,0]}    
    //or we can have an array that looks like this and then we can figure out the indices of those like S is gonna be 0, 0 
    //  [["S","U","P","E","R"],["Y",...]]
    //I'm gonna go with an object/dictionary. It's more intuitive for me

    
    const baseString = "ABCDEFGHIKLMNOPQRSTUVWXYZ" //SKIPPING J
    const combinedString = key+baseString
    
    const keyArray = [... new Set(combinedString)];

    const keyMatrix = {}
    const indexMatrix = {}
    keyArray.forEach((letter,index)=>{
    
        const column = index%5 //the x coordinate
        const row = Math.floor(index/5) //the y coordinate

        keyMatrix[letter] = [column,row] //key in a letter to get the coordinates
        indexMatrix[[column,row]]=letter //key in coordinates to get the letter
    })
    
    return [keyMatrix, indexMatrix]
}




const solvePlayfair=(inputString,keyString)=>{
    //just made a lookup table and a reverse lookup table
    const [coordsDict,lettersDict] = generateKeyMatricesFromKey(keyString);

    let solution = ""
    for(let i=0; i<inputString.length; i=i+2){
        //now I saw that the inputstring has I already so the key matrix has to have I, so this might be unnecessary but with this you can remove all Is and use an inputString with J
        const firstLetter = inputString[i] === 'J' ? 
                            'I'
                            :inputString[i]

        const [x1,y1] = coordsDict[firstLetter];
        
        const secondLetter = inputString[i+1] === 'J' ? 
                              'I'
                              :inputString[i+1]
                            
        const [x2,y2] = coordsDict[secondLetter];
        
        let firstAnswer=""
        let secondAnswer=""

        //if they are from the same row
        if(y1===y2){
            //so you have to grab the character one place left of this one, also gotta be careful of negative numbers, would have preferred modulo but js modulo returns negative values 
            firstAnswer =  lettersDict[
                            [x1==0 ? 4 : x1-1 ,
                            y1]
                            ]

            secondAnswer = lettersDict[
                            [x2==0 ? 4 : x2-1 ,
                            y1]
                            ]
        }else if(x1===x2){

            //so this means same column, grab the character one place above this one
            firstAnswer =  lettersDict[
                            [x1 ,
                            y1==0 ? 4 : y1-1]
                            ]

            secondAnswer = lettersDict[
                        [x1 ,
                        y2==0 ? 4 : y2-1]
                        ]
        }else{
            //this should make a rectangle, and we gotta grab each other's x coordinates
            firstAnswer = lettersDict[[x2,y1]]
            secondAnswer = lettersDict[[x1,y2]]
        }

        if(firstAnswer!='X'){
            solution += firstAnswer
        }
        if(secondAnswer!='X'){
            solution += secondAnswer
        }

    }
    return solution
}



// looks like the answer is HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA - fear of long words.
console.log(solvePlayfair(testString,keyString))
 
