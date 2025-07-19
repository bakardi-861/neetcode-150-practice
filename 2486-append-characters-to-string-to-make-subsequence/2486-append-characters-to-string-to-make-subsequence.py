class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # s = "coaching", t = "coding"
        #             i
        #                       j
        # res = t[j:]

        i = 0
        for c in s:        
            if i < len(t) and c == t[i]:
                i += 1
        return len(t) - i