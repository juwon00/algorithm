import sys

input = sys.stdin.readline

n, c = map(int, input().split())
x = []
for _ in range(n):
    x.append(int(input()))
x.sort()

print(n, c, x)

start = 1
end = x[n - 1] - x[0]
result = 0

while start <= end:
    print()
    mid = (start + end) // 2

    count = 1
    current = x[0]

    for i in range(1, len(x)):
        if x[i] - current >= mid:
            print(x[i])
            count += 1
            current = x[i]

    print(start, end, mid)
    print(count)

    if count >= c:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
