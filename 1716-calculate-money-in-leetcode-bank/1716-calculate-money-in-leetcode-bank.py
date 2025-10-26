class Solution:
    def totalMoney(self, n: int) -> int:
        k = n // 7
        F = 28 # first num in sequence (known sum of full week)
        L = 28 + (k - 1) * 7 # last num in sequence (known sum of full week + full weeks-1 * 7)
        arithmetic_sum = k * (F + L) // 2 # sum of full weeks
        
        monday = 1 + k # increment 1 by how many additional full weeks since first week always starts at 1
        final_week = 0

        # leftover days - this can also be an arithmetic sequence, but it is still O(1)
        for day in range(n % 7):
            final_week += monday + day
        
        return arithmetic_sum + final_week