
//we have a key, using that key we are going to build a cypher to encrypt the message.

//method for creating the cypher

function createCypher(StringKey){
    const cypher=[];
    let key=new Set();

    //add the key elements to a set
    for(let c of StringKey){
        key.add(c);
    }
    //adds the other characters into the set as well
    for(let i=0;i<26;i++){
        let c=String.fromCharCode(i+65);
        if(key.has(c)==false && c!="J"){
            key.add(c);
        }
    }

    let row=[]
    for(let c of key){
        //keeps adding the characters ot a row and then when row is of length 5,adds it to the cypher;
        if(row.length==5){
            cypher.push(row);
            row=[];
        }
        row.push(c);
    }
    cypher.push(row);
    return cypher;
}

function decryptMessage(msg,grid){
    //we get the message, if its odd add X
    if (msg.length % 2 != 0) {
        msg += "X"
    }

    //decoding the message
    let decodedMessage = "";
    for (let i = 0; i < msg.length; i += 2) {
        let pair = msg.substr(i, 2);
        let decodedPair = decodePairs(pair[0], pair[1], grid);
        decodedMessage += decodedPair;
    }
    //removing all X's from the result
    return decodedMessage.replace(/X/g, '');;
    
}

function decodePairs(ch1, ch2, grid) {
    let pair1=getPosition(ch1,grid);
    let pair2=getPosition(ch2,grid);

    let p1row=pair1[0], p1col=pair1[1], p2row=pair2[0], p2col=pair2[1];

    let decodedPair = "";

    if (p1row === p2row) {
        decodedPair += grid[p1row][(p1col - 1 + 5) % 5];
        decodedPair += grid[p2row][(p2col - 1 + 5) % 5];
    } else if (p1col === p2col) { 
        decodedPair += grid[(p1row - 1 + 5) % 5][p1col];
        decodedPair += grid[(p2row - 1 + 5) % 5][p2col];
    } else {
        decodedPair += grid[p1row][p2col];
        decodedPair += grid[p2row][p1col];
    }

    return decodedPair;

}

function getPosition(letter,cypher){
    //returns the x,y co-ordinates of the letter
    let pos=[]
    for(let r=0;r<cypher.length;r++){
        for(let c=0;c<cypher.length;c++){
            if(cypher[r][c]==letter){
                pos.push(r);
                pos.push(c);
                return pos;
            }
        }
    }
}

const cypher=createCypher("SUPERSPY");

const ans=decryptMessage("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV",cypher);

console.log(ans);

