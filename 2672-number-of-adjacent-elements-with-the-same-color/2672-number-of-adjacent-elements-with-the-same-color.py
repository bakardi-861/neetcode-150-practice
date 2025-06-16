class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        colors = [0] * n
        total = 0
        
        for index, new_color in queries:
            # Before update: decrement total if matching pairs break
            if index > 0 and colors[index] != 0 and colors[index] == colors[index - 1]:
                total -= 1
            if index < n - 1 and colors[index] != 0 and colors[index] == colors[index + 1]:
                total -= 1
            
            # Update color
            colors[index] = new_color
            
            # After update: increment total if new matching pairs formed
            if index > 0 and colors[index] == colors[index - 1]:
                total += 1
            if index < n - 1 and colors[index] == colors[index + 1]:
                total += 1
            
            ans.append(total)
        
        return ans
