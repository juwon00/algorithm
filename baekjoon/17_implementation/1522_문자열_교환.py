x = input()
n = len(x)
a_count = x.count('a')
x = x + x
result = 1000

for i in range(n):
    tmp = x[i:i + a_count].count('b')
    result = min(result, tmp)
print(result)
