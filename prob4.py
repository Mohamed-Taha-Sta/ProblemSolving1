# 2507

import math

def smallestValue(n: int) -> int:
    while True:
        summing = 0
        updated_n = n
        for i in range(2, math.isqrt(updated_n) + 1):
            while updated_n % i == 0:
                summing += i
                updated_n //= i
        if updated_n > 1:
            summing += updated_n
        if summing == n:
            return n
        n = summing


if __name__ == '__main__':
    print(smallestValue(15))
