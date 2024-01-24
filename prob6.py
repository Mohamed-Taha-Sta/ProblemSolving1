# 949
from typing import List
from itertools import permutations


def largestTimeFromDigits(arr: List[int]) -> str:
    for p in sorted(permutations(arr), reverse=True):
        if p[0]*10 + p[1] < 24 and p[2] < 6:
            return f"{p[0]}{p[1]}:{p[2]}{p[3]}"
    return ""


if __name__ == '__main__':
    print(largestTimeFromDigits([1,2,3,0]))

