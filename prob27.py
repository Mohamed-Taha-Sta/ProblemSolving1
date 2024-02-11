# 1051
from typing import List


def heightChecker(heights: List[int]) -> int:
    expected = sorted(heights)
    return sum(1 for i in range(len(heights)) if heights[i] != expected[i])

if __name__ == '__main__':
    print(heightChecker(heights = [1,1,4,2,1,3]))