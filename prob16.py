# 1291
from typing import List


def sequentialDigits(low: int, high: int) -> List[int]:
    seq = "123456789"
    answer = []
    number = low
    while number < high:
        strNbr = str(number)
        lenStrNbr = len(strNbr)
        print('number',number,'len', lenStrNbr)
        indx = seq.find(strNbr[0])
        sequential_Number = seq[indx:indx + lenStrNbr]
        intSeqNbr = int(sequential_Number)
        if low <= intSeqNbr <= high and intSeqNbr not in answer:
            answer.append(intSeqNbr)
        number += 10 ** (lenStrNbr - 1)
    return answer

if __name__ == '__main__':
    # print(sequentialDigits(low = 100, high = 300))
    # print(sequentialDigits(low = 1000, high = 13000))
    print(sequentialDigits(low = 10, high = 1000000000))