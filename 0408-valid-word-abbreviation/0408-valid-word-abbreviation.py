class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # substitution    abbr: s10n
        #            i             j
        # internationalization
        #              i
        i = j = 0
        while i < len(word) and j < len(abbr):
            # build the number
            if abbr[j].isnumeric():
                if abbr[j] == "0":
                    return False
                number = ""
                while j < len(abbr) and abbr[j].isnumeric(): # can't have leading 0s
                    number += abbr[j]
                    j += 1
                i += int(number)
                
                # # get each digit of the number string and 
                # num = 0
                # for n in reversed(number):
                #     num += (int(n) % 10)

            else: # both are letters, so skip ahead
                if abbr[j] != word[i]: # letters are not the same
                    return False
                j += 1
                i += 1
        return i == len(word) and j == len(abbr)


         # skip letters in the abbreviation/word
         # when abbr[j] is a number, loop through it to build the number from the characters until we reach another letter.
         # after building the number, move i ahead that many characters. i should be on the same letter j is at.
         # if abbreviation is valid, i == len(word) and j == len(abbr) once algo exits, else it is not valid.