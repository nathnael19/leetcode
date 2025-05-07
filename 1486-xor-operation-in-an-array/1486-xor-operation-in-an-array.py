class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        for i in range(n):
            nums.append(start + 2*i)
        result = nums[0]
        for num in nums[1:]:
            result ^= num
        return result
        
 

