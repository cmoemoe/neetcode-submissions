class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ogZeros = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    ogZeros.append((row, col))

        for coord in ogZeros:
            r = coord[0]
            c = coord[1]
            while r >= 0:
                matrix[r][c] = 0
                r -= 1
            r = coord[0]
            c = coord[1]
            while r < len(matrix):
                matrix[r][c] = 0
                r += 1
            r = coord[0]
            c = coord[1]
            while c >= 0:
                matrix[r][c] = 0
                c -= 1
            r = coord[0]
            c = coord[1]
            while c < len(matrix[0]):
                matrix[r][c] = 0
                c += 1
                    
        