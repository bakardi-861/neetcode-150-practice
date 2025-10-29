class Solution:
    def addMinimum(self, word: str) -> int:
        # valid string is abc
        # freq_index = Counter(word) => {a:[[0,1,2,3],1], b:[[1],1],c:[[2],1]}
        # {a:4,b:2,c:0}
        # a comes before bc, b goes btw ac, c goes after ab
        # bucket sort?/counting sort?

    #    "abc" "abccc"
    #        i     j
    #     ans = 2

        i = 0
        result = 0
        while i < len(word):
            if word[i:i+3] == "abc":
                i += 3  
            elif word[i:i+2] in ["ab","ac","bc"]:
                result += 1
                i += 2
            else:
                result += 2
                i += 1
        return result
