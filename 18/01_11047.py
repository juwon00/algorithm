n, k = map(int, input().split())
li = list()

for i in range(n):
    a = int(input())
    li.append(a)

li.sort(reverse=True)

count = 0

for coin in li:
    count = count + k // coin
    k = k % coin

print(count)
