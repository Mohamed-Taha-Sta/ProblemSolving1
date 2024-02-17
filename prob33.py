# 1642
import heapq
from typing import List


# def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
#     # Getting max jumps according to how many ladders we have:
#     jumps = []
#     for i in range(len(heights) - 1):
#         if heights[i+1] - heights[i] > 0:
#             jumps.append((i, heights[i+1] - heights[i]))
#
#     print(jumps)
#     jumps.sort(key=lambda x: x[1], reverse=True)  # sort in-place
#     jumps = jumps[:ladders]
#     print(jumps)
#
#     for i in range(len(heights) - 1):
#         print(bricks)
#         if i in [jump[0] for jump in jumps]:  # Check if i is the first element of any tuple in jumps
#             pass
#         elif bricks < 0 < heights[i + 1] - heights[i]:
#             return i
#         else:
#             if heights[i+1] - heights[i] > 0:
#                 bricks -= heights[i+1] - heights[i]
#     return len(heights)

def furthestBuilding(heights: List[int], bricks: int, ladders: int) -> int:
    heap = []
    for i in range(len(heights) - 1):
        if heights[i+1] - heights[i] <= 0:
            continue
        bricks -= heights[i+1] - heights[i]
        heapq.heappush(heap, -(heights[i+1] - heights[i]))
        if bricks < 0:
            if ladders == 0:
                return i
            ladders -= 1
            bricks += -heapq.heappop(heap)
    return len(heights) - 1


if __name__ == '__main__':
    print(furthestBuilding(heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
    # print(furthestBuilding(heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
    # print(furthestBuilding(heights = [14,3,19,3], bricks = 17, ladders = 0))

    # Create an empty heap
    # heap = []
    #
    # # Add elements to the heap
    # heapq.heappush(heap, 3)
    # heapq.heappush(heap, 1)
    # heapq.heappush(heap, 4)
    # heapq.heappush(heap, 1)
    # heapq.heappush(heap, 5)
    #
    # print("The heap is: ", heap)
    #
    # # Remove element from the heap
    # print("Pop from the heap: ", heapq.heappop(heap))
    #
    # print("The heap after popping: ", heap)