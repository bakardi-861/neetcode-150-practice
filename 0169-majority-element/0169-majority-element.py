class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # naive: use hashmap to count how many times each element has appeared and then iterate through it to find the one that appears more than n/2 times.
        # O(n) time and O(n) space in the worst case
        # To get O(1) space, I have to use an integer counter variable and not use a hashmap
        # The problem is when I see a different element, how can I keep track of the counts without storing them in something. Example, I count two 2s and then the next number is a 1, the count will get reset.

        # I know that Boyer voting algorithm is an option, but I just know the name and not how to implement it unfortunately. In lieu of that, I can use a variable majority to track the element with the highest frequency we have seen so far, maybe as a tuple with (num,count). 
        # [2,2,1,1,1,2,2]
        #              i
        # majority = (2,4)
        # res = 2

        # naive
        # map = Counter(nums)
        # n = len(nums)
        # for key,val in map.items():
        #     if val >= (n/2):
        #         return key

        # Sorting O(nlogn) time, O(1) space if not counting .sort()
        n = len(nums)
        nums.sort()
        count = 1
        majority = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
                if count >= (n/2):
                    majority = nums[i]
            else:
                count = 1
        return majority
        
        # Majority Vote Algo
        