class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        mono_de = mono_in = True
        st = []
        for n in nums:
            if st and n > st[-1]:
                mono_de = False
            if st and n < st[-1]:
                mono_in = False
            st.append(n)
        return mono_de or mono_in