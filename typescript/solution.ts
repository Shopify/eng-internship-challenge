/**
* Abdullah Morrison
*/

const table: string[][] = []
const tableMap: Map<string, number[]> = new Map() //maps the letter to the table index (H->[1,2]) for O(1) retrieval
function createTable(keyword: string){
  const alphabetWithoutJ = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
  const seenLetters = new Set<string>() 

  let keywordIdx = 0
  let alphabetIdx = 0
  for(let i=0; i<5; i++){
    table[i]=[] //new row

    for(let j=0; j<5; j++){
      if(keywordIdx<keyword.length){ // adding letters from keyword into table
        let letter = keyword.charAt(keywordIdx)

        while(letter && seenLetters.has(letter)){//making sure letter is unique
          keywordIdx++
          letter = keyword.charAt(keywordIdx)
        }
        if(!letter) throw new Error("Letter not found")

        seenLetters.add(letter)
        table[i][j] = letter
        tableMap.set(letter, [i, j])

        keywordIdx++
      }else{ //adding letters from alphabet into table
        let letter = alphabetWithoutJ.charAt(alphabetIdx)
        while(letter && seenLetters.has(letter)){//making sure letter is unique
          alphabetIdx++
          letter = alphabetWithoutJ.charAt(alphabetIdx)
        }
        if(!letter) throw new Error("Letter not found")

        table[i][j] = letter
        tableMap.set(letter, [i, j])

        alphabetIdx++
      }
    }
  }

  return table
}

function decryptDiagram(diagram: string){
  const letter1 = diagram.charAt(0)
  const letter2 = diagram.charAt(1)

  if(!letter1 || !letter2 ) throw new Error("Letter not found")

  const [row1, col1] = tableMap.get(letter1)!
  const [row2, col2] = tableMap.get(letter2)!

  let decryptedLetter1: string
  let decryptedLetter2: string
  if(row1==row2){
    decryptedLetter1 = table[row1][(col1+5-1)%5]
    decryptedLetter2 = table[row2][(col2+5-1)%5]
  }else if(col1==col2){
    decryptedLetter1 = table[(row1+5-1)%5][col1]
    decryptedLetter2 = table[(row2+5-1)%5][col2]
  }else{//rectangle
    decryptedLetter1 = table[row1][col2]
    decryptedLetter2 = table[row2][col1]
  }

  return decryptedLetter1+decryptedLetter2
}

function decryptMessage(encryptedMessage: string, keyword: string){
  let result = ""

  createTable(keyword)
  for(let i=1; i<encryptedMessage.length; i+=2){
    const diagram = encryptedMessage.charAt(i-1) +""+ encryptedMessage.charAt(i)
    result += decryptDiagram(diagram).replace("X", "")
  }

  return result;
}

(function main(){
  const encryptedMessage = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
  const keyword = "SUPERSPY"

  console.log(decryptMessage(encryptedMessage, keyword))
})()
