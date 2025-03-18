class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # mono stack - decreasing order
        stack = []
        ans = [0] * len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                pop = stack.pop()
                ans[pop] = i - pop
            stack.append(i)
        return ans            
