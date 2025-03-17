class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0

        while i < min(len(word1),len(word2)):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1
        
        ans = "".join(merged)

        if i < len(word1):
            ans += word1[i:len(word1)]
        elif i < len(word2):
            ans += word2[i:len(word2)]

        return ans