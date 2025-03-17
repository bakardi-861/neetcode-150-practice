class Solution:
    def calPoints(self, operations: List[str]) -> int:
        # ops = ["5","2","C","D","+"]
        # num: push to stack
        # +: add prev 2 scores and push that sum to stack
        # C: pop top of stack
        # D: double top of stack and push that to stack
        # return sum of stack

        stack = []
        for c in operations:
            if c == "C":
                stack.pop()
            elif c == "D":
                stack.append(int(stack[-1]) * 2)
            elif c == "+":
                stack.append(int(stack[-1]) + int(stack[-2]))
            else:
                stack.append(int(c))
        return sum(stack)