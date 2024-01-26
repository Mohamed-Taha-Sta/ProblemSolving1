# 2516
# Needs to be revised

# def takeCharacters(s: str, k: int) -> int:
#     cpt_a = 0
#     cpt_b = 0
#     cpt_c = 0
#
#     ind_A = 0
#     ind_B = 0
#     ind_C = 0
#
#     ind_A2 = 0
#     ind_B2 = 0
#     ind_C2 = 0
#
#     cpt_a2 = 0
#     cpt_b2 = 0
#     cpt_c2 = 0
#     for i in range((len(s) - 1)):
#         if s[i] == 'a':
#             if cpt_a == k: ind_A = i
#             else: cpt_a+=1
#         elif s[i] == 'b':
#             if cpt_b == k: ind_B = i
#             else: cpt_b+=1
#         elif s[i] == 'c':
#             if cpt_c == k: ind_C = i
#             else: cpt_c+=1
#         else:
#             return -1
#
#     for i in reversed(range((len(s) - 1))):
#         if s[i] == 'a':
#             if cpt_a2 == k: ind_A2 = len(s) - i - 1
#             else: cpt_a2 += 1
#         elif s[i] == 'b':
#             if cpt_b2 == k: ind_B2 = len(s) - i - 1
#             else: cpt_b2 += 1
#         elif s[i] == 'c':
#             if cpt_c2 == k: ind_C2 = len(s) - i - 1
#             else: cpt_c2 += 1
#         else:
#             return -1
#
#     sum = 0
#     if ind_A < ind_A2:
#         sum += cpt_a2
#     else:
#         sum += cpt_a
#     if ind_B < ind_B2:
#         sum += cpt_b2
#     else:
#         sum += cpt_b
#     if ind_C < ind_C2:
#         sum += cpt_c2
#     else:
#         sum += cpt_c
#
#     return sum

def takeCharacters(s: str, k: int) -> int:
    count = {'a': 0, 'b': 0, 'c': 0}
    for char in s:
        if char in count:
            count[char] += 1

    if any(val < k for val in count.values()):
        return -1

    left, right = 0, len(s) - 1
    seen = {'a': 0, 'b': 0, 'c': 0}

    while all(val < k for val in seen.values()):
        if seen[s[left]] < k:
            seen[s[left]] += 1
            left += 1
        elif seen[s[right]] < k:
            seen[s[right]] += 1
            right -= 1

    return left + len(s) - right

if __name__ == '__main__':
    print(takeCharacters("aabaaaacaabc",2))