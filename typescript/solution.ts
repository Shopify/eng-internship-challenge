const encryptedMessage = 'IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV';
const key = 'SUPERSPY';

class PlayfairCipher {
	private readonly keyTableSize = 5;
	private playfair: string[][] = Array(this.keyTableSize)
		.fill(0)
		.map(() => Array(this.keyTableSize).fill(''));

	constructor(key: string) {
		key = key.trim().toUpperCase();
		// want unique letters
		const keySet = new Set<string>(key.split(''));
		// omit J
		const alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'.split('');
		alphabet.forEach((letter) => keySet.add(letter));

		const keyArr = Array.from(keySet);
		let keyIndex = 0;
		// populate the key table from left to right, top to bottom
		this.playfair.forEach((row, rowIndex) => {
			row.forEach((_, colIndex) => {
				this.playfair[rowIndex][colIndex] = keyArr[keyIndex];
				keyIndex++;
			});
		});
	}

	/**
	 * Check if two letters are in the same row in the key table
	 */
	private areLettersInSameRow(letter1: string, letter2: string): boolean {
		const row1 = this.playfair.findIndex((row) => row.includes(letter1));
		const row2 = this.playfair.findIndex((row) => row.includes(letter2));
		return row1 === row2 && row1 !== -1;
	}

	/**
	 * Check if two letters are in the same column in the key table
	 */
	private areLettersInSameColumn(letter1: string, letter2: string): boolean {
		let col1 = -1;
		let col2 = -1;
		this.playfair.forEach((row, rowIndex) => {
			row.forEach((letter, colIndex) => {
				if (letter === letter1) {
					col1 = colIndex;
				} else if (letter === letter2) {
					col2 = colIndex;
				}
			});
		});
		return col1 === col2 && col1 !== -1;
	}

	/**
	 * Get the position of a letter in the key table
	 */
	private findPosition(letter: string): { row: number; col: number } {
		let rowResult = -1;
		let colResult = -1;
		this.playfair.forEach((row, rowIndex) => {
			row.forEach((key, colIndex) => {
				if (key === letter) {
					rowResult = rowIndex;
					colResult = colIndex;
				}
			});
		});
		return { row: rowResult, col: colResult };
	}

	/**
	 * Shift each letter to the right
	 */
	private shiftRight(
		firstLetter: string,
		secondLetter: string
	): [string, string] {
		const getShiftIndex = (index: number): number => {
			if (index === this.keyTableSize - 1) {
				return 0;
			}
			return index + 1;
		};

		const { row: firstLetterRow, col: firstLetterCol } =
			this.findPosition(firstLetter);
		const { row: secondLetterRow, col: secondLetterCol } =
			this.findPosition(secondLetter);

		const shiftedFirstLetter =
			this.playfair[firstLetterRow][getShiftIndex(firstLetterCol)];
		const shiftedSecondLetter =
			this.playfair[secondLetterRow][getShiftIndex(secondLetterCol)];
		return [shiftedFirstLetter, shiftedSecondLetter];
	}

	/**
	 * Shift each letter to the left
	 */
	private shiftLeft(
		firstLetter: string,
		secondLetter: string
	): [string, string] {
		const getShiftIndex = (index: number): number => {
			if (index === 0) {
				return this.keyTableSize - 1;
			}
			return index - 1;
		};

		const { row: firstLetterRow, col: firstLetterCol } =
			this.findPosition(firstLetter);
		const { row: secondLetterRow, col: secondLetterCol } =
			this.findPosition(secondLetter);

		const shiftedFirstLetter =
			this.playfair[firstLetterRow][getShiftIndex(firstLetterCol)];
		const shiftedSecondLetter =
			this.playfair[secondLetterRow][getShiftIndex(secondLetterCol)];
		return [shiftedFirstLetter, shiftedSecondLetter];
	}

