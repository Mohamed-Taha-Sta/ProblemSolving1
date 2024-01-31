# 127

from typing import List
from collections import deque

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        currentWord, level = queue.popleft()
        if currentWord == endWord:
            return level

        for i in range(len(currentWord)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = currentWord[:i] + c + currentWord[i+1:]
                if nextWord in wordSet:
                    queue.append((nextWord, level + 1))
                    wordSet.remove(nextWord)
    return 0

if __name__ == '__main__':
    print(ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
    # print(ladderLength("hit","cog",["hot","dot","dog","lot","log"]))
