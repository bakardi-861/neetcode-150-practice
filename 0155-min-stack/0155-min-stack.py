class MinStack:

    def __init__(self):
        s = self
        s.stack = []
        s.min_stack = [] 
        # insert min element each time element pushed to normal stack, size == to normal stack

    def push(self, val: int) -> None:
        s = self
        min = val # set min to new val by default
        if s.stack:
            if val > s.min_stack[-1]: # if top of min_stack is smaller, 
                                      # set min to that so that it gets appended correctly
                min = s.min_stack[-1]
        s.stack.append(val)
        s.min_stack.append(min)

    def pop(self) -> None:
        s = self
        s.min_stack.pop()
        s.stack.pop()

    def top(self) -> int:
        s = self
        return s.stack[-1]

    def getMin(self) -> int:
        s = self
        return s.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()