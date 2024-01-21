def numWaterBottles(numBottles: int, numExchange: int) -> int:
    allBottles = numBottles
    rest = numBottles
    while rest >= numExchange:
        newBottles = rest // numExchange
        allBottles += newBottles
        rest = newBottles + rest % numExchange
    return allBottles


if __name__ == '__main__':
    print(numWaterBottles(9, 3))
