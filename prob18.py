# 74
from typing import List


# def searchMatrix(matrix: List[List[int]], target: int) -> bool:
#     # L, R = matrix[0], matrix[len(matrix) - 1: len(matrix[0])][0]
#     L, R = (0, 0), (len(matrix) - 1, len(matrix[0]) - 1)
#     # print(L)
#     # print(R)
#     while L <= R:
#         # print(matrix[L[0]][L[1]])
#         # print(matrix[R[0]][R[1]])
#         mid = ((L[0] + R[0]) // 2, (L[1] + R[1]) // 2)
#         midValue = matrix[mid[0]][mid[1]]
#         print(mid)
#         print(midValue)
#         print("----")
#         if midValue < target:
#             L = mid[0]+1, mid[1]+1
#         elif midValue > target:
#             R = mid[0]-1, mid[1]-1
#         else:
#             return True
#
#     return False

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        print(mid)
        print(mid // cols,mid % cols)
        print('--------------')
        mid_value = matrix[mid // cols][mid % cols]

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


if __name__ == '__main__':
    print(searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3))
