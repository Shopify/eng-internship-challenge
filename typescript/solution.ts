import Playfair from "./Playfair";

const cipherText = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV";
const keyText = "SUPERSPY";

const playFairCipher = new Playfair(keyText);

console.log(playFairCipher.DecryptPlayFair(cipherText));
