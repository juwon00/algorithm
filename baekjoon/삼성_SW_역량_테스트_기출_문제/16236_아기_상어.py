import heapq
import sys

input = sys.stdin.readline


def bfs(i, j, size, cnt):
    heap = []
    heapq.heappush(heap, (0, i, j))
    # q = deque()  <-- 첫번째 놓친점 heapq가 아닌 deque로 선언한것
    # q.append((i, j, 0))
    visited = [[False] * n for _ in range(n)]
    while heap:
        # x, y, dist = q.popleft()
        dist, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        visited[x][y] = True
        print("now", x, y, dist)

        if 0 < graph[x][y] < size:
            return x, y, dist, cnt + 1
        if size < graph[x][y] < 9:
            continue

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                # q.append((nx, ny, dist + 1))
                heapq.heappush(heap, (dist + 1, nx, ny))
                print(nx, ny, dist + 1)

    return 0


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
for g in graph:
    print(g)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_x, start_y = i, j
print("start", start_x, start_y)

x, y = start_x, start_y
size = 2
cnt = 0
answer = 0
while True:
    print(">>>>", x, y)
    result = bfs(x, y, size, cnt)
    if result == 0:
        break
    mx, my, dist, cnt = result[0], result[1], result[2], result[3]
    answer += dist
    if size == cnt:
        cnt = 0
        size += 1
    if size == 9:  # <-- 두번째 놓친점 size가 9보다 커지면 23번째 줄 때문에 무한루프를 도는점
        size = 8
    print(mx, my, dist, size, cnt)
    graph[x][y] = 0
    graph[mx][my] = 9
    x, y = mx, my
    print("answer", answer)
    for g in graph:
        print(g)
    print()
print(answer)
