from collections import deque

n, k = map(int, input().split())
q = deque()
for i in range(1, n + 1):
    q.append(str(i))
result = []

while q:
    for j in range(k - 1):
        q.append(q.popleft())
    result.append(q.popleft())

print(f"<{', '.join(result)}>")
