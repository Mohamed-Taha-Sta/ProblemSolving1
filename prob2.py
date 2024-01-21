from typing import List


def applyOperations(nums: List[int]) -> List[int]:
    zeros = 0
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = nums[i] * 2
            nums[i + 1] = 0
    last_0 = len(nums) - 1
    zeros = nums.count(0)
    nums = [i for i in nums if i != 0] + ([0] * zeros)
    return nums


if __name__ == '__main__':
    print(applyOperations([1, 2, 2, 1, 1, 0]))
