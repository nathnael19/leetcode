class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        b = str(n)
        summ =0
        p = 1
        for i in range(len(b)):
            summ += int(b[i])
            p *= int(b[i])
        return p-summ