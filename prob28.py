# 169
from typing import List


def majorityElement(nums: List[int]) -> int:
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    return max(count, key=count.get)






if __name__ == '__main__':
    print(majorityElement(nums = [3,2,3]))
    print(majorityElement(nums = [2,2,1,1,1,2,2]))


