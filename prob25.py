# 279

import math

def numSquares(n: int) -> int:
    dp = [n+1] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        j = 1
        while j*j <= i:
            dp[i] = min(dp[i], dp[i - j*j] + 1)
            j += 1
    return dp[n]

if __name__ == '__main__':
    print(numSquares(n = 12))