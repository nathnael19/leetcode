class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                nums[i-1]*=2
                nums[i]=0
            
        for num in nums:
            if num==0:
                nums.remove(num)
                nums.append(num)
        return nums