# 766
from typing import List
# [[1,2,3,4],
#  [5,1,2,3],
#  [9,5,1,2]]

def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i]) - 1):
            if matrix[i][j] != matrix[i+1][j+1]:
                return False
    return True

if __name__ == '__main__':
    print(isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(isToeplitzMatrix([[1,2],[2,2]]))


