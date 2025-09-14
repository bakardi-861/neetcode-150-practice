class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hash table: track sequence starts, if num-1 not in set
        # union find: connected component = consecutive sequence (num + 0 or num + 1 or num - 1)
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while num + length in num_set:
                    length += 1
                max_len = max(max_len, length)
        return max_len