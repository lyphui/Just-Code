from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        num=len(matrix)
        for i in range(num):
            for j in range(i):
                matrix[j][i],matrix[i][j]=\
                    matrix[i][j],matrix[j][i]
        print(matrix)


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

s=Solution()
s.rotate(matrix)