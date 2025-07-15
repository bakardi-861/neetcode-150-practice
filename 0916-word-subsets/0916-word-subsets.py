class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # b is a subset of  a if every letter in b occurs in a including multiplicity.
        # "wrr" is a subset of "warrior" but is not a subset of "world".
        # A string a from words1 is universal if for every string b in words2, b is a subset of a.

        # words1 = ["amazon","apple","facebook","google","leetcode"]
        # words2 = ["lc","eo"]
        # universal_map = {l:1,c:1,e:1,o:1}
        # universal = [leetcode]


        # Time O(n * 26 * k)
        # Space: O(n)
        # store in universal_map: count each character from each word in word2
        # a universal word must match the frequency of universal_map
        # for each word in words1:
            # generate a new frequency map
            # if frequency map matches universal_map:
                # universal_words.append(word1[i])
        # return universal_words

        def count(word):
            return Counter(word)

        universal_map = Counter()
        for word in words2:
            freq = count(word)
            for c in freq:
                universal_map[c] = max(universal_map[c], freq[c])

        universal_words = []
        for word in words1:
            freq = count(word)
            if all(freq[c] >= universal_map[c] for c in universal_map):
                universal_words.append(word)
        return universal_words

        

