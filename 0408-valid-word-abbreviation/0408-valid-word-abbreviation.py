class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Two pointers
        i, j = 0, 0
        while i < len(abbr) and j < len(word):
            if abbr[i].isdigit():
                if abbr[i] == "0":
                    return False
                number = ""
                while i < len(abbr) and abbr[i].isdigit():
                    number += abbr[i]
                    i += 1
                j += int(number)
            else:
                if j >= len(word) or word[j] != abbr[i]:
                    return False
                i += 1
                j += 1
        return i == len(abbr) and j == len(word)

    # Post Mortem
    # Didn't account for edge case where i could be OOB of abbr or j could be out of bounds of word if number in abbr is too large
    # With that, instead of returning True at the end I have to return whether i and j are at the end index of abbr and word respectively.
    # Final time: 25:19