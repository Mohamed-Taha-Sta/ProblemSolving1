from functools import *

def differenceOfSums(n: int, m: int) -> int:
    num2 = reduce(lambda a, b: a + b, [element for element in range(1, n+1) if element % m == 0])
    num1 = reduce(lambda a, b: a + b, [element for element in range(1, n+1) if element % m != 0])
    return num1 - num2


if __name__ == '__main__':
    print(differenceOfSums(12,3))
