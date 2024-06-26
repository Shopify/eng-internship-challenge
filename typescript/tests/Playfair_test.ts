import Playfair from "../Playfair";

//Helpers
function RunTest(KeyText: string, CipherText: string, Expected: string): void {
  const playFair = new Playfair(KeyText);
  const Actual = playFair.DecryptPlayFair(CipherText);

  if (Actual === Expected) {
    console.log("Pass");
  } else {
    console.log("Fail");
  }
}

function ExpectError(KeyText: string, CipherText: string): void {
  try {
    const playFair = new Playfair(KeyText);
    playFair.DecryptPlayFair(CipherText);
    console.log("Fail");
  } catch (e) {
    console.log("Pass");
  }
}

//Unit tests to ensure that the key matrix is being produced correctly:
const KeyText1 = "playfair example";
const CipherText1 = "BMODZBXDNABEKUDMUIXMMOUVIF";
const Expected1 = "HIDETHEGOLDINTHETREESTUMP";

const KeyText2 = "playfair example";
const CipherText2 = "ZSKAMPPWMOPBQCNZBPXM";
const Expected2 = "SHOPIFYTESTINGSUITE";

const KeyText3 = "playfair example";
const CipherText3 = "ZSKAM1PPW MOPBQCNZB123PXM"; //check for non alphabet characters

const KeyText4 = "playfair example";
const CipherText4 = "ZSKAMPPWMOPBQCNZBPX"; //check for odd length cipher text

const KeyText5 = "playfair example";
const CipherText5 = "BMODZBXDNABEKUDMUIXMMOUVIF".toLowerCase(); //lower case key text
const Expected5 = "HIDETHEGOLDINTHETREESTUMP";

//NOTE: a correct outpout also correct tests the required post-conditions as well as the function required to generate
//the hashmap for the key matrix
RunTest(KeyText1, CipherText1, Expected1);
RunTest(KeyText2, CipherText2, Expected2);
ExpectError(KeyText3, CipherText3);
ExpectError(KeyText4, CipherText4);
RunTest(KeyText5, CipherText5, Expected5);
