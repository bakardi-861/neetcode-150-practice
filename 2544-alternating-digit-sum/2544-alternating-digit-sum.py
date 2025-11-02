class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sign = 1      # Start with + for the last digit
        total = 0

        while n > 0:
            digit = n % 10
            total += digit * sign
            sign *= -1
            n //= 10

        # If number of digits was even, flip sign
        return -total if sign == 1 else total