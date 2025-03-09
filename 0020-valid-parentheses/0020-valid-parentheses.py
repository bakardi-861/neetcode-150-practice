class Solution:
    def isValid(self, s: str) -> bool:
        # 1. open and closed types must match
        # 2. open and closed must be closed in order
        # 3. every closed has an open bracket of the same type

        map = {")":"(", "}":"{","]":"["}
        # s = "(([])){}))"
        # c = ")"
        stack = []

        for c in s:
            if stack and c in map: # c is closed and stack has something on it
                if stack[-1] != map[c]: # if type of brackets DO NOT match
                    return False
                stack.pop()
                continue # continue to next iteration
            stack.append(c) # append when open
        return len(stack) == 0
