import sys

n, m, b = map(int, sys.stdin.readline().split())
block = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


result = sys.maxsize
result_height = 0

for height in range(257):

    use_block = 0
    take_block = 0

    for i in range(n):
        block_row = block[i]  # 시간 줄이는 방법 !
        for j in range(m):
            if block_row[j] > height:
                take_block += block[i][j] - height
            elif block_row[j] < height:
                use_block += height - block[i][j]

    if use_block <= take_block + b:

        if take_block * 2 + use_block <= result:
            result = take_block * 2 + use_block
            result_height = height

print(result, result_height)
