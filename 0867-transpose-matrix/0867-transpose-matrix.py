class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        transpose = []
        for c in range(cols):
            new_row = []
            for r in range(rows):
                new_row.append(matrix[r][c])
            transpose.append(new_row)

        return transpose


        