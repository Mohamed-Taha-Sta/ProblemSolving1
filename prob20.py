# 76
from collections import Counter


# def minWindow(s: str, t: str) -> str:
#     def verifyExist(s1: str, s2: str) -> bool:
#         counter_s1 = Counter(s1)
#         counter_s2 = Counter(s2)
#
#         for char, count in counter_s2.items():
#             if counter_s1[char] < count:
#                 return False
#         return True
#     if len(t) > len(s):
#         return ""
#     if t == s:
#         return s
#     cand = []
#     length_S = len(s)
#     for j in range(length_S):
#         if s[j] not in t:
#             continue
#         else:
#             for i in range(j, length_S):
#                 if verifyExist(s[j:min(i, length_S)+1], t):
#                     cand.append(s[j:min(i, length_S)+1])
#                     break
#
#     if not cand: return ""
#     return min(cand, key=len)


# def minWindow(s: str, t: str) -> str:
#     if len(t) > len(s):
#         return ""
#     if t == s:
#         return s
#     cand = []
#     length_S = len(s)
#     t_counter = Counter(t)
#
#     for j in range(length_S):
#         letters_found = []
#         if s[j] not in t_counter:
#             continue
#         else:
#             for i in range(j, length_S):
#                 if s[i] in t_counter:
#                     letters_found.append(s[i])
#                 if Counter(letters_found) & t_counter == t_counter:
#                     cand.append(s[j:i+1])
#                     break
#     if not cand:
#         return ""
#     return min(cand, key=len)

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""

    dict_t = Counter(t)
    required = len(dict_t)
    l, r = 0, 0 # These are pointers used to expand and shrink the sliding window.
    formed = 0 # The formed variable is the number of unique characters in the sliding window that match with the characters in t.
    window_counts = {} # counts the character in s as we go on
    # The `ans` tuple below is used to store the length of the smallest substring initiated at infinity
    # because any length is going to be smaller than infinity later on when we test,
    # and the start and end indices of this substring respectively.
    ans = float("inf"), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1

        r += 1
        print(window_counts)

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

if __name__ == '__main__':
    print(minWindow(s="ADOBECODEBANC", t="ABC"))
    print(minWindow(s="ab", t="a"))

