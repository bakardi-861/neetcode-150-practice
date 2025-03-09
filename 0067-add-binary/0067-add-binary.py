class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Bit-shifting
        # convert strings to binary, add, then convert back ([2:] chops off the "0b" portion)
        # a,b = int(a,2), int(b,2)
        # return bin(a + b)[2:] O(1) time, O(n) space

        # O(1) approach with "pen/paper addition like add strings"
        carry = 0
        res = []
        a,b = a[::-1],b[::-1]

        for i in range(max(len(a),len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            sum = digit_a + digit_b + carry
            
            res.append(str(sum % 2))
            carry = sum // 2
        
        if carry:
            res.append("1")
        return "".join(res[::-1])
