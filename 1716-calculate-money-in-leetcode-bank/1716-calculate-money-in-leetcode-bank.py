class Solution:
    def totalMoney(self, n):
        total = 0
        complete_week = n // 7
        remaining_days = n % 7

        # total hamming distance
        total += (28 * complete_week) + (7 * (complete_week - 1) * complete_week // 2) #total for complete weeks

        total += (complete_week + 1 + complete_week + remaining_days) * remaining_days // 2 #total for remaining days

        return total

        # can also simulate with a while loop/for loop in O(n) time