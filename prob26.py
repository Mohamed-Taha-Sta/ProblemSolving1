# 647

def countSubstrings(s: str) -> int:
    n = len(s)
    ans = 0
    for center in range(2*n - 1):
        left = center // 2
        right = left + center % 2
        while left >= 0 and right < n and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
    return ans



# def countSubstrings(s: str) -> int:
#     palind = []
#     for i in range(len(s)):
#         palind.append(s[i])
#         if i > 0:
#             j = i - 1
#         else:
#             continue
#         while j >= 0:
#             aux_Word = s[j:i + 1]
#             if aux_Word in palind:
#                 palind.append(aux_Word)
#             else:
#                 pal = True
#                 for k in range(len(aux_Word)):
#                     if aux_Word[k] != aux_Word[len(aux_Word) - 1 - k]:
#                         pal = False
#                 if pal:
#                     palind.append(aux_Word)
#             j -= 1
#     print(palind)
#     return len(palind)


if __name__ == '__main__':
    # print(countSubstrings(s = "abc"))
    print(countSubstrings(s = "aaa"))
