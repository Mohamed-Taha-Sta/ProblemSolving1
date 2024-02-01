# 2966
from typing import List


def divideArray(nums: List[int], k: int) -> List[List[int]]:
    answer = []
    # we sort our array knowing that obviously the closest elements are those that have the biggest chance of being
    # less or equal to k.
    nums.sort()
    # we group the element in chunks of 3, knowing that n is divisible by 3.
    for i in range(0, len(nums), 3):
        answer.append(nums[i:i + 3])
    # greedy verification:
    for element in answer:
        for i in range(len(element)):
            for j in range(i, len(element)):
                if abs(element[i] - element[j]) > k:
                    return []
    return answer


if __name__ == '__main__':
    print(divideArray([1, 3, 4, 8, 7, 9, 3, 5, 1], 2))
    print(divideArray([1,3,3,2,7,3], 3))
