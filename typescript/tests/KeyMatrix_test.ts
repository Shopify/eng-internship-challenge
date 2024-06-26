import Playfair from "../Playfair";

//Helpers
function IsKeyMatrixEqual(Actual: string[][], Expected: string[][]): boolean {
  if (Actual.length !== Expected.length) {
    return false;
  }

  for (let i = 0; i < Actual.length; i++) {
    if (Actual[i].length !== Expected[i].length) {
      return false;
    }

    for (let j = 0; j < Actual[i].length; j++) {
      if (Actual[i][j] !== Expected[i][j]) {
        return false;
      }
    }
  }

  return true;
}

function RunTest(KeyText: string, Expected: string[][]): void {
  const playFair = new Playfair(KeyText);
  const Actual = playFair.KeyMatrix;

  if (IsKeyMatrixEqual(Actual, Expected)) {
    console.log("Pass");
  } else {
    console.log("Fail");
  }
}

function ExpectError(KeyText: string): void {
  try {
    const playFair = new Playfair(KeyText);
    console.log("Fail");
  } catch (e) {
    console.log("Pass");
  }
}

//Unit tests to ensure that the key matrix is being produced correctly:
const expected_1_2 = [
  ["M", "O", "N", "A", "R"],
  ["C", "H", "Y", "B", "D"],
  ["E", "F", "G", "I", "K"],
  ["L", "P", "Q", "S", "T"],
  ["U", "V", "W", "X", "Z"],
];

const expected_4 = [
  ["A", "B", "C", "D", "E"],
  ["F", "G", "H", "I", "K"],
  ["L", "M", "N", "O", "P"],
  ["Q", "R", "S", "T", "U"],
  ["V", "W", "X", "Y", "Z"],
];

const expected_5 = [
  ["S", "U", "P", "E", "R"],
  ["Y", "A", "B", "C", "D"],
  ["F", "G", "H", "I", "K"],
  ["L", "M", "N", "O", "Q"],
  ["T", "V", "W", "X", "Z"],
];

const expected_6 = [
  ["P", "L", "A", "Y", "F"],
  ["I", "R", "E", "X", "M"],
  ["B", "C", "D", "G", "H"],
  ["K", "N", "O", "Q", "S"],
  ["T", "U", "V", "W", "Z"],
];

RunTest("monarchy", expected_1_2);
RunTest("mOnaRcHy", expected_1_2);
ExpectError("abcedefghiklmnopqrstuvwxyzabcdefgh");
RunTest("abcdefghij", expected_4);
RunTest("SuperspySuperspy", expected_5);
RunTest("playfair example", expected_6);
