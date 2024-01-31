# 739

from typing import List


def dailyTemperatures(temperatures: List[int]) -> List[int]:
    length = len(temperatures)
    stack = []
    answer = [0] * length
    for i in range(length):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            head = stack.pop()
            print("--->", head)
            answer[head] = i - head
        stack.append(i)
    return answer


if __name__ == '__main__':
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
