class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(1,len(arr)):
            if arr[i-1]%2!=0 and arr[i]%2!=0:
                count +=1
            else:
                count = 0
            if count==2:
                return True
        return False
                    