import sys

input = sys.stdin.readline

n, k, b = map(int, input().split())
broken = [0] * (n + 1)

for _ in range(b):
    broken[int(input())] = 1
print(broken)

prefix_sum = []
sum_value = 0
for i in broken:
    sum_value += i
    prefix_sum.append(sum_value)
print(prefix_sum)

result = b
for i in range(k, n + 1):
    result = min(result, prefix_sum[i] - prefix_sum[i - k])  # k개의 연속된 구간에서 수리해야 할 신호등 개수
    print(i, prefix_sum[i], prefix_sum[i - k], prefix_sum[i] - prefix_sum[i - k])
print(result)
