class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        digit_sum=sum(nums)
        element_sum = 0

        result = ''.join(str(num) for num in nums)
        for i in range(len(result)):
            element_sum += int(result[i])
        
        return digit_sum - element_sum

                 

        