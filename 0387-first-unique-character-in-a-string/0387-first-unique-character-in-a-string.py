from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s)==len(set(s))/2:
                return -1
        for i,j in Counter(s).items():
            if j>=2:
               continue
            else:
                return s.find(i)
        return -1