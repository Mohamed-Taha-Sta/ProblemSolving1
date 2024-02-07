# 451
from collections import defaultdict


def frequencySort(s: str) -> str:
    occDict = defaultdict(str)
    for char in s:
        occDict[char] = occDict.get(char, "") + char
    return "".join(sorted(occDict.values(),key=len,reverse=True))


if __name__ == '__main__':
    print(frequencySort(s = "tree"))
    print(frequencySort(s = "cccaaa"))
    print(frequencySort(s = "Aabb"))













