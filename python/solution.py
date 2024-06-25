class PlayfairCipher:
    """A class for the Playfair cipher for encryption or decryption initialized with a given key"""

    def __init__(self, key: str) -> None:
        self.key = key
        self.key_table = self._generate_key_table(key)
        self.ch_to_coord = self._generate_key_mapping()

    def _generate_key_table(self, key: str) -> list[list[str]]:
        """Create the key table for encryption/decryption from the key given
        **Assumption that 'J' is not in the table since 'Q' appears in ciphertext
        Returns 5 x 5 array of letters - raises error if the key table does not contain exactly 25 characters
        """
        used_chars = set()
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key_table = []

        for ch in key + alphabet:
            if ch in used_chars:
                continue
            key_table.append(ch)
            used_chars.add(ch)

        assert (
            len(key_table) == 25
        ), f"Key table should contain 25 chars, currently has {len(key_table)}"
        return [key_table[idx * 5 : (idx + 1) * 5] for idx in range(5)]

    def _generate_key_mapping(self) -> dict[str, tuple[int, int]]:
        """Creates and returns a dictionary to map letters to their (row,col) coordinates in key_table"""
        return {self.key_table[i][j]: (i, j) for i in range(5) for j in range(5)}

    def bigram_coding(
        self, ch_a: str, ch_b: str, decrypt: bool = True
    ) -> tuple[str, str]:
        """
        Takes in bigram, and a mode (default decryption, otherwise encryption) and returns the coded bigram
        Checks the character coordinates in self.key_table for same row/column/formation of box
        Returns the two encrypted/decrypted letters
        """
        # set direction of new character based on encryption/decryption
        direction = -1 if decrypt else 1

        row_a, col_a = self.ch_to_coord[ch_a]
        row_b, col_b = self.ch_to_coord[ch_b]

        if row_a == row_b:
            coded_a = self.key_table[row_a][(col_a + direction) % 5]
            coded_b = self.key_table[row_b][(col_b + direction) % 5]
        elif col_a == col_b:
            coded_a = self.key_table[(row_a + direction) % 5][col_a]
            coded_b = self.key_table[(row_b + direction) % 5][col_b]
        # if characters form a rectangle
        else:
            coded_a = self.key_table[row_a][col_b]
            coded_b = self.key_table[row_b][col_a]
        return coded_a, coded_b

    def decrypt_ct(self, ct: str) -> str:
        """
        Decrypt ciphertext bigrams using bigram coding helper function
        Returns decrypted plaintext string
        """
        pt = []
        ct_len = len(ct)
        for idx in range(0, ct_len, 2):
            ch_a, ch_b = ct[idx], ct[idx + 1] if idx + 1 < ct_len else "X"
            a, b = self.bigram_coding(ch_a, ch_b, decrypt=True)
            pt.append(a)
            if b != "X":
                pt.append(b)
        return "".join(pt)

    def encrypt_pt(self, pt: str) -> str:
        """
        Generate bigrams (ensure double or standalone letters get padded)
        Encrypt bigrams according to key_table and Playfair rules
        Return encrypted ciphertext string
        """
        bigrams = []
        idx = 0
        pt_len = len(pt)
        while idx < pt_len:
            if idx + 1 == pt_len or pt[idx + 1] == pt[idx]:
                bigrams.append(pt[idx] + "X")
                idx += 1
            else:
                bigrams.append(pt[idx : idx + 2])
                idx += 2
        ct = []
        for ch_a, ch_b in bigrams:
            a, b = self.bigram_coding(ch_a, ch_b, decrypt=False)
            ct.append(a + b)
        return "".join(ct)


key = "SUPERSPY"
cipher = PlayfairCipher(key)
ciphertext = "IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV"
plaintext = cipher.decrypt_ct(ciphertext)
print(plaintext)