	/**
	 * Shift each letter down
	 */
	private shiftDown(
		firstLetter: string,
		secondLetter: string
	): [string, string] {
		const getShiftIndex = (index: number): number => {
			if (index === this.keyTableSize - 1) {
				return 0;
			}
			return index + 1;
		};

		const { row: firstLetterRow, col: firstLetterCol } =
			this.findPosition(firstLetter);
		const { row: secondLetterRow, col: secondLetterCol } =
			this.findPosition(secondLetter);

		const shiftedFirstLetter =
			this.playfair[getShiftIndex(firstLetterRow)][firstLetterCol];
		const shiftedSecondLetter =
			this.playfair[getShiftIndex(secondLetterRow)][secondLetterCol];
		return [shiftedFirstLetter, shiftedSecondLetter];
	}

	/**
	 * Shift each letter up
	 */
	private shiftUp(firstLetter: string, secondLetter: string): [string, string] {
		const getShiftIndex = (index: number): number => {
			if (index === 0) {
				return this.keyTableSize - 1;
			}
			return index - 1;
		};

		const { row: firstLetterRow, col: firstLetterCol } =
			this.findPosition(firstLetter);
		const { row: secondLetterRow, col: secondLetterCol } =
			this.findPosition(secondLetter);

		const shiftedFirstLetter =
			this.playfair[getShiftIndex(firstLetterRow)][firstLetterCol];
		const shiftedSecondLetter =
			this.playfair[getShiftIndex(secondLetterRow)][secondLetterCol];
		return [shiftedFirstLetter, shiftedSecondLetter];
	}

	/**
	 * Swap the corners of the rectangle formed by the two letters
	 */
	private swapCorners(
		firstLetter: string,
		secondLetter: string
	): [string, string] {
		const { row: firstLetterRow, col: firstLetterCol } =
			this.findPosition(firstLetter);
		const { row: secondLetterRow, col: secondLetterCol } =
			this.findPosition(secondLetter);

		const swappedFirstLetter = this.playfair[firstLetterRow][secondLetterCol];
		const swappedSecondLetter = this.playfair[secondLetterRow][firstLetterCol];
		return [swappedFirstLetter, swappedSecondLetter];
	}

	getKeyTable(): string[][] {
		return this.playfair;
	}

	encrypt(message: string): string {
		const res: string[] = [];
		message = message.trim().toUpperCase();
		const messageArr = message
			.split('')
			.filter((letter) => letter.match(/[A-Z]/));
		const len = messageArr.length;

		let index = 0;
		while (index < len) {
			const firstLetter = messageArr[index];
			let secondLetter = 'X';
			if (index < len - 1 && messageArr[index] !== messageArr[index + 1]) {
				// if there's a valid second letter then use that instead
				secondLetter = messageArr[++index];
			}

			if (this.areLettersInSameRow(firstLetter, secondLetter)) {
				res.push(...this.shiftRight(firstLetter, secondLetter));
			} else if (this.areLettersInSameColumn(firstLetter, secondLetter)) {
				res.push(...this.shiftDown(firstLetter, secondLetter));
			} else {
				res.push(...this.swapCorners(firstLetter, secondLetter));
			}
			index++;
		}
		return res.join('');
	}

	decrypt(message: string): string {
		const res: string[] = [];
		message = message.trim().toUpperCase();
		const messageArr = message
			.split('')
			.filter((letter) => letter.match(/[A-Z]/));
		const len = messageArr.length;

		let index = 0;
		while (index < len) {
			const firstLetter = messageArr[index];
			const secondLetter = messageArr[++index];

			if (this.areLettersInSameRow(firstLetter, secondLetter)) {
				res.push(...this.shiftLeft(firstLetter, secondLetter));
			} else if (this.areLettersInSameColumn(firstLetter, secondLetter)) {
				res.push(...this.shiftUp(firstLetter, secondLetter));
			} else {
				res.push(...this.swapCorners(firstLetter, secondLetter));
			}
			index++;
		}
		// filter out 'X', spaces, and special characters
		return res
			.filter((letter) => {
				return letter !== 'X' && letter !== ' ' && letter.match(/[A-Z]/);
			})
			.join('');
	}
}

const playfair = new PlayfairCipher(key);
console.log(playfair.decrypt(encryptedMessage));
// console.log(playfair.encrypt('HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA'));
