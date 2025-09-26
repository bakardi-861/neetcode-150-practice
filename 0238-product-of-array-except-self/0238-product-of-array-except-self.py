class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #         0 1 2 3
        # nums = [1,2,3,4]
        # ans =  [24,12,8,6]
        # Output: [24,12,8,6]
        #           0 1 2 3
        # # nums = [1,2,3,4]
        #             i
        #             l
        #               r
        # # prefix products = [1,1,2,6,24]
        #                          i
        #                          l
        #                              r  
            # ans equation = prefix[l]
            # ans = []
        # 

        
        # nums [1,2,3,4]
        #         i
        # pre [1,1,2,6,24]
        #          i
        # # suffix [24,24,12,4,1]
        #              i

        # prefix = [1] * (len(nums)+1)
        # for i in range(len(nums)):
        #     prefix[i+1] = prefix[i] * nums[i]
        
        # suffix = [1] * (len(nums)+1)
        # for i in reversed(range(len(nums))):
        #     suffix[i] = suffix[i+1] * nums[i]

        # ans = []
        # for i in range(len(nums)):
        #    answer.append(suffix[i] * prefix[i])

        # return ans


        ans = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in reversed(range(len(nums))):
            ans[i] *= suffix
            suffix *= nums[i]
        return ans


        
