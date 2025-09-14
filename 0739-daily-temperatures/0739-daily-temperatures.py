class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        ans = [0] * len(temperatures)
        hottest = 0

        for i in reversed(range(len(temperatures))):
            current_temp = temperatures[i]
            if current_temp >= hottest:
                hottest = current_temp
                continue
            
            days = 1
            while temperatures[i + days] <= current_temp:
                days += ans[i + days]
            ans[i] = days
        return ans
