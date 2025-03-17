class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(","}":"{","]":"["}
        for i,c in enumerate(s):
            if c in "]})":
                if stack and brackets[c] == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
            stack.append(c)
        return len(stack) == 0