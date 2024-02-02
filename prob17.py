# 704
from typing import List


def search(nums: List[int], target: int) -> int:
    L, R = 0, len(nums) - 1
    while L <= R:
        mid = (L+R)//2
        if nums[mid] < target:
            L = mid + 1
        elif nums[mid] > target:
            R = mid
        else:
            return mid
    return -1





if __name__ == '__main__':
    print(search(nums = [-1,0,3,5,9,12], target = 9))