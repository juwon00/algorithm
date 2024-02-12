n, m = map(int, input().split())
data = list(map(int, input().split()))

prefix_sum = []
sum_value = 0
remainder = [0] * m

for i in data:
    print(i)
    sum_value += i
    prefix_sum.append(sum_value)
    remainder[sum_value % m] += 1
print(prefix_sum)
print(remainder)

result = remainder[0]
for i in remainder:
    print(i)
    result += i * (i - 1) // 2
print(result)
