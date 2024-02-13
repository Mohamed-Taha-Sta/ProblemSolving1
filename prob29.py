# 2108
from typing import List

def firstPalindrome(words: List[str]) -> str:
    for word in words:
        for i in range(len(word)):
            if word[i] != word[len(word)- 1 - i]:
                break
            elif i == len(word) - 1:
                return word
    return ""




if __name__ == '__main__':
    print(firstPalindrome(words = ["abc","car","ada","racecar","cool"]))
    print(firstPalindrome(words = ["notapalindrome","racecar"]))
    print(firstPalindrome(words = ["def","ghi"]))
