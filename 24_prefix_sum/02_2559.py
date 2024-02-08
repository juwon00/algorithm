import sys

input = sys.stdin.readline

n, k = map(int, input().split())
data = list(map(int, input().split()))

prefix_num = [0]
sum_value = 0

for i in data:
    sum_value += i
    prefix_num.append(sum_value)
print(prefix_num)

left, right = 0, k
result = prefix_num[right] - prefix_num[left]
while right <= n:
    print(left, right, result, prefix_num[right] - prefix_num[left])
    result = max(result, prefix_num[right] - prefix_num[left])
    left += 1
    right += 1

print(result)
