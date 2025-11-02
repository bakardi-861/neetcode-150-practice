class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_de = mono_in = True
        last = None
        # st = []
        for n in nums:
            if last is not None and n > last:
                mono_de = False
            if last is not None and n < last:
                mono_in = False
            last = n
            # st.append(n)
        return mono_de or mono_in