class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
        # naive: O(n*m) solution is to search every word inclusive in every 
        # query and check if each word starts and ends with a vowel

        # how can we do this faster? Can we work with the ranges by merging them?
        # no, because we need to return individual answers for each query so merging the queries like [0,4] wouldn't work.

        # I think this is an example of prefix sums, where we can precompute the number of strings at each arr[i] that have vowels at the start and end. 
        # This prevents us from having to rescan the array multiple times for each query.

        # words = [  "aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
        # prefix = [0, 1,   1,    2,    3,   4]
        # i think we need to add a 0 at the start so that the math works out, since the first position in the array is always the sum + 0.
        # when we scan the queries, we just look at query[1]+1 index (ignoring prefix).
        # [0,2] = 2
        # [1,4] = 4
        # [1,1] = 1
        # that approach is incorrect for the last 2. we need to be subtracting 1 somewhere I think?
        # THE PROBLEM IS THAT I NEED TO DO PREFIX[R+1] - PREFIX[L], not summing them up. This is because I want to include all the strings from prefix[l] to prefix[r].
        # I still don't fully understand why this works. I know the +1 is because of the extra 0 we added at the start to get the true index. 
        # THIS PART: The prefix sum at index i represents the count of valid strings up to but not including index i in the original array.
        # [0,2] = 3-1 = 2
        # [1,4] = 4-1 = 3
        # [1,1] = 1-1 = 0
        #. res = [2,3,0]
        # Definitely need to do more prefix sum problems

        # prefix sum remember: precomputing values/sums of everything before and not including the current prefix[i]

        vowels = "aeiou"
        prefix = [0]
        for i,w in enumerate(words):
            if w[0] in vowels and w[-1] in vowels:
                prefix.append(prefix[i] + 1)
            else:
                prefix.append(prefix[i])
        
        res = []
        for q in queries:
            # start = q[0]
            # end = q[1]
            res.append(prefix[q[1]+1] - prefix[q[0]])
        return res


