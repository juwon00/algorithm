from collections import deque

n, m = map(int, input().split())
graph = [i for i in range(101)]
for _ in range(n + m):
    a, b = map(int, input().split())
    graph[a] = b
print(graph)

visited = [0] * 101

q = deque()
q.append(1)
visited[1] = 1

while q:
    now = q.popleft()
    print()
    print("now", now)

    for i in range(1, 7):
        dice = now + i

        if dice > 100:
            continue

        cnt = graph[dice]
        print(dice, cnt)

        if visited[cnt] == 0:
            print("cnt", cnt)
            q.append(cnt)
            visited[cnt] = visited[now] + 1
    print(visited)


print(visited[100] - 1)
