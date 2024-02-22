import sys

input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

prefix_sum = [0]
sum_value = 0
for d in data:
    sum_value += d
    prefix_sum.append(sum_value)
print(prefix_sum)

m = int(input())
for _ in range(m):
    i, j = map(int, input().split())
    print(i, j)
    print(prefix_sum[j] - prefix_sum[i - 1])
