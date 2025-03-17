class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1),len(word2))
        s = ""
        for i in range(n):
            s += word1[i] + word2[i]
        return s + word1[n:] + word2[n:]