class Solution:
    def isValid(self, s: str) -> bool:
        map = {')':'(', ']':'[', '}':'{'}
        stack = []

        for c in s:
            if c in map: # c is closed
                if stack:
                    if map[c] == stack[-1]:
                        stack.pop()
                        continue
            stack.append(c)
        return len(stack) == 0
            

