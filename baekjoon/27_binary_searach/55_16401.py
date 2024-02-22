import sys
input = sys.stdin.readline

m, n = map(int, input().split())
snacks = list(map(int, input().split()))

left = 1
right = max(snacks)
result = 0

while left <= right:
    mid = (left + right) // 2
    # print(mid)

    mid_cnt = 0
    for snack in snacks:
        mid_cnt += snack // mid
    # print("mid_cnt", mid_cnt)

    if mid_cnt >= m:
        result = max(mid, result)
        left = mid + 1
    else:
        right = mid - 1

print(result)
