class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        # i is beautiful if word from s[i..end] = a 
            # and s[i_start...i_end] == a
            # and s[j_start...j_end] == b 
            # and abs(i-j) <= k
        
        # get both a and b indices in s
        a_indices = []
        for i in range(len(s) - len(a) + 1):
            if s[i:i+len(a)] == a:
                a_indices.append(i)

        b_indices = []
        for j in range(len(s) - len(b) + 1):
            if s[j:j+len(b)] == b:
                b_indices.append(j)

        j = 0
        res = []
        for i in a_indices:
            while j < len(b_indices) and b_indices[j] < i - k:
                j += 1
            if j < len(b_indices) and abs(b_indices[j] - i) <= k:
                res.append(i)
        return res
