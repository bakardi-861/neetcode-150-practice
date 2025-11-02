class Solution:
    def alternateDigitSum(self, n: int) -> int:
        # for each digit in n
            #if pos: 
                # add to sum
            #else: 
                #subtract from sum
        
        num = str(n)
        pos = True
        sum = 0
        i = 0
        while i < len(num):
            n = int(num[i])
            if pos:
                sum += n
                pos = False
            else:
                sum -= n
                pos = True
            i += 1
        return sum


