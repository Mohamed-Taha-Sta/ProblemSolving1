# 387

def firstUniqChar(s: str) -> int:
    map = {}
    for c in s:
        map[c] = map.get(c, 0) + 1
    for i in range(len(s)):
        if map[s[i]] == 1:
            return i
    return -1



if __name__ == '__main__':
    print(firstUniqChar(s = "leetcode"))
    print(firstUniqChar(s = "loveleetcode"))
    print(firstUniqChar(s = "aabb"))