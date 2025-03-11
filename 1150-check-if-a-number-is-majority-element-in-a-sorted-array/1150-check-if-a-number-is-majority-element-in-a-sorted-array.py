class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # bc array is sorted and we are checking if an element is in the array, we can use binary search
        # binary search to find the lower bound: first instance of target
        def lower_bound():
            l,r = 0,len(nums)-1
            while l < r:
                mid = (r+l) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            return l

        # goal_index is the lower_bound() index + len(nums) // 2 to get the instance of target that appears more than len(nums) // 2 times.
        goal_index = lower_bound() + len(nums) // 2
        # if the index is within nums and the num at that index is target, then it's the majority element
        return goal_index < len(nums) and nums[goal_index] == target
