class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        longest = 0

        # Left to right pass
        for c in s:
            if c == "(":
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, left + right)  # Valid substring length
            elif right > left:  # Too many closing brackets, reset the substring length
                left = right = 0  # Reset

        # Reset counters
        left = right = 0

        # Right to left pass
        for c in reversed(s):
            if c == ")":
                right += 1
            else:
                left += 1

            if left == right:
                longest = max(longest, right + left)
            elif left > right:  # Too many opening brackets
                left = right = 0  # Reset

        return longest
