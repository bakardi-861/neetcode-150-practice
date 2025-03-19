class Solution:
    def makeGood(self, s: str) -> str:
        # good string does NOT have 2 adjacent characters where: 
        # 1) 0 <= i <= s.length - 2 
        # 2) s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
        stack = []
        # check if curr and prev are the same letter in different cases.
        for c in s:
            if stack and (c.lower() == stack[-1].lower() and c != stack[-1]):
                # do this to remove prev from stack and skip adding curr bc we want to remove both
                stack.pop()
                continue
            stack.append(c)
        return "".join(stack)