class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            rows = len(matrix)-1
            cols = len(matrix[0])
            result = []
            for i in range(cols):
                row = []
                for j in range(rows,-1,-1):
                    row.append(matrix[j][i])
                result.append(row)
            return result

        for i in range(4):
            mat=rotate(mat)
            if mat==target:
                return True
        return False
                                                                                          
            


