class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        l = 0
        #win = Counter(s[:k])
        max_vowels = 0
        win_sum = 0

        for r in range(len(s)):
            if s[r] in vowels:
                win_sum += 1
            while r-l+1 > k:
                if s[l] in vowels:
                    win_sum -= 1
                l += 1

            if r-l+1 == k:
                max_vowels = max(max_vowels,win_sum)
        return max_vowels