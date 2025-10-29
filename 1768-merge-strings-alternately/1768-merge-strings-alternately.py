class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 1 = "ab" 2 = "pqrs"
        #      i       j
        # merged = "".join([apqrs])

        ans = []
        i,j = 0,0
        while i < len(word1) and j < len(word2):
            ans.append(word1[i])
            i += 1
            ans.append(word2[j])
            j += 1
        
        if i < len(word1):
            ans.append(word1[i:]) # or extend

        if j < len(word2):
            ans.append(word2[j:]) # or extend
        return "".join(ans)