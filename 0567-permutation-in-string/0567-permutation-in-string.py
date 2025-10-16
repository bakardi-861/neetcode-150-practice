from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        win = Counter()
        matches = 0
        l = 0
        
        for r in range(len(s2)):
            char = s2[r]
            if char in s1_count:
                win[char] += 1
                if win[char] == s1_count[char]:
                    matches += 1
                elif win[char] == s1_count[char] + 1:
                    matches -= 1
            
            # shrink window if size exceeds s1 length
            if r - l + 1 > len(s1):
                left_char = s2[l]
                if left_char in s1_count:
                    if win[left_char] == s1_count[left_char]:
                        matches -= 1
                    elif win[left_char] == s1_count[left_char] + 1:
                        matches += 1
                    win[left_char] -= 1
                l += 1
            
            # check if all characters match
            if matches == len(s1_count):
                return True
        
        return False
