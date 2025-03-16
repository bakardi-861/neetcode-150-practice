class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        i = 0

        while i < min(len(word1),len(word2)):
            merged.append(word1[i])
            merged.append(word2[i])
            i += 1

        while i < len(word1):
            merged.append(word1[i])
            i += 1
        while i < len(word2):
            merged.append(word2[i])
            i += 1
        return "".join(merged)