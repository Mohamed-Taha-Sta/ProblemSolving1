#2945
from functools import reduce
from typing import List


# def findMaximumLength(nums: List[int]) -> int:
#     i = 0
#     j = 2
#     for element in nums:
#         spaceful = nums[i:j]
#         while reduce(lambda a,b:a+b, spaceful) < reduce(lambda a,b:a+b,nums[j:]):
#             j += 1
#             spaceful = nums [i:j]
#         # while reduce()
