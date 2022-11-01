n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # a배열의 가장 큰 수와 b배열의 가장 작은수를 차례대로 곱해서 더하면
b.sort(reverse=True) # 최소값을 구할 수 있다

sum = 0
for i in range(n):
    sum = sum +a[i] * b[i]

print(sum)