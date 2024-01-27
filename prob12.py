# 2379


def minimumRecolors(blocks: str, k: int) -> int:
    i = 0
    blocksToPaint = float('inf')
    while i < len(blocks) - k + 1:
        white_blocks = blocks[i:i + k].count('W')
        if white_blocks == 0: return 0
        if white_blocks < blocksToPaint:
            blocksToPaint = white_blocks
        i += 1
    return blocksToPaint


if __name__ == '__main__':
    print(minimumRecolors("WBBWWBBWBW", 7))
    print(minimumRecolors("WBWBBBW", 2))
