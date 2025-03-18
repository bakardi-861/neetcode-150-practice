class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # RPN = PEMDAS??
        # round decimals down
        stack = []
        for t in tokens:
            if t in "+/*-":
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    math = num1 + num2
                elif t == "-":
                    math = num1 - num2
                elif t == "*":
                    math = num1 * num2
                elif t == "/":
                    math = int(num1 / num2) # int() truncates towards 0
                stack.append(math)
            else:
                stack.append(int(t))
        return stack[0]
