class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[2]+nums[1]>nums[0]:
            result = Counter(nums)
            if len(result)==1:
                return "equilateral"
            elif len(result)==2:
                return "isosceles"
            else:
                return "scalene"
        else:
            return "none"
        