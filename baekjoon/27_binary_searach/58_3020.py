from bisect import bisect_left

n, h = map(int, input().split())

top = []
bottom = []

for i in range(n):
    if i % 2 == 0:
        bottom.append(int(input()))
    else:
        top.append(int(input()))

top.sort()
bottom.sort()

print(n, h)
print(top, bottom)
cnt = 1
min_val = float('inf')

for height in range(1, h+1):
    t, b = bisect_left(top, (h+1) - height), bisect_left(bottom, height)
    total = n - (t + b)

    if total < min_val:
        min_val = total
        cnt = 1
    elif total == min_val:
        cnt += 1

print(min_val, cnt)

