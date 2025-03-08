class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_list = []
        while k > 0:
            k_list.append(k % 10)
            k //=10

        num = num[::-1]
        carry = 0
        res = []

        # num =    [0,0,2,1]
        # k_list = [4,3]0 0
        # res = [4,3,2,1]
        # carry = 0

        for i in range(max(len(k_list),len(num))):
            d1 = num[i] if i < len(num) else 0
            d2 = k_list[i] if i < len(k_list) else 0
            sum = d1 + d2 + carry

            res.append(sum % 10)
            carry = sum // 10

        if carry:
            res.append(carry)
        return res[::-1]

