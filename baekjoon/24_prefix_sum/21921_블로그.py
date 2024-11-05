n, x = map(int, input().split())
blog = list(map(int, input().split()))

prefix_sum = [0]
sum_value = 0
for b in blog:
    sum_value += b
    prefix_sum.append(sum_value)
print(prefix_sum)

visitors = []
for i in range(n, x - 1, -1):
    print(i, i - x)
    visitors.append(prefix_sum[i] - prefix_sum[i - x])
print(visitors)

max_value = max(visitors)
if max_value == 0:
    print("SAD")
else:
    print(max_value)
    print(visitors.count(max_value))
