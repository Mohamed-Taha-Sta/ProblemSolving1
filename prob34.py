# 231

def isPowerOfTwo(n: int) -> bool:
    if n == 0:
        return False
    elif n == 1:
        return True
    else:
        i: int = 1
        while i <= n:
            if i == n:
                return True
            else:
                i *= 2
    return False

if __name__ == '__main__':
    print(isPowerOfTwo(n = 1))
    # print(isPowerOfTwo(n = 16))
    # print(isPowerOfTwo(n = 3))