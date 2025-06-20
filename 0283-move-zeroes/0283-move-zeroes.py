class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # for num in nums:
        #     if num==0:
        #         nums.remove(num)
        #         nums.append(num)
        # return nums

        size = len(nums)
        for i in range(size):
            if nums[i]==0:
                nums.append(nums[i])
                nums.remove(nums[i])
                size=len(nums)  
        return nums