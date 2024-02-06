# 49
from collections import defaultdict
from typing import List


# def groupAnagrams(strs: List[str]) -> List[List[str]]:
#     answer = []
#     while strs:
#         aux = []
#         curr_word = strs[0]
#         for word in strs[:]:
#             if sorted(word) == sorted(curr_word):
#                 aux.append(word)
#                 strs.remove(word)
#         answer.append(aux)
#     return answer

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    answerDict = defaultdict(list)
    for word in strs:
        sortedWord = tuple(sorted(word))
        answerDict[sortedWord].append(word)
    return  list(answerDict.values())



if __name__ == '__main__':
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
