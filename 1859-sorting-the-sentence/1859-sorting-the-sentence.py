class Solution:
    def sortSentence(self, s: str) -> str:
        # Time: O(n)
        # Space: O(n)
        # divide each word into into an array of strings
        # bucket sort bc number of letters is 1-9?
        # digit is always the last character of a word
        arr = s.split()

        # if not arr:
        #     return arr

        n = len(arr)
        buckets = ["" for _ in range(n)]

        # Step 1: Distribute elements into buckets
        for word in arr:
            digit = word[-1] # get digit at end of word
            buckets[int(digit)-1] = word[0:len(word)-1]
        return " ".join(buckets)
