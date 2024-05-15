# NOTE: For this solution, we assume that J is not used to fit the alphabet in a 5x5 table

class Solution:

    def generate_table(self, key: str):
        # We store the table as a dictionary of positions, given as follows:
        # [0  1  2  3  4 ]
        # [5  6  7  8  9 ]
        # [10 11 12 13 14]
        # [15 16 17 18 19]
        # [20 21 22 23 24]
        # We also store the inverse_table to be able to retrieve letters from positions

        table = {}  # letter: position
        inverse_table = {}  # position: letter

        # Remove duplicates from our message string by converting to a dictionary then back to a list
        message_unique = list(dict.fromkeys(key))

        # Get the remaining unused letters
        all_letters = [chr(ascii) for ascii in range(65, 91) if ascii != 74]
        remaining_letters = [c for c in all_letters if c not in message_unique]

        # Loop through each and assign it to its location in our table
        ordered_letters = message_unique + remaining_letters
        for i, letter in enumerate(ordered_letters):
            table[letter] = i
            inverse_table[i] = letter

        return table, inverse_table
    

    def decrypt(self, message: str, key: str):
        # Get our table from the above function
        table, inverse_table = self.generate_table(key)

        # If our message has odd length, append a "X"
        # if len(message) % 2 != 0:
        #     message += "X"

        # Split the input message into groups of two, and replace duplicate letters with "X"
        pairs = [message[i:i+2] for i in range(0, len(message), 2)]

        # Iterate over each pair and append the result to password
        password = ""

        for i, pair in enumerate(pairs):
            letter1, letter2 = pair[0], pair[1]
            pos1, r1, c1 = table[letter1], table[letter1] // 5, table[letter1] % 5
            pos2, r2, c2 = table[letter2], table[letter2] // 5, table[letter2] % 5

            # Apply the rules from Wikipedia, but inversed because we're decrypting not encrypting
            # RULE 1: We will drop extra instances of the chosen insert letter ('X') at the end

            # RULE 2: If letters appear on the same row, replace them with letter to their immediate left
            if r1 == r2:
                password += inverse_table[pos1 - 1] if c1 != 0 else inverse_table[pos1 + 4]
                password += inverse_table[pos2 - 1] if c2 != 0 else inverse_table[pos2 + 4]

            # RULE 3: If letters appear on the same column, replace them with letter immediately above
            elif c1 == c2:
                password += inverse_table[pos1 - 5] if r1 != 0 else inverse_table[pos1 + 20]
                password += inverse_table[pos2 - 5] if r2 != 0 else inverse_table[pos2 + 20]

            # # RULE 4: If letters not on same row or column, replace them with opposite corner pairs
            else:
                password += inverse_table[r1 * 5 + c2]
                password += inverse_table[r2 * 5 + c1]

        return password.replace('X', '')



solution = Solution()
print(solution.decrypt("IKEWENENXLNQLPZSLERUMRHEERYBOFNEINCHCV", "SUPERSPY"))