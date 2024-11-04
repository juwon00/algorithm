from collections import deque

n = int(input())

if n == 1:
    print(1)
    exit()

q = deque()
for i in range(1, n + 1):
    q.append(i)

while q:
    q.popleft()
    q.append(q.popleft())
    if len(q) == 1:
        break
print(q.popleft())
