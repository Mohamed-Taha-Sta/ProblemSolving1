# 2149
from typing import List

def find_index(lst, element):
    return lst.index(element) if element in lst else -1

def rearrangeArray(nums: List[int]) -> List[int]:
    negatives = list(filter(lambda i: i < 0, nums))
    positives = list(filter(lambda i: i >= 0, nums))
    for index, position in enumerate(range(0, len(nums), 2), start=0):
        nums[position] = positives[index]
        nums[position + 1] = negatives[index]
    return nums

if __name__ == '__main__':
    print(rearrangeArray(nums = [3,1,-2,-5,2,-4]))
    print(rearrangeArray(nums = [-1,1]))