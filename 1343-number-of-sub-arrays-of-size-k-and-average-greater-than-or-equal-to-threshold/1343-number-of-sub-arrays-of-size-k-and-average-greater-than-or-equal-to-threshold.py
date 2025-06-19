class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #  0   1. 2. 3. 4 5  6 7 8 9
        # [11,13,17,23,29,31,7,5,2,3]
        #  l
        #  r
        #            k
        # k = 3, threshold = 5

        ans = 0
        win_sum = sum(arr[:k])
        if win_sum >= threshold * k:
            ans += 1

        for i in range(k, len(arr)):
            win_sum += arr[i] - arr[i - k]
            if win_sum >= threshold * k:
                ans += 1
        return ans