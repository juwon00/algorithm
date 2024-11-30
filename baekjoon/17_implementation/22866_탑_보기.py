# 다시 풀어볼 문제

n = int(input())
building = list(map(int, input().split()))
INF = int(1e9)
cnt = [0] * n
nearest = [INF] * n

stack = []
for i in range(n):
    print(i, "-", building[i])
    while stack and building[stack[-1]] <= building[i]:
        stack.pop()
    print(stack)
    cnt[i] += len(stack)
    if stack:
        nearest[i] = stack[-1]
    stack.append(i)
    print()
print(cnt)
print(nearest)
print()

stack = []
for i in range(n - 1, -1, -1):
    print(i, "-", building[i])
    while stack and building[stack[-1]] <= building[i]:
        stack.pop()
    print(stack)
    cnt[i] += len(stack)
    if stack:
        if abs(i - stack[-1]) < abs(i - nearest[i]):
            nearest[i] = stack[-1]
    stack.append(i)
    print()
print(cnt)
print(nearest)
print()

for i in range(n):
    if cnt[i] > 0:
        print(cnt[i], nearest[i] + 1)
    else:
        print(0)
