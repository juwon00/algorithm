n,x = input().split()
n = int(n)
x = int(x)

# 위의 3줄을 1줄로 표현
# n,x = map(int, input().split())

li = list(map(int, input().split()))

for i in range(n):
    if li[i] < x:
        print(li[i], end=" ") 