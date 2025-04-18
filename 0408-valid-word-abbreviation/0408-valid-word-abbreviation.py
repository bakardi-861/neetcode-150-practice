class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        while i < len(word) and j < len(abbr):
            # build the number
            if abbr[j].isnumeric():
                if abbr[j] == "0":# can't have leading 0s
                    return False
                
                number = ""
                while j < len(abbr) and abbr[j].isnumeric():
                    number += abbr[j]
                    j += 1
                i += int(number)

            else: # both are letters, so skip ahead if letters are the same
                if abbr[j] != word[i]: # letters are not the same
                    return False
                j += 1
                i += 1
        return i == len(word) and j == len(abbr)