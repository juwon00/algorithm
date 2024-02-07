import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
prefix_sum = [0]

sum_value = 0
for i in range(n):
    sum_value += num[i]
    prefix_sum.append(sum_value)
print(prefix_sum)

for _ in range(m):
    a, b = map(int, input().split())
    print(a, b)
    print(prefix_sum[b] - prefix_sum[a - 1])
