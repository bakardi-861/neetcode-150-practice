class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        #           0.    1.    2.   3.    4
        # words = ["aba","bcb","ece","aa","e"]
        #                                  w
        # # don't even need i and j, just do w[0], w[-1]
        # res = [2,3,0]
        # queries = [[0,2],[1,4],[1,1]]
        #                         i

        # res = [0] * len(queries)
        # vowels = "aeiou"
        # for i in range(len(queries)):
        #     q = queries[i]
        #     start = q[0]
        #     end = q[1]

        #     while start <= end:
                # if words[start][0] in vowels and words[start][-1] in vowels:
                #     res[i] += 1
        #         start += 1
        # return res

        vowels = "aeiou"
        n = len(words)

        # Step 1: Build prefix sum with one extra slot
        prefix = [0] * (n + 1)
        for i in range(n):
            w = words[i]
            prefix[i + 1] = prefix[i] + (1 if w[0] in vowels and w[-1] in vowels else 0)

        # Step 2: Answer queries
        res = []
        for l, r in queries:
            res.append(prefix[r + 1] - prefix[l])
        return res
            




