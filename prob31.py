# 2971
from typing import List


def largestPerimeter(nums: List[int]) -> int:
    nums.sort()
    while len(nums) > 1:
        max_int = nums[-1]
        nums.pop()
        rest_sum = sum(nums)
        if rest_sum > max_int:
            return rest_sum + max_int
    return - 1

if __name__ == '__main__':
    print(largestPerimeter(nums = [5,5,5]))
    print(largestPerimeter(nums = [1,12,1,2,5,50,3]))
    print(largestPerimeter(nums = [5,5,50]))