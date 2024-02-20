# 268
from typing import List


# def missingNumber(nums: List[int]) -> int:
#     if 0 not in nums:
#         return 0
#     nums.sort()
#     for i in range(len(nums) - 1):
#         if nums[i] + 1 != nums[i+1]:
#             return nums[i] + 1
#     return nums[len(nums) - 1] + 1
def missingNumber(nums: List[int]) -> int:
    aux_list = [-1]*(len(nums) + 1)
    for i in range(len(nums)):
        aux_list[nums[i]] = 1
    return aux_list.index(-1)

if __name__ == '__main__':
    # print(missingNumber(nums = [3,0,1]))
    # print(missingNumber(nums = [0,1]))
    print(missingNumber(nums = [9,6,4,2,3,5,7,0,1]))


