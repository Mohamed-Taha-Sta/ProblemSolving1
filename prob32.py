# 1481
from collections import Counter, deque
from typing import List

# Greedy
# def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
#     counter = Counter(arr)
#     list_counter = list(counter.items())
#     list_counter.sort(key=lambda x:x[1])
#     while k > 0:
#         if list_counter[0][1] == 1:
#             list_counter.pop(0)
#         else:
#             list_counter[0] = (list_counter[0][0], list_counter[0][1] - 1)
#         k -= 1
#     return len(list_counter)

def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    counter = Counter(arr)
    list_values = deque(sorted(counter.values()))
    while k > 0:
        if list_values[0] == 1:
            list_values.popleft()
        else:
            list_values[0] -= 1
        k -= 1
    return len(list_values)


if __name__ == '__main__':
    # print(findLeastNumOfUniqueInts(arr = [5,5,4], k = 1))
    print(findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))
