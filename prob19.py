# 1043
from typing import List


def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    dp = [0] * k
    dp[0] = arr[0]
    for i in range(1,len(arr)):
        max_i = 0
        curr_max = 0
        for j in range(i, i - k, -1):
            if j < 0:
                break
            curr_max = max(arr[j], curr_max)
            window_size = i - j + 1
            curr_sum = curr_max * window_size
            sub_sum = dp[(j - 1) % k] if j > 0 else dp[-1]
            max_i = max(curr_sum+sub_sum,max_i)
        dp[i % k] = max_i
    return dp[(len(arr) - 1) % k]

# def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
#     dp = [0] * (len(arr) + 1)
#     for i in range(1, len(arr) + 1):
#         curr_max = 0
#         for j in range(1, min(i, k) + 1):
#             curr_max = max(curr_max, arr[i - j])
#             dp[i] = max(dp[i], dp[i - j] + curr_max * j)
#     return dp[len(arr)]


if __name__ == '__main__':
    print(maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))