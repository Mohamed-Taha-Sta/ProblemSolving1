# 125

def isPalindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    length = len(s) - 1
    for i in range(length):
        print(i)
        if s[i] != s[length - i]:
            return False
    return True


if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))